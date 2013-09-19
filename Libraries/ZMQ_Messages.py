import json

class Message_Encoder(json.JSONEncoder):
	def default(self, obj):
        # Convert objects to a dictionary of their representation
        d = { '__class__':obj.__class__.__name__, 
              '__module__':obj.__module__,
              }
        d.update(obj.__dict__)
        return d

class Message_Decoder(json.JSONDecoder):
	def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            args = dict( (key.encode('ascii'), value) for key, value in d.items())
            inst = class_(**args)
        else:
            inst = d
        return inst

class Ardu_Message:
	def __init__(self, destination, origin, data, priority="*"):
		self.destination = destination
		self.origin = origin
		self.data = data
		self.priority = priority

class Module_info:
	def __init__(self, name, priority, status, mode="default" ,args="" ,origin, destination = '*'):
		self.name = name
		self.origin = origin
		self.priority = priority
		self.status = status 
		self.destination = destination
		self.mode = mode
		self.args = args 

class Loaded_Module(Module_info):
	def __init__(self, name, priority, status, mode="default" ,args="" ,origin, destination = '*'):
		Module_info.__init__(self, name, priority, status, mode="default" ,args="" ,origin, destination = '*')
		
	def Update(self, info): # updata from incomming Module_info message
		if(self.name == info.name && self.name != info.origin):
			self.status = info.status
			self.priority = info.priority
			return True
		
	def SetStatus(self, status):
		self.status = status
		return Module_info(self.name, self.priority, self.status, self.name, self.destination)
	
	def SetPriority(self, prio):
		self.priority = prio
		return Module_info(self.name, self.priority, self.status, self.name, self.destination)
		
class Command:
		def __init__(self, destination, priority, command, data):
		self.destination = destination
		self.priority = priority
		self.command = command
		self.data = data
		
class Sensor_Data:
		def __init__(self, label, type, data):
		self.label = label #example Sonar_Front
		self.type = type #ex distance
		self.data = data