$(function () {
    $("#alert-success").hide();
    $("#alert-danger").hide();
    $("input").keyup(function () {
        var pwd1 = $("#passwordField").val();
        var pwd2 = $("#passwordCkField").val();
        if (pwd1 == pwd2) {
            $("#alert-success").show();
            $("#alert-danger").hide();
            $("#passwordField").css("border", "2px solid #CECECE");
            $("#passwordCkField").css("border", "2px solid #CECECE");
        } else {
            $("#alert-success").hide();
            $("#alert-danger").show();
            $("#passwordField").css("border", "2px solid #FF3F3F");
            $("#passwordCkField").css("border", "2px solid #FF3F3F");
        }
    });
});