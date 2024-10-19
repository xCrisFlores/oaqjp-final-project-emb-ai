let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                // Solo cambia el contenido si el estado es 200 (OK)
                document.getElementById("system_response").innerHTML = JSON.parse(this.responseText).response;
            } else {
                // Maneja el caso de error
                document.getElementById("system_response").innerHTML = JSON.parse(this.responseText).error || "An error occurred!";
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
