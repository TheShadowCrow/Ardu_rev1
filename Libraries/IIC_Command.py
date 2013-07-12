class IIC_Command:
	def __init__(self, name, command, data):
		self.name = name
		self.command = ord(command) #mogelijk ord(command)
		self.data = data
		self.send = False
	
	def setValue(self, value):
		self.data = value
		self.send = True
		
	def setCommand(self, command):
		self.command = command
