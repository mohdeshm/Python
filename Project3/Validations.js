window.onload = function () {
    document.getElementById("fname").onblur =  function validateEmpty() {
        if(this.value == ""){
            document.getElementById("fnameError").innerHTML = "This field can't be empty";
        }else {
            document.getElementById("fnameError").innerHTML = " ";
        }
    };

    document.getElementById("cpassword").onblur =  function confirmPassword() {
        if(this.value != document.getElementById("password").value){
            document.getElementById("cpasswordError").innerHTML = "Password doesn't match.Try again?";
        }else {
            document.getElementById("cpasswordError").innerHTML = " ";
        }
    };

    document.getElementById("gender").onblur =  function confirmGender() {
        if(this.value == "iam"){
            document.getElementById("genderError").innerHTML = "This field can't be empty";
        }else {
            document.getElementById("genderError").innerHTML = " ";
        }
    };

    document.getElementById("pcode").onblur =  function confirmCode() {
        if(this.value == "select"){
            document.getElementById("numberError").innerHTML = "This field can't be empty";
        }else {
            document.getElementById("numberError").innerHTML = " ";
        }
    };

    document.getElementById("location").onblur =  function confirmLocation() {
        if(this.value == "select"){
            document.getElementById("locationError").innerHTML = "This field can't be empty";
        }else {
            document.getElementById("locationError").innerHTML = " ";
        }
    };

    document.getElementById("frm").onsubmit = function finalValidation(e){
        var flag=0;
        if( document.getElementById("gender").value=="iam"){
            document.getElementById("genderError").innerHTML = "This field can't be empty";
            flag=1;
        }else {
            document.getElementById("genderError").innerHTML = " ";
        }
        if(document.getElementById("pcode").value == "select"){
            document.getElementById("numberError").innerHTML = "This field can't be empty";
            flag=1;
        }else {
            document.getElementById("numberError").innerHTML = " ";
        }
        if(document.getElementById("location").value == "select"){
            document.getElementById("locationError").innerHTML = "This field can't be empty";
            flag=1;
        }else {
            document.getElementById("locationError").innerHTML = " ";
        }
        if(flag==1) {
            return false;
        }
        else{
            alert("Successfully signed up!")
            return true;
        }
    };
};

