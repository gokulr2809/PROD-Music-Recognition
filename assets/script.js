function recbutton(){
    document.getElementById("rec").onclick="null";
    document.getElementById("img").src="{% static '3.gif' %}" ;
    document.getElementById("click").textContent="RECORDING...";
    let a = document.querySelector("#close");
    a.style.visibility='visible';
    }
    function closen()
    {
    document.getElementById("rec").onclick="recbutton()";
    let a = document.querySelector("#close");
    a.style.visibility='hidden';
    document.getElementById("img").src="{% static '2.png' %}";
    document.getElementById("click").textContent="CLICK TO SEARCH !";
    }
