import os
from Game import Game

# clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# initialize variables
g = Game()
last_input = None

# The main loop
while True:
	state = g.get_state()

	# Print stuff
	print "Time - " + state["time"]
	print ""
	print state["message"]
	print ""
	for i in range(len(state["actions"])):
		print str(i) + ". " + state["actions"][i]
	print ""
	last_input = raw_input(":")

	# Wait and clear the screen
	os.system('cls' if os.name == 'nt' else 'clear')
	
	g.advance()