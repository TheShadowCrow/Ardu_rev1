class IIC_Device:
	def __init__(self, bus, addres, device_driver):
		self.bus = bus
		self.address = address
		self.driver = device_driver
	
	def sendData():
		data_out = []
		for item in data_out:
			data_out.append(self.driver._out[item][0])
			data_out.append(self.driver._out[item][1])
        
		bus.write_i2c_block_data(self.address, 0, data_out)

	def setInternalCommand(command, data):
		self.driver.setCommand(command, data)
		sendData()
	
	def setMainData(data):
		self.driver.setMain(data)
		sendData()