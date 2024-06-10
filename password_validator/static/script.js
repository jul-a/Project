$(document).ready(function () {
    if ($('#register-content').is(':visible')) {
        $('#password-validator-content').hide();
    } else {
        $('#password-validator-content').show();
    }

    // Toggle content sections
    $('.menu-button').on('click', function () {
        var target = $(this).attr('id').replace('-button', '-content');
        $('.content').slideUp();
        $('#' + target).slideDown();
        clearMessages();
    });

    function clearMessages() {
        $('#email-messages').empty();
        $('#username-messages').empty();
        $('#password-messages').empty();
        $('#messages').empty();
    }

    // Real-time password validation
    $('#password').on('keyup', function (event) {
        var password = $('#password').val();
        $.ajax({
            url: '/validate_password',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ password: password }),
            success: function (response) {
                var messages = response.messages;
                var messagesDiv = $('#messages');
                messagesDiv.empty();
                if (messages.length === 0) {
                    messagesDiv.append('<p class="message-valid">Your password is valid!</p>');
                } else {
                    messages.forEach(function (message) {
                        messagesDiv.append('<p class="message-invalid">' + message + '</p>');
                    });
                }
            }
        });
    });

    // Toggle password visibility
    $('#toggle-password').on('change', function () {
        var passwordField = $('#password');
        var type = passwordField.attr('type') === 'password' ? 'text' : 'password';
        passwordField.attr('type', type);
    });

});
