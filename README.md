Please set timer mode to File and Milliseconds.
Set input mode to Fling.


Very important keys:
	F1: Restart
 	F2: Decrease game speed by 0.2x
  	F3: Increase game speed by 0.2x
   	F4: Set game speed to 1x
	F5: Freeze game speed
 	F6: Set game speed to 1/240x (1 fps for 240hz refresh rate, but the game automatically interpolates)
	   		Speeds should only be used on very consistent parts or to slow motion a specific movement.
			They do not work well for long term usage; you should always ensure a movement works in 1x speed before proceeding.
    		Caution advised.
	May seem confusing, but think of them in groups:
	F1 F4 for utility
 	F2 F3 for normal speed changes
	F5 F6 for extremely slow speeds

Available functions:
	wait(ms):
		Waits for the timer to hit the specified amount of ms.
	wait(ground):
 		Waits for the player to hit the ground.
   	pause:
		Pauses.
  	speed(multiplier):
   		Sets gamespeed to multiplier amount. See speed warning above.
   	input(x,y):
		Feeds an input to the game.
  		Bounds:
			x: -12.5 (left) to 12.5 (right)
   			y: 1.25 (barely up) to 12.5 (all the way up)
	  		x,y are floats
		Caution advised, there are no checks to ensure x, y are within bounds. I have no idea what happens if they are not.

Any unrecognized lines in this file (empty lines, lines that start with /, #, ect. will be skipped.
The tool checks for the first character of the line; ensure that your commented lines start with a special character or they may crash the game.
Any lines that have incorrect syntax will crash the game.
Example script to ensure the tool works:
	/speed(2)
	speed(1)
	wait(0)
	input(11.88,11.9)
	wait(ground)
	input(12.5,4.4)
	wait(ground)
	pause

Good luck!
