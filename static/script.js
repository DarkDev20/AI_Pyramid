document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("triangle-form").addEventListener("submit", async function (event) {
        event.preventDefault();

        let numRows = document.getElementById("numRows").value;
        let output = document.getElementById("triangle-output");

        if (!numRows || numRows < 1) {
            output.textContent = "Please enter a valid number of rows.";
            return;
        }

        try {
            let response = await fetch("/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ numRows: parseInt(numRows) }),
            });

            let data = await response.json();
            if (data.triangle) {
                output.textContent = data.triangle;
            } else {
                output.textContent = "Error: " + data.error;
            }
        } catch (error) {
            output.textContent = "Failed to generate triangle.";
        }
    });
});
