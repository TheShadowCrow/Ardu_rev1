class IIC_Device:
	def __init__(self, bus, addres, device_driver):
		self.bus = bus
		self.address = address
		self.driver = device_driver
	
	def sendData(self):
		data_out = []
		for item in self.driver.out:
			if(self.driver.out[item].send == True):
				data_out.append(self.driver.out[item].command)
				data_out.append(self.driver.out[item].data)
				self.driver.out[item].send = False 
        
		bus.write_i2c_block_data(self.address, 0, data_out)
				

	def setInternalCommand(self, command, data):
		self.driver.setCommand(command, data)
		self.sendData()
	
	def setMainData(self, data):
		self.driver.setMain(data)
		sendData()
	
	def getState(self):
		return self.driver.state