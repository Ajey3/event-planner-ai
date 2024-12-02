document.getElementById("plan-event-btn").addEventListener("click", function() {
    const userQuery = document.getElementById("event-query").value;  // Get input value

    if (userQuery.trim() === "") {  // If query is empty, alert the user
        alert("Please enter a query!");
        return;
    }

    // Change button text to show it's planning
    const button = document.getElementById("plan-event-btn");
    button.textContent = "Planning...";

    // Send the user query to the Flask backend
    fetch("/plan-event", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query: userQuery })  // Send the query in the body of the request
    })
    .then(response => response.json())  // Parse the JSON response from Flask
    .then(data => {
        // Update the UI with the response from the AI
        const eventResponse = data.response;
        document.getElementById("response").innerText = eventResponse;
        button.textContent = "Plan Event";  // Reset button text after response
    })
    .catch(error => {
        console.error("Error:", error);
        button.textContent = "Plan Event";  // Reset button text in case of error
    });
});
