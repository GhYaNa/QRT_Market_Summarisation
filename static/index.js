function userRequest(){
    // get input text from users, to feed to LM studio
    var lmInput = document.getElementById("User_text");

    // Get the value from the input element
    var text = lmInput.value;

    // API end point for Python
    document.addEventListener('DOMContentLoaded', function () {
        fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                document.getElementById('output').textContent = data.message;
            });
    });
}
  