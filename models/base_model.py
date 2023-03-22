#!/usr/bin/python3

import uuid
from datetime import datetime
from . import storage

class BaseModel:
    	
	"""
	Base Model class with
	"""
	def __init__(self, *args, **kwargs):
    		
			
		""" 
		method to instantiate objects with some validations
		"""
		if len(kwargs) != 0:
			for key, value in kwargs.items():
				if key == 'id':
					self.id = value
				elif key == 'created_at':
					value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")  
					self.created_at = value
				elif key == 'updated_at':
					value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")  
					self.updated_at = value
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			storage.new(self)
	def __str__(self):
    		
		"""
		unofficial representation of a class
		"""
		return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
	def save(self):
    		
		"""
		updates the public instance attribute updated_at with current datetime
		"""
		self.updated_at = datetime.now()
		storage.save()
	def to_dict(self):
    		
		"""
		returns a dictionary containing all key/values of __dict__ of instances
		"""
		dicts = {
				'id': self.id,
				'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
				'updated_at': self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
				'__class__': __class__.__name__,
				
				}
		return dicts