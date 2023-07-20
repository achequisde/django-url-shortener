const url = document.getElementById('url-container');

document.querySelector('button').addEventListener("click", async () => {
    const urlText = url.textContent;

    try {
        await navigator.clipboard.writeText(urlText);
    } catch (err) {
        console.error(`Couldn't copy text to clipboard: ${err}`);
    }
}, []);