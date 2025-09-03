async function LoadUsers() {
    try {
        const response = await fetch('http://127.0.0.1:8000/getalluser', {
            credentials: "include"
        });
        if (!response.ok) {
            alert("failed to fetch users");
            return;
        }

        const data = await response.json();
        let html = "";
        data.forEach(user => {
            html += `<p style="cursor: pointer; color:zinc;" onclick="createroom(${user.id})">${user.username}</p>`;

             });
        document.getElementById('users').innerHTML = html;
        
        } catch (error) {
    }
}

async function createroom(UserId) {
        const csrftoken =await getCookie('csrftoken');
        const response = await fetch('http://127.0.0.1:8000/createroom/', {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken// Uses helper.js
            },

            body: JSON.stringify({
                "user_id": UserId
       })
    });
             

        const data = await response.json();
        console.log(data.rooom)
        localStorage.setItem('room_id', JSON.stringify(data.room.id));
        window.location.href = "message.html";
}


LoadUsers()

