# Bomb-Guessing-Game-Final
This is a bomb guessing game. Click either the dog's left or right hand and avoid clicking on the bomb.

How does the code work:
Only requires importing pygame, random, and sys.

Game states helped give the bomb a "random" side (left or right) to choose, determine if the bomb is revealed, determine which hand is open or closed when it's clicked on, show the explosion image for a second after bomb is clicked on, and a reveal timer to give time to show bomb in hand.

In draw(), there is sections called not revealed, clicked_hand, revealed and not show_explosion, & show_explosion

"if not revealed" kept the closed fist image on both left and right hands

"if clicked_hand" changes one closed fist to a open hand picture

"if revealed and not show_explosion" puts bomb image into the open hand

"show_explosion" changed the bomb image to an explosion image

While the code is running:

Score is kept count (No highscore system)

The player only needs to click with their mouse and game will recieve a "tick" to start the reveal_timer's tick count in order to accurately time the bomb's reveal if the hand with the bomb is picked. If the bomb is picked, then the code will move on to play the explosion sound and the show_explosion which changes the bomb to an explosion after a second and a game over text is given. Then the program ends once the player loses
