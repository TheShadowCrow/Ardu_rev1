import cv
import FaceDetection 


class Tracker: 
	def __init__(self, tracking, factor):
		self.tracking = tracking #specify an face tracker or object tracker or color tracker etc..
		self.prevX = 0
		self.prevY = 0
		self.factor = factor

		
	def Track():
		self.tracking.Track()
		dx = self.prevX - self.tracking.CenterX
		dy = self.prevY - self.tracking.CenterY
		pos = []
		pos[0] = dx / self.factor
		pos[1] = dy / self.factor
	return pos 
	

class FaceTracker(FaceDetection.FaceDetect): 

	def Track(self):
		faces = []
		faces = self.detect_faces()
		if(len(faces) == 1 ):
			for (x,y,w,h) in faces:	#x,y cordinate, width height
				self.CenterX = x + (0.5 * w)
				self.CenterY = y +(0.5 * h)
			
	