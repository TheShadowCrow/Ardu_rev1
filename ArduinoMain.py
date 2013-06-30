class Arduino_Main:
	def __init__(self, bus, address):
		self.bus = bus
		self.address = address
		self.data_out = {
			"left_speed": ['L', 0], 
			'left_dir': ['l', False], 
			'right_speed': ['R', 0],
			'right_dir': ['r', False],
			'h_turn': ['b', 45],
			'h_titl': ['n', 45]}
		self.data_int = {
			"Version": ['V' 1.0]
			}
	
	def sendData():
		arduino_out = []
		for item in data_out:
			adruino_out.append(data_out[item][0])
			adruino_out.append(data_out[item][1])
        
		bus.write_i2c_block_data(self.address, 0, arduino_out) 
	
	def Stop():
		self.data_out["right_speed"][1] = 0
        self.data_out["left_speed"][1] = 0
        sendData() # arduino vertellen om te stoppen
		
	def ForeWard(speed):
	    data_out["right_speed"][1] = speed
        data_out["left_speed"][1] = speed
        data_out["left_dir"][1] = True
        data_out["right_dir"][1] = True
		sendData()
		
	def TurnLeft(speed):
		data_out["right_speed"][1] = speed
        data_out["left_speed"][1] = speed
        data_out["left_dir"][1] = False
        data_out["right_dir"][1] = True
		sendData()
	
	def TurnRight(speed):
		data_out["right_speed"][1] = speed
        data_out["left_speed"][1] = speed
        data_out["left_dir"][1] = True
        data_out["right_dir"][1] = False 
		sendData()
		
	def Backward(speed):
		data_out["right_speed"][1] = speed
        data_out["left_speed"][1] = speed
        data_out["left_dir"][1] = False
        data_out["right_dir"][1] = False 
		sendData()
		