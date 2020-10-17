// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];



let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

function respond() {
    // Your Code Here
    let img = document.getElementById("yoda-pic");
    let input = document.getElementById("user-input");
    let chatbox = document.getElementById("chat-box");
    let canSpeak = false;
    let arr;

    addMessage(input.value, true);
    
    let srcStr = "";

    if(input.value.includes(names[0]) || input.value.includes("baby")) {
        srcStr += "cute-";
    } else {
        srcStr += "regular-";
        canSpeak = true;
    }

    if(input.value.includes(moods[1])) {
        if(input.value.includes(moods[0])) {
            srcStr += "dark";
            arr = dark_quotes;
        } else {
            srcStr += "force";
            arr = force_quotes;
        }
    } else {
        srcStr += "std";
        arr = std_quotes;
    }

    let text;
    if(canSpeak) {
        let r = Math.floor(Math.random() * arr.length);
        text = arr[r];
    } else {
        text = "Hmmmmmmmmm"
    }
    addMessage(text, false);

    img.setAttribute("src", `img/${srcStr}.jpg`);

    input.value = "";
}

document.getElementById("user-input").addEventListener("keydown", function(e) {
    if(e.key === "Enter") {
        respond();
    }
});

function addMessage(text, user=true) {
    let chatbox = document.getElementById("chat-box");

    let typeOfMessage, person;
    if(user) {
        typeOfMessage = "user-message" ;
        person = "You";
    } else { 
        typeOfMessage = "yoda-message";
        person = "Yoda";
    }

    let message = document.createElement("DIV");
    message.classList.add(typeOfMessage);
    message.innerHTML = `<p><b>${person}: </b>${text}</p>`;
    chatbox.appendChild(message);

    chatbox.scrollTop = chatbox.scrollHeight;

}