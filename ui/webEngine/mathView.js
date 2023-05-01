function setEquation(text){
    document.body.innerHTML = text

    renderMathInElement(document.body, {

        delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false},
            {left: "\\(", right: "\\)", display: false},
            {left: "\\begin{equation}", right: "\\end{equation}", display: true},
            {left: "\\begin{align}", right: "\\end{align}", display: true},
            {left: "\\begin{alignat}", right: "\\end{alignat}", display: true},
            {left: "\\begin{gather}", right: "\\end{gather}", display: true},
            {left: "\\begin{CD}", right: "\\end{CD}", display: true},
            {left: "\\[", right: "\\]", display: true}
        ],
        throwOnError : false
    });
}

function setTextStyle(textColor, fontWeight, fontSize){
    document.body.style.color = textColor
    document.body.style.fontWeight = fontWeight
    document.body.style.fontSize = fontSize
}