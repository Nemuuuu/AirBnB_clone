#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    	
	"""
	Place class inherited from BaseModel
	"""
	city_id = ""
	user_id = ""
	name = ""
	description = ""
	number_rooms = ""
	number_bathrooms = ""
	max_guest = 0
	price_by_night = 0
	latitude = 0.0
	logitude = 0.0
	amemity_ids = []
