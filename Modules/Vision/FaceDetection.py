import cv
#HAAR_CASCADE = "face.xml"

class FaceDectect:
	def __init__(self, cascade, cam):
		self.capture = cv.CaptureFromCAM(cam)
		self.storage = cv.CreateMemStorage()
		self.cascade = cv.Load(cascade) 


	def detect_faces(self, image): 
		faces = [] 
		detected = cv.HaarDetectObjects(image, self.cascade, self.storage, 1.2, 2,  cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
		if detected:
			for (x,y,w,h),n in detected:
				faces.append((x,y,w,h))
		return faces
		
	def detect_faces(self):
		self.get_Image()
		faces = [] 
		detected = cv.HaarDetectObjects(self.image, self.cascade, self.storage, 1.2, 2,  cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
		if detected:
			for (x,y,w,h),n in detected:
				faces.append((x,y,w,h))
		return faces
		
	def get_Image(self):
		self.image = cv.QueryFrame(self.capture)
		return self.image
	
if __name__ == "__main__":
	cv.NamedWindow("Video", 1)
	fd = FaceDetect("face.xml", 0)
	faces = []	
	i = 0
	while True: 	
		if i%5==0:
			faces= detect_faces()
		
		for (x,y,w,h) in faces:
            cv.Rectangle(fd.image, (x,y), (x+w,y+h), 255)
 
        cv.ShowImage("w1", fd.image)
        i += 1	