document.addEventListener("DOMContentLoaded", function () {
  const formContainer = document.querySelector(".form-container");
  const registerLink = document.querySelector(".register-link");
  const loginLink = document.querySelector(".login-link");

  registerLink.addEventListener("click", function (event) {
    event.preventDefault();
    formContainer.classList.add("show-register");
    formContainer.classList.remove("show-login");
  });

  loginLink.addEventListener("click", function (event) {
    event.preventDefault();
    formContainer.classList.remove("show-register");
    formContainer.classList.add("show-login");
  });
});
