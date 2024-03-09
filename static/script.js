function analyze_title() {
    // TODO: suck out the input
    const inputValue = document.getElementById('title-to-analyze').value;
    
    fetch('/analyze', {
        method: 'POST',
        body: inputValue
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        const result = data.result;
        document.getElementById('output').textContent = result;
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error); 
    });

}


const button = document.getElementById('my-button');
button.addEventListener('click', analyze_title);