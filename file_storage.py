# !/usr/bin/python3

import json
import os

class FileStorage:
    	
	"""
	File Storage class with two private attribute
	"""
	__file_path = "file.json"
	__objects = {}
	def all(self):
    		
		"""
		returns dictionary
		"""
		return FileStorage.__objects
	def new(self, obj):
    		
		"""
		sets in objects the obj with key <obj class name>.id
		"""
		objname = obj.__class__.__name__
		objid = obj.id

		key = str(objname) + "." + str(objid)
		value = obj

		FileStorage.__objects[key] = value # sets in __objects the obj with key <obj class name>.id
	def save(self):
    		
		"""
		serializes objects to the JSON file

		serialization - python to JSON (dump/ dumps(this one is with only one argument)
		"""
		dictionary = {}
		for key, value in FileStorage.__objects.items():
			dictionary[key] = value.to_dict() # changing not serializable object to dictionary & store the values with respect to their key

		with open(FileStorage.__file_path, "w") as file:
			json.dump(dictionary, file) # serializing changed dictionary

	def reload(self):
    		
		"""
		deserializes the JSON file to objects if the path to the file exists

		# deserialization - JSON to python (loads)
		"""
		if os.path.exists(FileStorage.__file_path):
			with open(FileStorage.__file_path, "r") as file:
				json.load(file)

	def delete(self, obj=None):
		# delete obj from __objects if it's inside
		if obj != None:
			key = "{}.{}".format(type(obj.__name__), obj.id)
			print("key value ",key)
			if FileStorage.__objects[key]:
				del FileStorage.__objects[key]
				self.save()

""" Test delete feature
"""

from models.state import State

fs = FileStorage()

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])