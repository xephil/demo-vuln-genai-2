function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    
    // Check if userInput is not empty to avoid sending empty messages
    if (!userInput.trim()) {
        return; // Prevents sending empty messages
    }

    // Append user input to chat box immediately
    const chatBox = document.getElementById('chat-box');
    const userDiv = document.createElement('div');
    userDiv.innerHTML = `You: ${userInput}`;
    chatBox.appendChild(userDiv);

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
        // Append AI response to chat box
        aiDiv = document.createElement('div');
        aiDiv.innerHTML = `AI: ${data.response.output}`;
        chatBox.appendChild(aiDiv);

        // Clear the input box
        document.getElementById('user-input').value = '';

        // Scroll to the latest message
        aiDiv.scrollIntoView({ behavior: 'smooth' });

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
