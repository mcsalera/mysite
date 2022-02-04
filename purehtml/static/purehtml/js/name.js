let showName = false;
let name = document.getElementById("name");
let nameButton = document.getElementById("name-btn")

function changeDisplay(){
    if (showName) {
        name.innerHTML = 'Hi, I\'m Marie Curie!';
        nameButton.innerHTML = 'Hide'
    } else {
        name.innerHTML = '';
        nameButton.innerHTML = 'Show'
    }
};

nameButton.addEventListener("click", () => {
    showName = !showName;
    changeDisplay();
})