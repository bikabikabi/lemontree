function login(){
    let inputs=document.getElementsByTagName("input")
    let data={
        "username":inputs[0].value,
        "passward":inputs[1].value
    }
    post(data,"login").then(res=>{
        console.log(res)
        if(res!="false"){
            let data=JSON.parse(res)
            if(data.manager==true){

                window.location.href="manage.html";
            }else{

                window.location.href="order.html";
                
            }
                    
        }else{

        }

    })
}
