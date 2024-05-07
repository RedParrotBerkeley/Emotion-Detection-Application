// static/mywebscript.js

function analyzeEmotion() {
    // Get the input statement
    let statement = document.getElementById("statement").value;

    // Create a new FormData object for the form submission
    let formData = new FormData();
    formData.append("statement", statement);

    // Perform an AJAX request to the Flask endpoint
    fetch('/emotionDetector', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display the result message
        let resultDiv = document.getElementById("result");
        resultDiv.innerHTML = `<p>${data.message}</p>`;
    })
    .catch(error => console.error('Error:', error));
}
