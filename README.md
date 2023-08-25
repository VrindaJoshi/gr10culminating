# gr10culminating
FINAL SUMMATIVE ESCAPE ROOM PROPOSAL
VRINDA JOSHI - ICS208
MY ESCAPE ROOM’S PREMISE
Users will be tasked with finding the truth about the disappearance of Waldo Junior, the son and only heir of Waldo Senior, the multi-billionaire who recently passed away. To do so, the user will have to look for clues in Waldo Manor, the strange residence of the Waldos. 

The user will face obstacles throughout their journey. They will have to deal with broken stairs, dark rooms with hidden light switches, and numerous locked doors. The notes, ciphers, and keys they find along their journey may or may not be helpful in uncovering the whereabouts of Waldo Jr. One vital skill the user needs to find the truth, is to be able to solve riddles, and think creatively to do so.

The user will hopefully in the end find Waldo Jr, who is hiding in the hideout of the Manor. The notes that the user receives may hint towards a possible kidnapping of Waldo Jr, but it is revealed that the billionaire Waldo Sr had many unpaid debts that are now left to Waldo Jr in his will. Waldo Jr’s inability to pay the debts have left him no choice but to go into hiding.
SKILLS USED: 
if else statements + booleans - Key to make the game work. Conditionals ensured correct answer was needed to advance, or user had key to unlock
decision control structures were used in my code (when user has to choose which door to go into, what action to take next)
HOW I KEPT MY CODE EFFICIENT AND CLEAR:
To keep my code visibly organized, I separated sections using lines:
_______________________
A MAIN SECTION
(beginning, different door)
_______________________
…………………………………………………
A NEW WINDOW
…………………………………………………
+++++++++++++++++++++
HIGHLIGHTED
+++++++++++++++++++++
-----------------------------------
MAIN VARIABLES
------------------------------------
To make my life easier, I made variables for the hex codes and font sizes I used when formatting:
#colour variables
cream = "#f4eee0"
blue = "#151983"
black = "#000000"
white = "#ffffff"
#font presets
title_font = ("Century Schoolbook L", 30)
main_header_font = ("Century Schoolbook L", 18)
header_font = ("Century Schoolbook L", 16)
text_font = ("Century Schoolbook L", 11)
button_font = ("Century Schoolbook L", 10)
WHAT SET’S MY ESCAPE ROOM APART?
Some escape room ideas I added to make my code more creative were:
A room with the lights off, where the user has to find the lights with their mouse
I made use of customizable colors to make the background, the button, and the button text all black. I also reduced the button border to 0
A NDA at the end
I used conditional statements to check whether the user had checked the checkbox and entered their name before allowing them to continue
Different doors
Customizing the shape of buttons to make them look like a door
Locked drawers and boxes that require the user to go back and find the key
Changed the value of a variable to determine whether a key had been found yet. If yes, unlocked the lock.
ALGORITHM OF MY CODE
enter the escape room
introduce the situation
walk up the stairs - the stairs will break and you’ll have to figure out what material the stairs are made out to fix it (riddle to find material)
reach the top, where you’ll have to choose from 4 doors
first door - pitch dark (click all over the screen to find the light). 
when the light can be turned on, you’ll find a note in binary code (no cipher?!!)
there will be another door to get to the bathroom, where there will be a another note 
(first note - “waldo junior will be back from his vacation on <2 days ago date> (use time module) be sure to pick him up from the airport to avoid ‘them’!”) (second note - my drawer in my office may help you find out where i go if i get lost - waldo jr)
leave room (there’s nothing else to do here)
second door - its locked (complete riddle to unlock it)
inside is 2 doors
first door - enter a hallway (solve riddle to unlock) there will be one door at the end.
go inside (solve riddle to unlock). it’ll be waldo sr’s office. take the key
leave and return to 4 doors base (nothing else to do here)
second door - enter waldo jr’s office (solve riddle to unlock). open his drawer (with the key you found on the balcony) 
find cipher
nothing else here
third door - this room will contain a box with a lock. (unlock w waldo sr office key)
with the key unlock the box to discover a note.
the note will read: “MOVE THE BOX”
you are able to move it. underneath the box is a hole in the ground, with a slide to a pitch dark basement. (solve a riddle correctly to go down the slide)
in the basement, you’ll call out, where you’ll hear the voice of someone
you’ll trip and fall into a cage trap!! all you can do is call for help
someone will come out to ask you a riddle
if you’re correct, the someone will trust you and reveal themselves as waldo jr
waldo jr will tell you about what happened and you will be able to go home, finally knowing the truth
fourth door - goes to the balcony, where you’ll find a key (to where?!?)
PSEUDOCODE
import modules (tkinter, tkinter.messagebox, time)
colour variables
refresh function
if 4
there’s nothing else here
make key label and next button and pack
message box (tell user they on balcony)
if 2:
riddle to unlock each
1
nothing else to do here (messagebox)
inside there will be a cipher (add to cipher window/make it)
riddle to unlock
waldo sr’s office will be at the end
tell user their in a hallway, with a door at the end
2 
nothing else to do here (messagebox)
else make note label
when user opens drawer, tell them they need a key if they dont have the one from the balcony
enter jr’s office - tell user to open the drawer (messagebox)
tell user theyre in jr’s bedroom, there will be 2 doors
riddle to unlock
if 3
if it's right, the someone will reveal their idenity as waldo and tell them about his fathers loans, which waldo will have to fulfill. waldo make you sign an nda, (checkbox), and you’ll be allowed to leave (call win)
if wrong call lose
a riddle pops up tl window 
user gets stuck in a trap
make bg black
if right call next f
if wrong redo
riddle for what is in the hole
if correct move box button will pop up 
pop up tl window to enter what the note says
if have key - refresh make + pack note label
box that when clicked - message box to say it’s locked (unless user has key)
if 1 
mb - there’s nothing else here - return to door base
transform to bathroom - show note (note is a button that when clicked will show the note in the note window)
message box - there's nothing else here, lets go to the bathroom 
message box to say the lights turned on - transform window to show note (note is a button that when clicked will pop up notes window, show it there, and pop up message box to explain that the note requires a cipher
make window bg black, button black (button “turns on lights”) 
Tranform to landing, amke buttons for ech door
no - refresh window and call riddle1 again 
check whether response is correct
pop up messagebox, transform root window to riddle1
transform to stairs window
transform to intro window
make root window - beginning window

ANSWERS
R: I come from a mine and always get surrounded by wood. What am i? (answer in lowercase!)
A: pencil lead

R: What is cut on a table, but is never eaten? (answer in lowercase!)
A: a deck of cards

R: I shave every day, but my beard stays the same. What am i? (answer in lowercase)
A: a barber

R: If two’s company, and three’s a crowd, what are four and five?
A: 9 / nine

Q: What did the note say?
A: MOVETHEBOX

R: I take people down, but they love me. What am i?
A: a slide

R: What flies with no wings? (answer in lowercase) *YOU MUST GET THIS RIGHT 1ST TRY OR LOSE
A: time



