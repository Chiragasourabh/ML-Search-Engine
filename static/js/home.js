function validate() {
    var x = document.forms["searchForm"]["search"].value;
    if (x == "") {
        alert("Search Something...");
        return false;
    }
}

function record(){
  var x = document.forms["searchForm"]["search"].value;
  if (x == "") {
  alert("Search Something...");
}
}
