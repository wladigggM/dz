//log-sign
console.log('Script loaded');

let logIn = document.querySelector(".log-in");
let logArea = document.querySelector(".log-in-area");
let logBlock = document.querySelector(".log-in-block");
let signIn = document.querySelector(".sign-in");
let signArea = document.querySelector(".sign-in-area");
let signBlock = document.querySelector(".sign-in-block");
let isOpen = false;

document.addEventListener("DOMContentLoaded", function() {
  logIn.addEventListener("click", function () {
    let logForm = document.querySelector(".log-in-form");
    if (!isOpen) {
      isOpen = true;
      console.log(logArea);
      logArea.addEventListener("click", function (el) {
        if (el.target == logArea && el.target != logBlock) {
          exitLogIn();
        }
      });
      if (logArea.classList.contains("hidden")) {
        logArea.classList.remove("hidden");
        setTimeout(() => {
          logBlock.setAttribute("style", "top: 150px");
          logArea.style.backgroundColor = "rgba(0,0,0,0.5)";
        }, 100);
      } else {
        exitLogIn();
      }
    }
  });

  signIn.addEventListener("click", function () {
    let signForm = document.querySelector(".sign-in-form");
    if (!isOpen) {
      isOpen = true;
      signArea.addEventListener("click", function (el) {
        if (el.target == signArea && el.target != signBlock) {
          exitSignIn();
        }
      });
      if (signArea.classList.contains("hidden")) {
        signArea.classList.remove("hidden");
        setTimeout(() => {
          signBlock.setAttribute("style", "top: 100px");
          signArea.style.backgroundColor = "rgba(0,0,0,0.5)";
        }, 100);
      } else {
        exitSignIn();
      }
    }
  });

  function exitLogIn() {
    logBlock.setAttribute("style", "top: -400px");
    setTimeout(() => {
      logArea.style.backgroundColor = "transparent";
    }, 100);
    setTimeout(() => {
      logArea.classList.add("hidden");
    }, 200);
    isOpen = false;
  }

  function exitSignIn() {
    signBlock.setAttribute("style", "top: -400px");
    setTimeout(() => {
      signArea.style.backgroundColor = "transparent";
    }, 100);
    setTimeout(() => {
      signArea.classList.add("hidden");
    }, 200);
    isOpen = false;
  }
});