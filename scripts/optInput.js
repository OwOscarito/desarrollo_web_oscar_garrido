function updateInput(element){
    if (element.checked) {
      document.getElementById(element.name).style.display = "block";
    } else {
       document.getElementById(element.name).style.display = "none";
    }
}
    