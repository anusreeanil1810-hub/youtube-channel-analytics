const input = document.getElementById("channel");
const suggestions = document.getElementById("suggestions");

function loadSuggestions(value=""){

    fetch("/suggest?q="+value)

    .then(response=>response.json())

    .then(data=>{

        suggestions.innerHTML="";

        if(data.length===0){

            suggestions.style.display="none";
            return;

        }

        suggestions.style.display="block";

        data.forEach(name=>{

            const div=document.createElement("div");

            div.className="suggestion-item";

            div.innerText=name;

            div.onclick=function(){

                input.value=name;
                suggestions.style.display="none";

            }

            suggestions.appendChild(div);

        });

    });

}

input.addEventListener("focus",function(){

    loadSuggestions("");

});

input.addEventListener("input",function(){

    loadSuggestions(input.value);

});

document.addEventListener("click",function(e){

    if(!suggestions.contains(e.target) && e.target!=input){

        suggestions.style.display="none";

    }

});