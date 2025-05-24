document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.signup-form');
    const password1 = document.getElementById('password1');
    const password2 = document.getElementById('password2');

    const errorMsg = document.createElement('p');
    errorMsg.style.color = 'red';
    errorMsg.style.fontSize = '0.9rem';
    errorMsg.style.marginTop = '-10px';
    errorMsg.style.display = 'none';
    password2.parentNode.insertBefore(errorMsg, password2.nextSibling);

    form.addEventListener('submit', function (e) {
        if (password1.value !== password2.value) {
            e.preventDefault();  // Stop form from submitting
            errorMsg.textContent = 'Passwords do not match!';
            errorMsg.style.display = 'block';
            password2.style.borderColor = 'red';
        } else {
            errorMsg.style.display = 'none';
            password2.style.borderColor = '#ccc';  // Reset if valid
        }
    });
});
