document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Gather form data
        const formData = new FormData(form);

        // Send the data to the server using Fetch API
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }
            return response.json();
        })
        .then(result => {
            if (result.prediction) {
                resultDiv.innerHTML = `Suggested Sport: ${result.prediction}`;
            } else if (result.error) {
                resultDiv.innerHTML = `Error: ${result.error}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = 'An error occurred while predicting the sport.';
        });
    });
});
