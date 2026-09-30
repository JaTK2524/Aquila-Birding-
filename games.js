let SavedMoney = localStorage.getItem("winnings")

let money;

if(SavedMoney === null) {
    money = 100;
    localStorage.setItem("winnings", money)
    } else {
             money = Number(SavedMoney)
             
             if (money === 0) {
                 money = 50;
                 localStorage.setItem("winnings", money);
                   }
                 }  
    

const play = document.getElementById("play");
const guess = document.getElementById("guess");
const MoneyDisplay = document.getElementById("money");
const bet = document.getElementById("bet");
const resultDisplay = document.getElementById("result")

MoneyDisplay.textContent = "Seeds: " + money;
function flipCoin() {
     const choices = ["Heads", "Tails", "Third-Face"];
     const result = choices[Math.floor(Math.random() * choices.length)];
     
     const chosenGuess = guess.value;
     const chosenBet = Number(bet.value);
     
     if (chosenBet <= 0 || chosenBet > money) {
         resultDisplay.textContent = "Please place a valid bet.";
         return;
         
         }
     if (result === chosenGuess) {
         money += chosenBet;
         
         resultDisplay.textContent  = 
           "🦉  You won! The result was " + result + ". You receive " + chosenBet + " seeds!   🦉"  ; 
           } else {
                    money -= chosenBet;
                    
                    resultDisplay.textContent = "🦜  You lost! The result was " + result + ". You lose " + chosenBet + " seeds.  🦜"
                    }
           
           MoneyDisplay.textContent = "Seeds: " + money;
           
           localStorage.setItem("winnings", money);
           
           
           if (money === 0) {
           
               const newGame = confirm("Do you want to start a new game with 50 seeds? ")
               
               if(newGame) {
                 money = 50;
                 MoneyDisplay.textContent = "Seeds: " + money;
                 localStorage.setItem("winnings", money);
                    }
             }
             
        }    
                    play.addEventListener("click", flipCoin);
                    document.addEventListener("keydown", function(event) {
                     if (event.key === "Enter") {
                        flipCoin();
                      }
                     if (event.key === "/") {
                      bet.focus();
                      }
                     if (event.ctrlKey && event.key === "o") {
                        event.preventDefault();
                        guess.focus();
                        }
                     if(event.key === "Escape")  {
                        event.preventDefault();
                        bet.value = "";
                        bet.dispatchEvent(new Event("input"));
                        bet.focus();
                        }
                        
           });  
    const audio = document.getElementById("casinoMusic")
    const button = document.getElementById("muteButton")
    
    button.addEventListener("click", function() {
     audio.muted = !audio.muted
     
     if (audio.muted) {
         button.textContent = "🔇";
         } else {
                  audio.play()
                  button.textContent = "🔊";
                   }
                    });
                    document.addEventListener("keydown", function(event) {
                      if (event.ctrlKey && event.key.toLowerCase() === "m") {
                           button.click();
                            }
                            
                          });  
         
