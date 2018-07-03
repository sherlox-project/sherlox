from namechk import Namechk

class EngineLoader:
	engines="None"
	data = {}
	def __init__(self):
		self.engines={"namechk" : Namechk()}

	def run (self, engine_id, user_name):
		return self.engines[engine_id].run(user_name)

	