function clickMe()
{
    var Gmail = document.getElementById("email");
    var Passwords = document.getElementById("password");

    if(Gmail.value == "")
    {
        alert("Please enter your email address");
    }
    if(Passwords.value == "")
    {
        alert("Please enter your password");
    }
    else
    {
        alert("Login Successful");
    }
}