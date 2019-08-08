function myFunction() {
  // var element = document.getElementById("myDIV");
  // element.classList.remove("mystyle");

  var element = document.getElementById("btn-myBtn")
  if(element.classList.contains("btn-upsidedown")){
    element.classList.remove("btn-upsidedown");
  }
  else {
    element.classList.add("btn-upsidedown");
  }

}
