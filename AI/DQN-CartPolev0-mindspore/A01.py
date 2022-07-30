import random
from mindspore import dtype
from mindspore import load_param_into_net
import mindspore as ms
from mindspore import nn
from mindspore import Tensor
from mindspore.dataset import GeneratorDataset
import numpy as np  # 导入numpy
import gym  # 导入gym
from mindspore.common import initializer as init
# 超参数
BATCH_SIZE = 16  # 样本数量
LR = 0.01  # 学习率
EPSILON = [0.6,0.75,0.9,0.95,1]  # greedy policy
GAMMA = 0.9  # reward discount
TARGET_REPLACE_ITER = 100  # 目标网络更新频率
MEMORY_CAPACITY = 2000  # 记忆库容量
env = gym.make("CartPole-v0").unwrapped  # 使用gym库中的环境：CartPole，且打开封装
N_ACTIONS = env.action_space.n  # 动作个数 
N_STATES = env.observation_space.shape[0]  # 状态个数
b_a=None
p=0
class MyNet(nn.Cell):
    def __init__(self):
        super(MyNet, self).__init__()
        self.fc1 = nn.Dense(N_STATES, 32, weight_init=init.Normal(0.1))
        # self.fc2 = nn.Dense(32, 16)
        self.fc3 = nn.Dense(32, N_ACTIONS, weight_init=init.Normal(0.1))
        self.relu = nn.ReLU()

    def construct(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        # x = self.fc2(x)
        # x = self.relu(x)
        x = self.fc3(x)
        return x


class MyLoss(nn.LossBase):
    def __init__(self, reduction="mean"):
        """初始化并求loss均值"""
        super(MyLoss, self).__init__(reduction)
        self.square = ms.ops.Square()
    def construct(self, base, target):
        q_eval = ms.ops.GatherD()(base, 1, b_a)
        x = self.square(q_eval - target)
        return self.get_loss(x)  # 返回loss均值


class DQN(object):

    def __init__(self):
        self.eval_net, self.target_net = MyNet(), MyNet()  # 利用Net创建两个神经网络: 评估网络和目标网络
        self.learn_step_counter = 0  # for target updating
        self.memory_counter = 0  # for storing memory
        self.memory = np.zeros((MEMORY_CAPACITY, N_STATES * 2 + 2))  # 初始化记忆库，一行代表一个transition
        self.optimizer = nn.Adam(self.eval_net.trainable_params(),learning_rate=LR)  # 使用Adam优化器 (输入为评估网络的参数和学习率)
        self.loss_func = MyLoss()
        self.Modle = ms.train.Model(self.eval_net, self.loss_func, self.optimizer)
        self.op = ms.ops.ReduceMax(keep_dims=True)

    @staticmethod
    def data_load(s, target):
        def fun(s, target):
            yield np.array(s).astype(np.float32), np.array(target).astype(np.float32)

        return GeneratorDataset(list(fun(s, target)), column_names=['state', 'target'])

    def action_select(self, x):
        if random.random() < EPSILON[p]:
            x = Tensor([x], dtype=ms.float32)
            action_value = self.eval_net(x)
            action = ms.ops.Argmax(axis=1)(action_value)[0].asnumpy().tolist()

        else:
            action = random.randint(0, N_ACTIONS-1)

        return action

    def store_transition(self, s, a, r, s_):
        global p
        experience = np.hstack((s, [a, r], s_))
        index = self.memory_counter % MEMORY_CAPACITY
        self.memory[index] = experience
        self.memory_counter += 1
        if self.memory_counter in[2500,3000,4000,5000]:
            p+=1

    def learn(self):
        global b_a
        if self.learn_step_counter % TARGET_REPLACE_ITER == 0:
            params = self.eval_net.parameters_dict()
            load_param_into_net(self.target_net, params)
        self.learn_step_counter += 1

        sample_index = np.random.randint(0,MEMORY_CAPACITY,BATCH_SIZE)
        b_memory = self.memory[sample_index]
        b_s = Tensor(b_memory[:, :N_STATES], dtype=ms.float32)
        b_a = Tensor(b_memory[:, N_STATES:N_STATES + 1], dtype=ms.int32)
        b_r = Tensor(b_memory[:, N_STATES + 1:N_STATES + 2], dtype=ms.float32)
        b_s_ = Tensor(b_memory[:, -N_STATES:], dtype=ms.float32)

        # q_eval=ms.ops.GatherD(self.eval_net(b_s),1,b_a)
        q_next = self.target_net(b_s_)
        q_target = b_r + GAMMA * self.op(q_next, 1)
        data = self.data_load(b_s, q_target)
        self.Modle.train(1, data)


def run():
    dqn = DQN()
    n=20
    t=0
    while True:
        t+=1
        s = env.reset()
        env.render()
        reward = 0
        while True:
            a = dqn.action_select(s)

            s_, r, done1,done2, info = env.step(a)
            env.render()

            reward += r
            dqn.store_transition(s, a, r, s_)

            s = s_
            if dqn.memory_counter%100==0:
                print("动作步数：{} 选择率{}".format(dqn.memory_counter,EPSILON[p]))
            if dqn.memory_counter >= MEMORY_CAPACITY:
                dqn.learn()
            if done1 or done2:
                print("第{}轮:  奖励为：{}".format(t, reward))
                break
        if t==n:
            print("已训练{}轮".format(n))
            ret = input("是否继续?")
            if ret!="No":
                i=0
                n=int(input("继续多少轮？"))
            else:
                break

    ms.save_checkpoint(dqn.target_net, "DQN.ckpt")
run()