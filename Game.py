# The main class that runs the entire game.
# 
# The class just manages what to do on each turn
# and returns a state on each turn.
# 
# It does not increment the turns. It instead is run on every
# turn by some other function.

import json, random

class Game:
	def __init__(self, time=0, speed=10):
		"""
		time: 	The current time in the game (defaults to 0).
		speed:	The ratio of in-game minutes to real-time seconds.
		"""
		self.time = time
		self.speed = speed

		# Load locations
		with open('json/locations.json') as locations_file:    
		    self.locations = json.load(locations_file)
		self.current_location =  self.locations["room"]

		# Load events
		with open('json/events.json') as events_file:    
		    self.events = json.load(events_file)

		# Load actions
		with open('json/actions.json') as actions_file:    
		    self.actions = json.load(actions_file)

		# Setup initial events
		self.previous_events = []
		self.current_events = []
		self.possible_future_events = []
		self.available_actions = []
		self.add_events()


	# Advances through the game and receives a dictionary
	# of new inputs on each turn.
	def advance(self, action=None):
		self.advance_time()
		self.add_events()

	# Add an event and appropriate actions depending on the time
	# and current location of the player
	def add_events(self):
		# Add the current events
		self.previous_events = self.current_events[:]
		self.current_events = []
		for event in self.current_location["events"][self.get_hour()]:
			if self.events[event]["chance"] > random.random():
				self.current_events.append(self.events[event])

		# Add the possible actions in response to these events
		self.available_actions = []
		for event in self.current_events:
			for action in event["actions"]:
				self.available_actions.append(self.actions[action])

	# Returns the updated state of the player each turn.
	# This is meant to be called after advance()
	def get_state(self):
		return {
			"events": {
				"responses": [],
				"new_events": [event["message"] for event in self.current_events]
			},
			"actions": [{"name": action["name"], "text": action["text"]} for action in self.available_actions]
		}

	# Update the time based on the speed
	def advance_time(self):
		self.time += 1
		if self.time >= int(60*24/self.speed):
			self.time = 0

	def get_hour(self):
		return int(self.time*self.speed/60)

	def get_minute(self):
		return self.time*self.speed % 60

	# Get the time as something more human readable
	def get_readable_time(self):
		return str(self.get_hour()) + ":" + str(self.get_minute()).zfill(2)