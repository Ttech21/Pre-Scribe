function showHidePassword() {
    const passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      document.querySelector(".show-hide-icon").classList.remove("fa-eye-slash");
      document.querySelector(".show-hide-icon").classList.add("fa-eye");
    } else {
      passwordInput.type = "password";
      document.querySelector(".show-hide-icon").classList.remove("fa-eye");
      document.querySelector(".show-hide-icon").classList.add("fa-eye-slash");
    }
  }

  function showPassword() {
    const passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      document.querySelector(".show-hide-icon").classList.remove("fa-eye-slash");
      document.querySelector(".show-hide-icon").classList.add("fa-eye");
    } else {
      passwordInput.type = "password";
      document.querySelector(".show-hide-icon").classList.remove("fa-eye");
      document.querySelector(".show-hide-icon").classList.add("fa-eye-slash");
    }
  }