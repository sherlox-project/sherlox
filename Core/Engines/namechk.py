import requests

class Namechk:
	
	token = ""
	def __init__(self):
		home = requests.get('https://namechk.com/')
		print home

	def run(self, user_name):
		return "not implemented"