/**
 * @param {any} inputElement The input element that need to set as error.
 * @param {string} message Text about error information.
 */
function setInputError(inputElement, message) {
    console.log('inputElement:', inputElement);
    inputElement.classList.add("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = message;
}

/**
 * @param {Element} inputElement The input element that need to clear error.
 */
function clearInputError(inputElement) {
    inputElement.classList.remove("form__input--error");
    inputElement.parentElement.querySelector(".form__input-error-message").textContent = "";
}

document.addEventListener("DOMContentLoaded", () => {

    const accountInfo = document.querySelector("#accountInfo")
    const moreInfo = document.querySelector("#moreInfo")

    document.querySelectorAll(".form__input").forEach(inputElement => {

         document.querySelector("#nextToMoreInfo").addEventListener("click", e => {
        e.preventDefault();
        accountInfo.classList.add("form--hidden");
        moreInfo.classList.remove("form--hidden");
    });

    document.querySelector("#backToSignup").addEventListener("click", e => {
        e.preventDefault();
        accountInfo.classList.remove("form--hidden");
        moreInfo.classList.add("form--hidden");
    });

        inputElement.addEventListener("blur", evt => {
            if (evt.target.id === "username" && evt.target.value.length > 0 && evt.target.value.length < 10) {
                console.log('inputElement', inputElement);
                setInputError(inputElement, "Username must be at least 10 characters in length");
            }
            if (evt.target.id === "email" && /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(evt.value)) {
                console.log("inputElement", inputElement);
                console.log("evt", evt);
                setInputError(inputElement, "You have entered an invalid email address!");
            }
        });

        inputElement.addEventListener("input", () => {
            clearInputError(inputElement);
        })
    });
})
