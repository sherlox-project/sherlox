from Engines import EngineLoader
from Parsers import ParserLoader
class Core:
	parsers = None
	engines = None

	def __init__(self):
		self.parsers = ParserLoader()
		self.engines = EngineLoader()
