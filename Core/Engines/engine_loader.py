from facebook_engine import FacebookEngine

class EngineLoader:
	engines="None"
	data = {}
	def __init__(self):
		self.engines={"facebook" : FacebookEngine()}

	def run_username_osint (self, engine_id, user_name):
		return self.engines[engine_id].run_username_osint(user_name)
