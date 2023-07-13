document.addEventListener("DOMContentLoaded", () => {
const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const fistForm = document.getElementById("form1");
const secondForm = document.getElementById("form2");
const container_login = document.querySelector(".container_login");

signInBtn.addEventListener("click", () => {
  container_login.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
  container_login.classList.add("right-panel-active");
});

fistForm.addEventListener("submit", (e) => e.preventDefault());
secondForm.addEventListener("submit", (e) => e.preventDefault());
});

//로그인 끝


$(function(){
  $(document).one('click', '.like-review', function(e) {
    $(this).html('<i class="fa fa-heart" aria-hidden="true"></i> You liked this');
    $(this).children('.fa-heart').addClass('animate-like');
  });
});