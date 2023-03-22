# !/usr/bin/python3

from shlex import split
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


classes = {
			'BaseModel': BaseModel,
			'User': User,
			'Place': Place,
			'State': State,
			'City': City,
			'Amenity': Amenity,
			'Review': Review
			}
class HBNBCommand(cmd.Cmd):
	prompt = "hbnb$ " # changes the default value of the prompt which was 'Cmd'                     
	def do_quit(self, line):
		"""
		exit the program
		"""
		return True
	def do_EOF(self, line):
		"""
		exit the program
		"""
		return True
	def do_help(self, line):
		"""
		help section
		"""
		helpsec = split(line)
		if len(helpsec) > 1:
    			
			print("Error")
		elif helpsec == []:
    			
			print("Documented commands (type help <topic>):\
				========================================\
	 		\nEOF  quit  create  show  all  destroy  update")
		elif helpsec[0] == 'EOF':
    			
			print("EOF: to exit")
		elif helpsec[0] == 'quit':
    			
			print("Quit: to exit")
		elif helpsec[0] == 'create':
    			
			print("Create:\n\tcreates  a new instance of BaseModel, saves it to JSON file, prints the id")
		elif helpsec[0] == 'show':
    			
			print("Show:\n\tPrints string representation of an instance based on class name & id")
		elif helpsec[0] == 'destroy':
    			
			print("Destroy:\n\tDeletes an instance based on the class name & id")
		elif helpsec[0] == 'all':
    			
			print("All:\n\tPrints all string representation of all instances based or not onthe class name")
		elif helpsec[0] == 'update':
    			
			print("Update:\n\tUpdates an instance based onthe class name & id by adding or updating attribute, saves the change into JSON file")
	def do_create(self, line):
    		
		"""
		creates  a new instance of BaseModel
		saves it to JSON file
		prints the id
		"""
		model1 = split(line) # splits the line that is recieved from commandline & stores it in a list
		if model1 == []:
			print("** class name missing **")
		elif model1[0] not in classes:
			print("** class doesn't exist ** ")
		else:
			models = classes[model1[0]]() # creating instance of BaseModel
			models.save()
			print(models.id)
	def do_show(self, line):
    		
		"""
		prints string representation of an instance based on class name & id
		"""
		model2 = split(line)
		if model2 == []:
    			
			print("** class name missing **")
		elif model2[0] not in classes:
    			
			print("** class doesn't exist ** ")
		elif len(model2) == 1:
    			
			print("** instance id missing **")
		else:
    			
			new = f"{model2[0]}.{model2[1]}" # extracts classname.id
			objs = models.storage.all() # extracting all data and stores to 'objs'
			if new not in objs: # if id not found
    				
				print("** no instance found **")
			else:
    				
				print(objs[new])

	def do_destroy(self, line):
    		
		"""
		Deletes an instance based on the class name & id
		"""
		model3 = split(line)
		if model3 == []:
    			
			print("** class name missing **")
		elif model3[0] not in classes:
    			
			print("** class doesn't exist **")
		elif len(model3) == 1:
    			
			print("** instance id missing **")
		else:
    			
			des = f"{model3[0]}.{model3[1]}"
			objtoDel = models.storage.all()
			if des not in objtoDel:
    				
				print("** no instance found **")
			else:
    			# delete and save chages
				del objtoDel[des]
				models.storage.save()
	def do_all(self, line):
    		
		"""
		prints all string representation of all instances based or not onthe class name
		"""
		lists = []
		model4 = split(line)
		if model4 == []: # command without classname
    			
			for instances in models.storage.all().values(): # doesn't consider key/pair DS, it displays all classes data
    				
				lists.append(str(instances))
				
		else:
    			
			if model4[0] not in classes:
    				
				print("** class doesn't exist **")
				return False # to prevent printing lists if the class doesn't exist
			else:
    				
				for key, value in models.storage.all().items(): # key/pair DS is there in specific class
    					
					if value.__class__.__name__ == model4[0]:
    						
						lists.append(str(value))
		print(lists)

    				
	def do_update(self, line):
    		
		"""
		Updates an instance based onthe class name & id by adding or updating attribute
		saves the change into JSON file
		"""
		model5 = split(line)
		if model5 == []:
    			
			print("** class name missing **")
		elif model5[0] not in classes:
    			
			print("** class doesn't exist **")
		elif len(model5) == 1:
    			
			print("** instance id missing **")
		elif len(model5) == 2:
    			
			print("** attribute name missing **")
		elif len(model5) == 3:
    			
			print("** value missing **")
		else:    			
			updated = f"{model5[0]}.{model5[1]}"
			objects = models.storage.all()
			if updated not in objects:
    				
				print("** no instance found **")
			else:
    				
				setattr(models.storage.all()[updated], model5[2], model5[3]) # adding attribute 
				models.storage.save()
if __name__ == '__main__':
	HBNBCommand().cmdloop()