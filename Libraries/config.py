#config file loader
import xml 
import os 
class ConfigLoader:
	def __init__(self, ModuleName, config="default"):
		self.Module = ModuleName
		if config == "default":
			self.config = "default.xml"
		
	def ParseConfigFile(self):
	

class CoreConfigParser(ConfigLoader):