/*jshint esversion: 6 */

"use strict";


const dropArea= document.getElementById("drop-area");
const inputFile = document.getElementById("inputfile");
const imageView = document.getElementById("img-view");


inputFile.addEventListener("change", uploadImage);
function uploadImage() {
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    imageView.style.backgroundImage = `url(${imgLink})`;
    imageView.textContent = "";
    imageView.style.border = 0;
}

dropArea.addEventListener("dragover", function(e) {
    e.preventDefault();
});
dropArea.addEventListener("drop", function(e) {
    e.preventDefault();
    inputFile.files[0] = e.dataTransfer.files;
    uploadImage();
});


