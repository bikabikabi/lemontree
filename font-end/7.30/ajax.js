let sendAjax=(url)=> {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'json';
        xhr.open('get', url,true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status >= 200 && xhr.status < 300) {
                    resolve(xhr.response);
                } else {
                    reject(xhr.status);
                }
            }
        }
        xhr.send(); 
    })
}
async function fun(url){
    let value= await sendAjax(url)
    console.log("渲染")
    Render(value)
        

}
function Render(value){
    console.log(value)
}
fun('http://music.eleuu.com/personalized')