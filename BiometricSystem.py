from Tkinter import *
from tkFileDialog import *
import tkMessageBox
import os
from PIL import Image 
from PIL import ImageEnhance
import PIL
import PIL.Image
import math
import hashlib
import binascii
import cv2
from os.path import basename
import numpy as np
import sys
import datetime



temp = ""
global listl
global t
global file_contents
file_contents=[]
listl=[];
brightness = 2
contrast =	1.1
def train(rollnumber,names):
		thefile=open('names.txt','a')
		#listl.append(names)
		#for items in listl:
		thefile.write("%s\n" %names)
		read_file=open('names.txt', 'r')
		file_contents = read_file.read().split('\n')
		print file_contents
		
		
		read_file.close()

		faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		camera = cv2.VideoCapture(0)
		#for r in range(1,3):
		for i in range(0,10):
			ext=['.centerlight','.glasses','.happy','.leftlight','.noglasses','.rightlight','.sad','.sleepy','.surprised','.wink']
			while True:
				return_value,image = camera.read()
				if return_value == True:
					gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
					faces = faceCascade.detectMultiScale(
						gray,
						scaleFactor=1.3,
						minNeighbors=15,
						minSize=(30, 30),
						flags=cv2.cv.CV_HAAR_SCALE_IMAGE
					)
					flag = False
					for (x, y, w, h) in faces:
							cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 5)
							flag = True
							
					cv2.imshow(ext[i],image)
					if (cv2.waitKey(1) & 0xFF == ord('s')) or (cv2.waitKey(1) & 0xFF == ord('S')):
							
							if not flag:
								continue
							count = 1
							for (x,y,w,h) in faces:

								#cv2.imshow('subject1'+ext[i],gray)
								cv2.waitKey(1000)
								cv2.destroyWindow(ext[i])
								cwd = os.getcwd()
								print cwd
								#newpath = cwd+'test'
								#print newpath
								if not os.path.exists('test'):
									os.mkdir('test')
								cv2.imwrite(os.path.join('test', 'subject'+str(rollnumber)+ext[i]+'.jpg'), gray)
								if cv2.waitKey(1) & 0xFF == ord('q'):
									
									break
							break
		#camera.release()
		cv2.destroyAllWindows()
   
	
	
