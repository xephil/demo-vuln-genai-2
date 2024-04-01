function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    // Show progress bar
    document.getElementById('progress-bar').style.display = 'block';
    document.getElementById('progress').style.width = '100%'; // Simulate a progress completion
    
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({message: userInput}),
    })
    .then(response => response.json())
    .then(data => {
        // Access the output from data.response.output
        document.getElementById('chat-box').innerHTML += `<div>You: ${userInput}</div><div>AI: ${data.response.output}</div>`;
        // Instead of clearing the input box, you might want to keep the question
        // document.getElementById('user-input').value = ''; // To clear input box, uncomment if needed

        // Hide progress bar
        document.getElementById('progress-bar').style.display = 'none';
        document.getElementById('progress').style.width = '0%'; // Reset progress
    })
    .catch((error) => {
        console.error('Error:', error);
        // Hide progress bar in case of error as well
        document.getElementById('progress-bar').style.display = 'none';
        document.getElementById('progress').style.width = '0%'; // Reset progress
    });
}