function setFormMessage(formElement, type, message) {
    const messageElement = formElement.querySelector(".form__message");

    messageElement.textContent = message;
    messageElement.classList.remove("form__message--success", "form__message--error");
    messageElement.classList.add(`form__message--${type}`);
}

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");

    loginForm.addEventListener("submit", evt => {
        evt.preventDefault();

        setFormMessage(loginForm, "error", "Invalid username/password combination.");
    });

    let submitLogin = document.getElementById('submitLogin')
    let url = new URL('https://')
    let params = new URLSearchParams(url.search.slice(1))

    submitLogin.onclick = function (click) {
        params.append("email", "email from form")
    }


})
