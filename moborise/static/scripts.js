var modal = document.getElementById("myModal");

var modall = document.getElementById("myModallll");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

var btnn = document.getElementById("myBtnn");


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];





btn.onclick = function() {
    modal.style.display = "block";
}

btnn.onclick = function() {
    modall.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

span.onclick = function() {
    modall.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

window.onclick = function(event) {
    if (event.target == modall) {
        modall.style.display = "none";
    }
}

// function openPage(pageName, elmnt, color) {
//   // Hide all elements with class="tabcontent" by default */
//   var i, tablinks;

//   // Remove the background color of all tablinks/buttons
//   tablinks = document.getElementsByClassName("side-item");




//   for (i = 0; i < tablinks.length; i++) {
//     tablinks[i].style.backgroundColor = "";
//   }

//   // Show the specific tab content
//   // Add the specific color to the button used to open the tab content
//   elmnt.style.backgroundColor = color;
// }

// defaultt = document.getElementById("defaultOpen");

// defaultt.click(),style.backgroundColor = "green";