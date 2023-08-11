function handleLogin() {
  // 로그인 버튼 클릭 시 실행되는 로직
  // 로그인 처리 구현
}


// 비밀번호 보기 옵션
function togglePasswordVisibility() {
    var passwordField = document.getElementById("passwordField");
    var toggleImage1 = document.querySelector(".toggle-image1");
    
    if (passwordField.type === "password") {
      passwordField.type = "text";
      toggleImage1.src = "/public/images/pwd-toggle-hide.svg";
    } else {
      passwordField.type = "password";
      toggleImage1.src = "/public/images/pwd-toggle-show.svg";
    }
  }
  
function togglePasswordCheckVisibility() {
  var passwordCkField = document.getElementById("passwordCkField");
  var toggleImage2 = document.querySelector(".toggle-image2");
  
  if (passwordCkField.type === "password") {
    passwordCkField.type = "text";
    toggleImage2.src = "/public/images/pwd-toggle-hide.svg";
  } else {
    passwordCkField.type = "password";
    toggleImage2.src = "/public/images/pwd-toggle-show.svg";
  }
}