def sad():
			faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
			camera = cv2.VideoCapture(0)
			read_file=open('names.txt', 'r')
			file_contents = read_file.read().split('\n')
			t= len(file_contents)
			read_file.close()
			print file_contents
			print t
			i = datetime.datetime.now()
			klpd=str(("%s/%s/%s" % (i.day, i.month, i.year) ))
			for i in range(0,1):
					ext=['.normal']
					while True:
						return_value,image = camera.read()
						if return_value == True:
							gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
							faces = faceCascade.detectMultiScale(
								gray,
								scaleFactor=1.3,
								minNeighbors=15,
								minSize=(50, 50),
								flags=cv2.cv.CV_HAAR_SCALE_IMAGE
							)
							flag = False
							for (x, y, w, h) in faces:
									cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 5)
									flag = True
									
							cv2.imshow(ext[i],image)
							if cv2.waitKey(1):
									
									if not flag:
										continue
									count = 1
									for (x,y,w,h) in faces:

										#cv2.imshow('subject1'+ext[i],gray)
										cv2.waitKey(1000)

										cv2.destroyWindow(ext[i])
										cwd = os.getcwd()
										print cwd
										#newpath = cwd+'test'
										#print newpath
										if not os.path.exists('test'):
											os.mkdir('test')
										read_file=open('names.txt', 'r')
										file_contents = read_file.read().split('\n')
										t= len(file_contents)
										for j in range (1,t):
											cv2.imwrite(os.path.join('test', 'subject'+str(j)+ext[i]+'.jpg'), gray)
											if cv2.waitKey(1)& 0xFF == ord('q'):
											
												break
									break
					camera.release()
					cv2.destroyAllWindows()

					cascadePath = "haarcascade_frontalface_default.xml"
					faceCascade = cv2.CascadeClassifier(cascadePath)

					recognizer = cv2.createLBPHFaceRecognizer()

					def get_images_and_labels(path):
						
						rahul =0
						image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.normal.jpg')]
					  
						images = []
						
						labels = []
						for image_path in image_paths:
							
							image_pil = Image.open(image_path).convert('L')
						
							image = np.array(image_pil, 'uint8')
							
							nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
							
							
							faces = faceCascade.detectMultiScale(image,scaleFactor=1.3,
									minNeighbors=13,
									minSize=(30, 30),
									flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
							
							for (x, y, w, h) in faces:
								images.append(image[y: y + h, x: x + w])
								labels.append(nbr)
								
								cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
								cv2.waitKey(1)
					   
						return images, labels


					path = './test'

					images, labels = get_images_and_labels(path)
					cv2.destroyAllWindows()

					print labels




					recognizer.train(images, np.array(labels))


					image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.normal.jpg')]
					for image_path in image_paths:
						predict_image_pil = Image.open(image_path).convert('L')
						predict_image = np.array(predict_image_pil, 'uint8')
						faces = faceCascade.detectMultiScale(predict_image)
						for (x, y, w, h) in faces:
							nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
							nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
							
							if nbr_actual == nbr_predicted:
								print "Recognition will depend on confidence: so your confidence with your trained images is  {}".format(conf)
								if conf<100:
									if conf<60:
									
									   print nbr_actual-1
									   tkMessageBox.showinfo( "Attandance Status","your attandance is successful "+file_contents[nbr_actual-1] + "  Thanks  !!")
									   attn_file=open('attendance.txt', 'a')
									   i = datetime.datetime.now()
									   klpd=str(("\n%s/%s/%s" % (i.day, i.month, i.year)))
									   print klpd 
									   attn_file.write(klpd +"-------"+file_contents[nbr_actual-1])
									else:
									   tkMessageBox.showinfo( "Attandance Status","Attander is incorrect person:you are not part of organization ")
								else:
									   break
							#cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
							cv2.destroyAllWindows()





       
# GUI 



def pass_alert(t):
   tkMessageBox.showinfo("Rollnumber Alert","Please enter a valid Rollnumber. Ex:- "+str(t))
   
def pass_alert2():
   tkMessageBox.showinfo("Student Name Alert","Please enter a valid Student Username") 
   

   

def image_open():
	
	global file_path_e
	
	
	rollnumber = passg.get()
	names = passg2.get()
	read_file=open('names.txt', 'r')
	file_contents = read_file.read().split('\n')
	t= len(file_contents)	
	read_file.close()
	if rollnumber == ""  or names ==  "":
		if rollnumber == "" :
			pass_alert(t)	
		else:
			pass_alert2()
	elif (int(rollnumber) == t ):
		train(rollnumber,names)
	else :
		pass_alert(t)
	
			
	
	

	
def cipher_open():
	
		global file_path_d
		   
		sad()


	
class App:
  def __init__(self, master):
    
	global passg
	global passg2
	global m
	title = "BioMetric System"
	author = "ECA_TEAM"
	msgtitle = Message(master, text =title)
	msgtitle.config(font=('helvetica', 17, 'bold'), width=200)
	msgauthor = Message(master, text=author)
	msgauthor.config(font=('helvetica',10), width=200)

   
	canvas_width = 200
	canvas_height = 50
	w = Canvas(master, 
		   width=canvas_width,
		   height=canvas_height)

	
	msgtitle.pack()
	msgauthor.pack()
	w.pack()
	
   
	passlabel = Label(master, text="Enter Roll no:")
	passlabel.pack()
	passg = Entry(master, width=20)
	passg.pack()

	passlabel = Label(master, text="Enter Name:")
	passlabel.pack()
	passg2 = Entry(master, width=20)
	passg2.pack()

	self.train = Button(master, 
						 text="save image", fg="black", 
						 command=image_open, width=25,height=5)
	self.train.pack(side=LEFT)
	self.sad = Button(master,
						 text="Detect", fg="black",
						 command=cipher_open, width=25,height=5)
	self.sad.pack(side=RIGHT)



root = Tk()
root.wm_title("BioMetric System")
app = App(root)
root.mainloop()