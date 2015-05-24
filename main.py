import os, json
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
	print json.dumps(state, indent=4)
	for event in state["events"]["new_events"]:
		print event
	print ""
	for i in range(len(state["actions"])):
		print str(i) + " - " + state["actions"][i]["text"]
	print ""
	last_input = raw_input(":")

	# Wait and clear the screen
	os.system('cls' if os.name == 'nt' else 'clear')
	
	g.advance()