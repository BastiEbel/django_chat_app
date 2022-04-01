async function sendMessage() {
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
        messageContainer.innerHTML += `<div class="chat" id="deleteMessage">
        <span class="color-gray">${dateString}</span> {{ request.user.username }} <i class="color-gray">${messageField.value}</i>
        </div>`;

        let response = await fetch('', {
            method: 'POST',
            body: fd
        });

        let json = await response.json();
        let chatJson = JSON.parse(json);

        document.getElementById('deleteMessage').remove();
        messageContainer.innerHTML += `<div class="chat">
        <span class="color-gray">${chatJson.created_at}</span> {{ request.user.username }} <i>${chatJson.text}</i>
        </div>`;
    } catch (e) {
        console.log('an error occured', e);
    }
}