function validate(e){
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('Password').value;
    const age = document.getElementById('age').value;
    const msgBox = document.getElementById('message');

    let message = '';
    if(email === ''){
        message = 'Please enter an email.';
        msgBox.style.color = 'red';
    } else if(password === ''){
        message = 'Please enter a password.';
        msgBox.style.color = 'red';
    } else if(age === ''){
        message = 'Please enter your age.';
        msgBox.style.color = 'red';
    } else {
        message='Login successful';
        msgBox.style.color = 'green';
    }
    msgBox.innerHTML = message;
}   
// Run validate when Login is clicked
document.getElementById("loginForm").onsubmit = validate;

//real-time validation (like screenshots)
document.getElementById("email").oninput = () => validate({preventDefault: () => {} });
document.getElementById("Password").oninput = () => validate({preventDefault: () => {} });
document.getElementById("age").oninput = () => validate({preventDefault: () => {} });
