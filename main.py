import time, sys, os
from Game import Game

# clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# initialize variables
g = Game()

# The main loop
while True:
	state = g.advance()
	print "Time - ", state["time"],

	# Wait and clear the screen
	sys.stdout.flush()
	print "\r",
	time.sleep(1)