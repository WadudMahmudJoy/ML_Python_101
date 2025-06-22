import random
import time

choices = ['rock', 'paper', 'scissors']
fun_facts = [
    "Did you know? The game originated in China over 2,000 years ago!",
    "Fun fact: In Japan, it's called 'Jan-Ken'.",
    "Rock, Paper, Scissors is used to settle disputes worldwide!",
    "Scissors beats paper, but did you know paper was once made from papyrus?",
    "Some people play with extra moves like 'lizard' and 'Spock'!"
]

player_score = 0
computer_score = 0
game_history = []

print("Welcome to Rock, Paper, Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

while True:
    print(f"\nScore - You: {player_score} | Computer: {computer_score}")
    player = input("Your move: ").strip().lower()
    if player == 'quit':
        print("Thanks for playing!")
        break
    if player not in choices:
        print("Invalid choice. Try again.")
        continue
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if player == computer:
        result = "It's a draw!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        result = f"You win! {player.capitalize()} beats {computer}."
        player_score += 1
    else:
        result = f"You lose! {computer.capitalize()} beats {player}."
        computer_score += 1
    print(result)
    game_history.append(f"You: {player} | Computer: {computer} | {result}")
    if len(game_history) > 10:
        game_history.pop(0)
    print(random.choice(fun_facts))
    print("Game History (last 10):")
    for h in game_history:
        print("  ", h)
    time.sleep(1)
