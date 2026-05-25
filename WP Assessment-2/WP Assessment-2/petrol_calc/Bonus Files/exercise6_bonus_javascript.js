var colours = [
    "rgb(255, 0, 0)",
    "rgb(0, 255, 0)",
    "rgb(0, 0, 255)",
]

var colour_squares = document.querySelectorAll(".colour");

for(var i=0 ; i<colour_squares.length ; i++){
    colours_squares[i].style.backgroundColor = colours[i];
}