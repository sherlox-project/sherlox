from Engines import EngineLoader

class Core:
	username_osint_sources  = ["facebook"]
	user_name = ""
	engine_loader = None

	def __init__(self, user_name):
		self.user_name = user_name
		self.engine_loader = EngineLoader()

	def username_osint(self):
		for engine in self.engine_loader.engines:
			data = self.engine_loader.run_username_osint(engine, self.user_name)
		print data