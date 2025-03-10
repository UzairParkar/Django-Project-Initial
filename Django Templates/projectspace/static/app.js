
function changeText(){
    let message = document.getElementById("message");
if (message.innerText === "") {
    message.innerText = "You clicked the button!";
} else {
    message.innerText = "";
}
}
