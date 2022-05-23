let logJson;

async function sendMessage(event) {
    event.preventDefault();
    let fd = new FormData();
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let date = new Date();

    let month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let days = ('0' + date.getDate()).slice(-2);
    let year = date.getFullYear().toString();

    let dateString = month[date.getMonth()] + "  " + days + ',' + " " + year;

    fd.append('textmessage', messageField.value);
    fd.append('csrfmiddlewaretoken', token);
    try {
        messageContainer.innerHTML += `<div class="chat-section" id="deleteMessage">
        <span class="color-gray">${dateString}</span> {{ request.user.first_name }}: <i class="color-gray">${messageField.value}</i>
        </div>`;

        let response = await fetch('', {
            method: 'POST',
            body: fd
        });

        let json = await response.json();
        let obj = JSON.parse(json);
        console.log('json is:', obj.fields);


        document.getElementById('deleteMessage').remove();
        messageContainer.innerHTML += `<div class="chat-section">
        <span class="color-black">${dateString}</span> {{ request.user.first_name }}: <i>${obj.fields.text}</i>
        </div>`;
        location.reload();
    } catch (e) {
        messageContainer.innerHTML += `<div class="chat color-red">
            <span class="color-red">${dateString}</span> {{ request.user.first_name }}: <i class="color-gray">${messageField.value}</i>
            </div>`;
    }
}

async function userRegister() {
    /* let fd = new FormData();

    fd.append('username', userName.value);
    fd.append('first_name', firstName.value);
    fd.append('last_name', lastName.value);
    fd.append('email', eMail.value);

    try {
        let response = await fetch('/register/', {
            method: 'POST',
            body: fd
        });

        let userjson = await response.json();
        JSON.parse(json);
        console.log('json is:', userjson);
    } catch (e) {
        console.log(e);
    } */
}

async function loginUser() {
    /* let fd = new FormData();
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fd.append('username', usernameJson.value);
    fd.append('csrfmiddlewaretoken', token);

    try {
        let response = await fetch('/login/', {
            method: 'POST',
            body: fd
        });

        let loginjson = await response.json();
        logJson = JSON.parse(loginjson);
        console.log('json is:', logJson);
    } catch (e) {
        console.log(e);
    } */
}