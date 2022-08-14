const pool=require("./pool.js")
const user=pool.user
const dish=pool.dish
const orders=pool.order
const http =require("http")
var username='abc'
const sever=http.createServer((req,res)=>{

    let url=req.url
    console.log(url)

    res.writeHead(200, {
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Origin': 'null',
        'Access-Control-Allow-Headers': 'Content-type',
        'Content-type': 'application/json;charset=UTF-8'
    })
    let data=''
    req.on("data",(chunk)=>{
        data+=chunk.toString()
    })
    req.on("end",()=>{
        if (data != '') {
            data=JSON.parse(data)
            console.log(data)

            if(url==='/login'){
                login(data,res)
            }
            else if(url==='/logon'){
                logon(data,res)
            }
            else if(url==='/add_dish'){
                add_dish(data,res)
            }
            else if(url==='/getdishes'){
                get_dishes(data,res)
            }
            else if(url==='/del_dish'){
                del_dish(data,res)
            }
            else if(url==='/update_dish'){
                update_dish(data,res)
            }
            else if(url==='/getusers'){
                get_users(null,res)
            }
            else if(url==='/del_user'){
                del_user(data,res)
            }
            else if(url==='/update_user'){
                update_user(data,res)
            }
            else if(url==='/save_order'){
                save_order(data,res)
            }
            else if(url==='/getorders'){
                get_orders(data,res)
            }
            else{
                console.log(data)
                res.end()
            }
        }else{
            res.end()
        }

    })
})
sever.listen(3000)

function login(data,res){

    user.find(data,(err,ret)=>{
        if (err) {
            console.log("查找err")
        } else {
            console.log(ret)
            if(ret.length!=0){
                let User={
                    username:ret[0].username,
                    passward:ret[0].passward,
                    manager:ret[0].manager
                }
                username=User.username
                User=JSON.stringify(User)

                res.write(User)
                res.end()
            }else{
                res.end("false")
            }
            
        }
    })
}
function logon(data,res){
    let temp={
        username:data.username
    }
    user.find(temp,(err,ret)=>{
        if (err) {
            console.log("查找err")
        } else {
            if(ret.length==0){

                let User=new user(data)
                User.save((err,ret)=>{
                    if (err) {
                        console.log("注册err")
                    } else {
                        console.log(ret)
                        res.write("true")
                        res.end()
                    }
                })
            }
            else{
                res.end("false")
            }
        }
    })
}
function del_user(data,res){
    user.findOneAndRemove(data,(err,ret)=>{
        if(err){
            console.log("err")
        }else{
            res.end()
        }
    })
}
function update_user(data,res){
    user.findOneAndUpdate(data[0],data[1],(err,ret)=>{
        if(err){
            console.log("err")
        }else{
            res.end()
        }
    })
}
function get_users(data,res){
    if(data===null){
        user.find((err,ret)=>{
            if(err){
                console.log("err")
            }else{
                let data = []
    
                for (let i = 0, length = ret.length; i < length; i++) {
                    let item = ret[i]
                    data.push({
                        'username': item.username,
                        'passward': item.passward,
                        'vip':item.vip
                    })
                }
                console.log(data)
                data=JSON.stringify(data)
                res.write(data)
                res.end()
            }
        })
    }else{
        let reg = new RegExp(data['name'], 'g')
        user.find({"name":reg},(err,ret)=>{
            if(err){
                console.log("err")
            }else{
                let data = []
                for (let i = 0, length = ret.length; i < length; i++) {
                    let item = ret[i]
                    data.push({
                        'username': item.username,
                        'passward': item.passward,
                        'vip':item.vip
                    })
                }
                console.log(data)
                data=JSON.stringify(data)
                res.write(data)
                res.end()
            }
        })
    }
}
function add_dish(data,res){
    let temp={
        name:data.name
    }

    dish.find(temp,(err,ret)=>{
        if (err) {
            console.log("查找err")
        } else {
            console.log(ret)
            if(ret.length==0){
                data.manager=true
                let Dish=new dish(data)
                Dish.save((err,ret)=>{
                    if (err) {
                        console.log("添加err")
                    } else {
                        // console.log(ret)
                        res.write("true")
                        res.end()
                    }
                })
            }
            else{
                res.end("false")
            }
        }
    })
}
function get_dishes(data,res){
    if(data===null){
        dish.find((err,ret)=>{
            if(err){
                console.log("err")
            }else{
                let data = []
    
                for (let i = 0, length = ret.length; i < length; i++) {
                    let item = ret[i]
                    data.push({
                        'name': item.name,
                        'cost': item.cost
                    })
                }
                console.log(data)
                data=JSON.stringify(data)
                res.write(data)
                res.end()
            }
        })
    }else{
        let reg = new RegExp(data['name'], 'g')
        dish.find({"name":reg},(err,ret)=>{
            if(err){
                console.log("err")
            }else{
                let data = []
                for (let i = 0, length = ret.length; i < length; i++) {
                    let item = ret[i]
                    data.push({
                        'name': item.name,
                        'cost': item.cost
                    })
                }
                console.log(data)
                data=JSON.stringify(data)
                res.write(data)
                res.end()
            }
        })
    }
    
}
function update_dish(datas,res){

    dish.findOneAndUpdate(datas[0],datas[1],(err,ret)=>{
        if(err){
            console.log("err")
        }else{
                
                let data=JSON.stringify(datas[1])
                res.end(data)      
        }
    })
    
}
function del_dish(data,res){
    dish.findOneAndRemove(data,(err,ret)=>{
        if(err){
            console.log("err")
        }else{
            res.end()
        }
    })
}
function save_order(data,res){
    let data_={
        "username":username,
        "dishes":data.dishes,
        "date":data.date
    }

    let Order=new orders(data_)
    Order.save((err,ret)=>{
        if(err){
            console.log("err")
        }else{
            res.end()
        }
    })
}
function get_orders(data,res){
    let temp={"username":username}
    orders.find(temp,(err,ret)=>{
        console.log(username)
        console.log(ret)
        if(err){
            console.log("err")
        }else{
            let data = []
            for (const item of ret) {
                data.push({
                    "date":item.date,
                    "dishes":item.dishes
                })
            }
            console.log(data)
            data=JSON.stringify(data)
            res.end(data)
        }
    })
}