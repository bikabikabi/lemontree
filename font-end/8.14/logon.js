function logon(){
    let inputs=document.getElementsByTagName("input")
    let data={
        "username":inputs[0].value,
        "passward":inputs[1].value,
        "manager":inputs[2].checked
    }
    post(data,"logon").then(res=>{
        console.log(typeof(res))
        if(res==="true"){
            window.location.href="login.html";
        }else{

        }
        
    })
}