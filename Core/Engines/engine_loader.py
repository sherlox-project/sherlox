from namechk import Namechk

class EngineLoader:
	engines="None"
	def __init__(self):
		self.engines=[Namechk()]

	def run(self, user_name):
		for engine in self.engines:
			engine.run(user_name)
