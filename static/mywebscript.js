let RunSentimentAnalysis = () => {
    let textToAnalyze = encodeURIComponent(document.getElementById("textToAnalyze").value);

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            document.getElementById("system_response").innerHTML = response.response;
        }
    };
    xhttp.open("GET", `/emotionDetector?textToAnalyze=${textToAnalyze}`, true);
    xhttp.send();
};

