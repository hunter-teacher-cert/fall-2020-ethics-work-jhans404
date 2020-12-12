function changeCSS(cssFile, cssLinkIndex) {

    var oldlink = document.getElementsByTagName("link").item(cssLinkIndex);

    var newlink = document.createElement("link");
    newlink.setAttribute("rel", "stylesheet");
    newlink.setAttribute("type", "text/css");
    newlink.setAttribute("href", cssFile);

    document.getElementsByTagName("head").item(0).replaceChild(newlink, oldlink);
}

function showAnswer(id) {
    var index = id-1;
    var x = document.getElementsByClassName("ansDiv");
    if (x[index].style.display === "none") {
        x[index].style.display = "block";
    } else {
        x[index].style.display = "none";
    }
}

function showClue(id) {
    var index = id-1;
    var x = document.getElementsByClassName("clueDiv");
    if (x[index].style.display === "none") {
        x[index].style.display = "block";
    } else {
        x[index].style.display = "none";
    }
}
