Snake and Ladder - folder 
	
	1.Assets - folder 
		- images - folder 
		- sound - folder 
		
	2.Entities - folder
		- dice.py - generates random number from 1 to 6. and return dice image and random number.
		- ladder.py - takes and return two values. takes number and checks, return the number also returns the boolean value whether ladder is present or not.
		- matrix.py - hard coded x and y coordinates of the snake and ladder board from 1 to 100.
		- snake.py - takes and return two values. takes number and checks, return the number also returns the boolean value whether snake is present or not.
	
	3.Utilities - folder
		- background.py - display images of background, snake, and play button.
		- players.py - display the string "Player 1", "Player 2", "Your Turn!!!". Also the positions the red and blue tokens.
		- screen_size.py - width size and height size.
	
	4.main.py
		- It runs the game untill sys.exit() is called or the program gets over. 
		- condition for red and blue.
		- condition for every dice number inside red and blue as well.
		- when the program ends it displays Winning msg and wait for 10 sec and then close it automatically.
