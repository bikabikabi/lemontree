const mongoose =require("mongoose")
const Schema =mongoose.Schema
mongoose.connect("mongodb://localhost:27017/order")
var user=new Schema({
    username:{
        type: String,
        required: true
    },
    passward:{
        type: String,
        required: true
    },
    manager:{
        type:Boolean,
        required:true
    }

})
var dish =new Schema({
    name:{
        type: String,
        required: true
    },
    cost:{
        type: String,
        required:true
    }
    
})
var order=new Schema({
    username:{
        type:String,
        required:true
    },
    dishes:{
        type:String,
        required:true
    },
    date:{
        type:String,
        required:true
    }
})
var user = mongoose.model("user", user)
var dish = mongoose.model("dish", dish)
var order=mongoose.model("order",order)
exports.user=user
exports.dish=dish
exports.order=order