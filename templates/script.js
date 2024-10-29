// static/app.js
async function analyzeRepo() {
    const githubUrl = document.getElementById("github-url").value;
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Analyzing...";

    try {
        const response = await fetch(`/analyze?github_url=${encodeURIComponent(githubUrl)}`);
        if (!response.ok) {
            throw new Error("Error analyzing repository");
        }
        const data = await response.json();
        resultDiv.innerHTML = `
            <h3>Most Complex Repository:</h3>
            <p><strong>Name:</strong> ${data.most_complex_repo.name}</p>
            <p><strong>Complexity Score:</strong> ${data.most_complex_repo.complexity_score}</p>
            <p><strong>Description:</strong> ${data.most_complex_repo.description}</p>
        `;
    } catch (error) {
        resultDiv.innerHTML = `Error: ${error.message}`;
    }
}
