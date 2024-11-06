document.getElementById("order_form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
    
    // Get form data
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    // Save data to localStorage
    localStorage.setItem("talanku-formData", JSON.stringify({ name, email }));

    alert("Form data saved!");
});

// Optional: Load data from localStorage when the page loads
window.addEventListener("load", function() {
    const savedData = JSON.parse(localStorage.getItem("talanku-formData"));
    if (savedData) {
        console.log(savedData);
        document.getElementById("name").value = savedData.name;
        document.getElementById("email").value = savedData.email;
    }
    else{
        console.log("No Saved Data Was Found");
    }
});
