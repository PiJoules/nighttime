# The main class that runs the entire game.
# 
# The class just manages what to do on each turn
# and returns a state on each turn.
# 
# It does not increment the turns. It instead is run on every
# turn by some other function.

class Game:
	def __init__(self, time=0, speed=10):
		"""
		time: 	The current time in the game (defaults to 0).
		speed:	The ratio of in-game minutes to real-time seconds.
		"""
		self.time = time
		self.speed = speed

	# Advances through the game and receives a dictionary
	# of new inputs on each turn.
	# Returns the updated state of the player each turn.
	def advance(self, actions={}):
		self.advance_time()
		return {
			"time": self.get_readable_time()
		}

	# Update the time based on the speed
	def advance_time(self):
		self.time += 1
		if self.time >= int(60*24/self.speed):
			self.time = 0

	# Get the time as something more human readable
	def get_readable_time(self):
		hours = int(self.time*self.speed/60)
		minutes = self.time*self.speed % 60
		return str(hours) + ":" + str(minutes)