document.getElementById('submitBtn').addEventListener('click', async () => {
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const FNcaseOption = document.getElementById('FNcaseOption').value;
    const LNcaseOption = document.getElementById('LNcaseOption').value;

    try {
        const response = await fetch('http://127.0.0.1:5000/process_name', {  // Note the full URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ firstName, lastName, FNcaseOption, LNcaseOption }),
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById('result').textContent =
                `First name: ${result.firstName}, Last name: ${result.lastName}, Total length: ${result.totalLength}`;
        } else {
            document.getElementById('result').textContent = "Error processing the Name.";
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
