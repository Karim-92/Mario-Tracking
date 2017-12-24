""" 
A simple computer vision program to track Super Mario in a video
Based on the "Template Matching" Algorithm
"""
# Libraries needed, Just OpenCV
import cv2

# Tracking Function, takes two parameters, image frame and the template to match
def trackMario(imageFrame, templateImage):
	grayscaleFrame= cv2.cvtColor(imageFrame, cv2.COLOR_RGB2GRAY)
	templateHeight, templateWidth=templateImage.shape[:2]
	locations=cv2.matchTemplate(grayscaleFrame, templateImage, method=cv2.TM_SQDIFF)
	min_loc=cv2.minMaxLoc(locations)[2]
	x_min, y_min=min_loc
	cv2.rectangle(imageFrame, (x_min-30, y_min-30), (x_min+templateWidth+20, y_min+120), color=[255,0,0], thickness=2)
	return imageFrame

def main():
	# Video Capture Object and read mario template as grayscale
	vidCap=cv2.VideoCapture('Tracking_Mario.mp4')
	template=cv2.imread('marioTemplate.jpg')
	template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
	templateHeight, templateWidth=template.shape[:2]
	print("Template Height: " , templateHeight , " Template Width: ", templateWidth)

	# Video saving parameters, uncomment below to use openCV videowriter
	fourcc = cv2.VideoWriter_fourcc(*'MJPG')
	vidOut = cv2.VideoWriter('trackedVideo.avi',fourcc, 30.0, (1280,720))
	while(vidCap.isOpened()):
		frameExists ,imageFrame=vidCap.read()
		if(frameExists):
			imageFrame=trackMario(imageFrame, template)
			vidOut.write(imageFrame)
			cv2.imshow('Tracking Mario', imageFrame)
			cv2.waitKey(1)
		else:
			break
	vidCap.release()
	vidOut.release()
	cv2.destroyWindow('Tracking Mario')

main()