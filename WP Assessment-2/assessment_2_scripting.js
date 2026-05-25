function copy_function() {
    var copyText = document.getElementById("copy_number");

    copyText.select();
    copyText.setSelectionRange(0, 99999);

    navigator.clipboard.writeText(copyText.value);

    alert("Number has been copied!");
}