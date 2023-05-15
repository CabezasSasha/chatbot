$(document).ready(function() {
    $("#send-btn").click(function() {
        sendMessage();
    });

    $('#user-input').keypress(function(event) {
        if (event.keyCode === 13) {
            sendMessage();
        }
    });

    function sendMessage() {
        var userInput = $('#user-input').val();
        $('#user-input').val('');
        $('#chat-log').append('<div class="chat-bubble user-bubble">' + userInput + '</div>');
        $.ajax({
            url: '/get',
            type: 'GET',
            data: {msg: userInput},
            success: function(response) {
                $('#chat-log').append('<div class="chat-bubble bot-bubble">' + response + '</div>');
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
});