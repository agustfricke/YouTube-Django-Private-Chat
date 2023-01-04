
// Alerta 
let alert_close = document.querySelectorAll('.alert_close');
alert_close.forEach((x) => {
    x.addEventListener('click', () => x.parentElement.classList.add('hidden'))
})

console.log('JS works')

const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
);

socket.onopen = function (e) {
    console.log('CONNECTION OPEN')
};

socket.onclose = function (e) {
    console.log('CONNECTION CLOSE')
};

socket.onerror = function (e) {
    console.log('CONNECTION ERROR')
};


socket.onmessage = function (e) {
    
    const data =JSON.parse(e.data);

    if (data.username == message_username) {
        document.querySelector('#chat-body').innerHTML +=

        `<li class="flex justify-end">
            <div class="relative max-w-xl px-4 py-2 text-gray-700 bg-gray-100 rounded-lg">
                <span class="block">${data.message}</span>
            </div>
        </li>`

    } else {
        document.querySelector('#chat-body').innerHTML += 

        `<li class="flex justify-start">
            <div class="relative max-w-xl px-4 py-2 text-[#171c2d] bg-[#f9982f] rounded-lg">
                <span class="block">${data.message}</span>
            </div>
        </li>`

    }
}

document.querySelector('#chat-message-submit').onclick = function (e) {
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    socket.send(JSON.stringify({
        'message': message,
        'username': message_username,
    }));

    message_input.value = '';
}