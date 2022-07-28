function alldiy(list){
    let length=list.length
    let results=[]
    let count=0
    let p=new Promise((resolve, reject) => {
        for(let i =0;i<length;i++){
            Promise.resolve(list[i]).then(res=>{
                let index=i
                count+=1
                results[index]=res
                if(count===length){
                    resolve(results)
                }
            },reason=>{
                reject(reason)
            })
        }
    })
    p.catch(e=>{})
    return p
}
let p1 = Promise.resolve("abc")
let p2 = Promise.reject('Success');
let p3 = Promise.resolve('Oh Yeah');
const result1=alldiy([p1,p2,p3])
setTimeout(function(){
    console.log(result1)
},2000)