from Engines import EngineLoader
from Parsers import ParserLoader
class Core:
	username = ""
	parsers = None
	engines = None

	def __init__(self, user_name):
		self.username = user_name
		self.parsers = ParserLoader()
		self.engines = EngineLoader()

	def username_osint(self):
		data = self.engines.run(self.username)
		print data
