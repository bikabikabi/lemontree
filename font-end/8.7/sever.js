const http = require("http")
// const Massage=require('./pool')
const mongoose = require("mongoose");
const Schema = mongoose.Schema;

mongoose.connect("mongodb://localhost:27017/memorandum");
var massageschema = new Schema({
    title: {
        type: String,
        require: true
    },
    content: {
        type: String,

    }
});
var Massage = mongoose.model("massage", massageschema)
const sever = http.createServer((req, res) => {
    res.writeHead(200, {
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Origin': 'null',
        'Access-Control-Allow-Headers': 'Content-type',
        'Content-type': 'application/json;charset=UTF-8'
    })

    let url = req.url
    console.log(url)
    if (url === '/add') {
        let data = ''
        req.on('data', (chunk) => {
            data += chunk.toString()
        })
        req.on('end', () => {
            if (data != '') {
                console.log(data)
                res.write(data)
                save(data)
            }
            res.end()
        })
    }
    else if (url === '/delete') {
        let data = ''
        req.on('data', (chunk) => {
            data += chunk.toString()
        })
        req.on('end', () => {
            if (data != '') {
                console.log(data)

                del(data)
            }
            res.end()
        })
    }
    else if (url === '/modify') {
        let data = ''
        req.on('data', (chunk) => {
            data += chunk.toString()
            console.log(data)
        })
        req.on('end', () => {
            if (data != '') {
                modify(data)
            }
            res.end()
        })
    }
    else if (url === '/getall') {
        let data = ''
        req.on('data', (chunk) => {
            data += chunk.toString()

        })
        req.on('end', () => {

            if (data != '') {
                console.log(data)
                find(null,res = res)
            }else{
                res.end()
            }

        })
    }
    else if (url === '/find') {
        let data = ''
        req.on('data', (chunk) => {
            data += chunk.toString()
        })
        req.on('end', () => {
            if (data != '') {
                find(data, res)

            } else {
                res.end()
            }

        })
    }

})
sever.listen(3000)
// 保存
function save(data) {
    data = JSON.parse(data)

    let massage = new Massage(data)
    massage.save((err, ret) => {
        if (err) {
            console.log("保存err")
        } else {
            console.log('保存ok')
            console.log(ret)
        }
    })
}
// 查询
function find(data = null, res) {

    if (data === null) {
        Massage.find((err, ret) => {
            if (err) {
                console.log("查找err")
            } else {
                console.log(ret)
                let data = []
                for (let i = 0, length = ret.length; i < length; i++) {
                    let item = ret[i]
                    console.log(item.title)
                    data.push({
                        'title': item.title,
                        'content': item.content
                    })
                }
                data = JSON.stringify(data)
                console.log(data)
                res.write(data)
                res.end()
            }
        })
    } else {
        data = JSON.parse(data)

        let reg = new RegExp(data['data'], 'g')


        Massage.find({ $or: [{ 'title': reg }, { 'content': reg }] }, 'title date content', (err, ret) => {
            if (err) {
                console.log("查找err")
            } else {
                let data = []
                for (let i = 0, length = ret.length; i < length; i++) {
                    let item = ret[i]

                    data.push({
                        'title': item.title,
                        'content': item.content
                    })
                }
                data = JSON.stringify(data)
                console.log(data)
                res.write(data)
                res.end()
            }
        })

    }
}
// 删除
function del(data) {
    Massage.findOneAndRemove(data, (err, ret) => {
        if (err) {
            console.log("删除err")
        } else {
            console.log('删除成功')
            console.log(ret)
        }
    })
}
// 更新
function modify(content) {
    content=JSON.parse(content)
    let data =content[0]
    let newdata=content[1]
    console.log(data,newdata)
    Massage.findOneAndUpdate(data, newdata, (err, ret) => {
        if (err) {
            console.log("更新err")
        } else {
            console.log('更新成功')
            console.log(ret)
        }
    })
}