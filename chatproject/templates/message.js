checkLoginStatus()

const room_id=localStorage.getItem('room_id');
if (!room_id){
    alert("No Room Is Selected");
    window.location.href='index.html';

}
async function LoadMessages() {
    try {

        const response = await fetch(`http://127.0.0.1:8000/getmessage/${room_id}`, {
            credentials: "include"
        });
        if (!response.ok) return;
        const data = await response.json()
        let html = "";
        data.forEach(message => {
            html += `<p><b>${message.sender_username}:</b> ${message.text}</p>`;
        });
        document.getElementById('message').innerHTML = html;
    } catch (error) {

    }
}
setInterval(LoadMessages, 2000)

