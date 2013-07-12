class IIC_Device:
	def __init__(self, bus, address, device_driver):
		self.bus = bus
		self.address = address
		self.driver = device_driver
	
	def sendData(self):
		data_out = []
		n = 0
		for item in self.driver.out:
			if(item.send == True):
				data_out.append(item.command)
				data_out.append(item.data)
				self.driver.out[n].send = False
			n = n + 1
        
		self.bus.write_block_data(self.address, 0, data_out)
				

	def setInternalCommand(self, command, data):
		self.driver.setCommand(command, data)
		self.sendData()
	
	def setMainData(self, data):
		self.driver.setMain(data)
		sendData()
	
	def getState(self):
		return self.driver.state
