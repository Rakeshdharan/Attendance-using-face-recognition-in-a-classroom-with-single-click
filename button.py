import tkinter
import os
import tkinter.font as font
from PIL import ImageTk ,Image
from tkinter import*

top = tkinter.Tk()
top.title("Autonomous Attendance System using Facial Recognisation")

frame_a = tkinter.Frame(master = top)
frame_a.pack()

frame_a.rowconfigure(0,weight = 1 , minsize = 100)
frame_a.columnconfigure(0,weight = 1 , minsize = 1000)

Label(top, text = 'Post Attendance in seconds', font =('Verdana', 10)).pack(side = TOP, pady = 10) 
# Creating a photoimage object to use image 
photo = ImageTk.PhotoImage(file = r"a.ppm")
# here, image option is used to 
# set image on button 
Button(top, text = 'Click Me !',bg = "lightgreen" ,image = photo).pack(side = TOP)

label = tkinter.Label(master = frame_a, text = """Autonomous Attendance System using Facial Recognisation\n Choose anyone of the  below actions:""", bg = "lightgreen", fg = 'red')
label['font'] = font.Font(family = "Times",size = 20)
label.grid(sticky = "news")

frame_fs = tkinter.Frame(top, width  = 1000, height = 25 )
frame_fs.pack()

frame = tkinter.Frame(top, width  = 1500, height = 100 , bg = "lightgreen")
frame.pack()
frame.columnconfigure(0,weight = 1 , minsize = 300)
frame.columnconfigure(1,weight = 1 , minsize = 300)
frame.columnconfigure(2,weight = 1 , minsize = 300)
frame.rowconfigure(0,weight = 1 , minsize = 100)

def create_dataset():
	print('creating Dataset5')
	os.system("python3 /home/sammy-ros/attendance_facial/create_dataset_gui.py")
	
def train_dataset():
	print('Training Dataset')
	os.system("""gnome-terminal -e "python3 /home/sammy-ros/attendance_facial/training.py" """)

def post_attendance():
	print('Posting Attendance')
	os.system("python3 /home/sammy-ros/attendance_facial/update_attendance_gui.py")

def update_unknown():
	#print('Posting Attendance')
	os.system("python3 /home/sammy-ros/attendance_facial/unknown_face_handling.py")


def view_attendance():
	print('Posting Attendance')
	os.system("""gnome-terminal -e " libreoffice /home/sammy-ros/attendance_facial/attendance.xlsx" """)


A = tkinter.Button(master = frame, text = 'Create\nDataset',cursor = "fleur",bg = "lightblue" , fg = "blue" ,command =  create_dataset )
B = tkinter.Button(master = frame, text = 'Training \nDataset',cursor = "fleur",bg = "lightblue" , fg = "blue",command =  train_dataset )
C = tkinter.Button(master = frame, text = 'Post\nAttendance',cursor = "fleur",bg = "lightblue" , fg = "blue", command =  post_attendance )
A['font'] = font.Font(size = 16)
B['font'] = font.Font(size = 16)
C['font'] = font.Font(size = 16)

A.grid(row=  0,column = 0, sticky = "nsew", padx = 25, pady = 15)
B.grid(row=  0,column = 1, sticky = "nsew", padx = 25, pady = 15)
C.grid(row=  0,column = 2, sticky = "nsew", padx = 25, pady = 15)


frame_l = tkinter.Frame(top, width  = 1500, height = 100 , bg = "lightgreen")
frame_l.pack()

for x in range(2):
	frame_l.columnconfigure(x,weight = 1 , minsize = 450)
frame_l.rowconfigure(0,weight = 1 , minsize = 100)

D = tkinter.Button(master = frame_l, text = 'Update Unknown Faces',cursor = "fleur",bg = "lightblue" , fg = "blue", command =  update_unknown )
D['font'] = font.Font(size = 14)
D.grid(row=  0,column = 0, sticky = "nsew", padx = 25, pady = 15)

E = tkinter.Button(master = frame_l, text = 'View Attendance',cursor = "fleur",bg = "lightblue" , fg = "blue", command =  view_attendance )
E['font'] = font.Font(size = 14)
E.grid(row=  0,column = 1, sticky = "nsew", padx = 25, pady = 15)

frame_ls = tkinter.Frame(top, width  = 1000, height = 25 )
frame_ls.pack()

top.mainloop()