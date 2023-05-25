function showCode(){
    code_block = document.getElementById("code")
    display = code_block.style.display
    if (display == "none"){display="block"}
    else{display="none"}
    code_block.style.display = display; 
}