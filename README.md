Please set timer mode to File and Milliseconds.
Set input mode to Fling.

Run the .py program, go in game, press shift to start. Press F8 to exit the program.
Put inputs into inputs.txt.
Redos update automatically, if they are wrong you can open redos.txt in a text editor and set it back to 0.

Available functions:
	
	reset():
		Works when paused in game, great to toss at the start of your inputs.txt file
		Works on 1920x1080 Fullscreen.
	
	
	waitfor(ms, pause=False):
		Waits for the timer to hit the specified amount of ms, if pause parameter is set to true it will pause once it hits this amount of ms, great to enable at the last line so it will show you where you land.
	
	
	mouse_input(angle_deg, duration=0.005, dist=500):
		0 is straight up, 90 is straight to the right, ect.
		
	time.sleep(ms):
		Allows for waiting, should only ever be used when menuing.
	
	mouse.move(x,y):
		Moves mouse to position on screen, only used for menuing.
	
	mouse.click():
		Clicks mouse, only used for menuing. 