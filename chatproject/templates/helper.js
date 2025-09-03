function getCookie(name) {
        return document.cookie
                .split('; ')
                .find(cookie => cookie.startsWith(name + '='))
                ?.split('=')[1] || null;
        }

async function checkLoginStatus() {
            try {
                const response = await fetch('http://127.0.0.1:8000/checklogin/', {
                   credentials: "include"

                })
                const data = await response.json();
                console.log(data);
                if (!data.Logged_In) {
                    
                    window.location.href='login.html';
                }
            } catch (error) {
                return ({"Error": "there is error in code", error});
            }

        }
checkLoginStatus();
                    

                 