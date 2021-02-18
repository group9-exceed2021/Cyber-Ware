function setFormMessage(formElement, type, message) {
    const messageElement = formElement.querySelector(".form__message");

    messageElement.textContent = message;
    messageElement.classList.remove("form__message--success", "form__message--error");
    messageElement.classList.add(`form__message--${type}`);
}

function setInputError(formElement ,inputElement, message) {
    const messageElement = formElement.querySelector(`#${inputElement}.form__input`)

    messageElement.classList.add("form__input--error");
    messageElement.parentElement.querySelector(".form__input-error-message").textContent = message;
}

function clearInputError(inputElement) {
    inputElement.classList.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = "";
}

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");
    const createAccountForm = document.querySelector("#createAccount");

    loginForm.addEventListener("submit", evt => {
        evt.preventDefault();

        setFormMessage(loginForm, "error", "Invalid username/password combination.");
    });

    document.querySelectorAll(".form__input").forEach(inputElement => {
        inputElement.addEventListener("blur", evt => {
            if (evt.target.id === "signupUsername" && evt.target.value.length > 0 && evt.target.value.length < 10) {
                setInputError(createAccountForm, inputElement, "Username must be at least 10 characters in length");
            }
        });

        inputElement.addEventListener("input", () => {
            clearInputError(inputElement);
        })
    });
})
