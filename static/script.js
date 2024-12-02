document.querySelector("button").addEventListener("click", () => {
    const button = document.querySelector("button");
    button.textContent = "Planning...";
    setTimeout(() => {
        button.textContent = "Plan Event";
        alert("Event planning completed!");
    }, 2000);
});
