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

function signupData(email, firstname, surname, password, job, bloodType, sn) {
    let result;
    fetch('http://158.108.182.10:3000/signup_post', {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            email: email,
            firstname: firstname,
            surname: surname,
            password: password,
            job: job,
            bloodType: bloodType,
            sn: sn
        }),
    })
        .then((response) => response.json())
        .then(value => {
            result = value.result
        })
        .catch(reason => console.log("error", reason));
    return result;
}

document.addEventListener("DOMContentLoaded", () => {

    const createAccountForm = document.querySelector("#createAccount")
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

    createAccountForm.addEventListener("submit", evt => {
        evt.preventDefault();
        let email = document.getElementById("email").value;
        let firstname = document.getElementById("firstname").value;
        let surname = document.getElementById("surname").value;
        let password = document.getElementById("password1").value;
        let bloodType = document.getElementById("blood type").value;
        let job = document.getElementById("jobs").value;
        let sn = document.getElementById("cyberWareSN").value;
        signupData(email, firstname, surname, password, job, bloodType, sn);
        document.getElementById("email").value = "";
        document.getElementById("firstname").value = "";
        document.getElementById("surname").value = "";
        document.getElementById("password1").value = "";
        document.getElementById("password2").value = "";
        document.getElementById("blood type").value = "";
        document.getElementById("jobs").value = "";
        document.getElementById("cyberWareSN").value = "";

        window.location.href = "../templates/login.html";
    })
})
