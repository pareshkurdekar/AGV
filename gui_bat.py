from Tkinter import*
import time
import sys
import cv2
import Image, ImageTk
import os
import serial
#ser = serial.Serial('/dev/ttyACM0') # Arduino

i = 5
x = 3

def quit_func():
    sys.exit()


def update_vol_var():
    global i                          #To update values for batttery Capacity,Current,Voltage
    i = i+3
    vol_var.set(i)
    top.update()
    time.sleep(0.2)
    top.after(2000, update_vol_var)



def update_cur_var():
    global i                          #To update values for batttery Capacity,Current,Voltage
    i = i+3
    cur_var.set(i)
    top.update()
    time.sleep(0.2)
    top.after(3000, update_cur_var)


def update_cap_var():
    global i                          #To update values for batttery Capacity,Current,Voltage
    i = i+3
    cap_var.set(i)
    top.update()
    time.sleep(0.2)
    top.after(5000, update_cap_var)



def show_cam():
    os.system("python /home/paresh/Atom/rasplapcam.py")
'''    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened():                      # Live Feed
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    cv2.destroyWindow("preview")
    vc.release()


    '''                          # exit



top = Tk(className = " AGV Specifications")
top.configure(bg = "light blue")
vol_var = IntVar()
cur_var = IntVar()
cap_var = IntVar()
l4 = []

def show_map():


    MAP  = Toplevel()
    f1 = Frame(MAP)
    f2 = Frame(MAP)
    f1.pack(side = LEFT)
    f2.pack(side = LEFT)
    start_coord = StringVar()
    start_coord.set("                      ")

    end_coord = StringVar()
    end_coord.set("                     ")

    def start_pos():
        global x
        x = 0
        print(x)
    def end_pos():
        global x
        x = 1
        print(x)
    def close_window():
        print "Window closed"
        MAP.destroy()

    def send_data():
        print("Will send data")
        print(l4)
        coordinate_ard = ",".join(l4)
        print(coordinate_ard)
#        ser.write(coordinate_ard)

        #MAP.destroy( )

    PhotoImage(master = f1, width = 500, height = 700)
    canvas = Canvas(f1,width = 450,height = 670)
    canvas.grid(row=0, column=0,sticky=N+S+E+W)
    File = '/home/paresh/Pictures/map.jpeg'
    img = ImageTk.PhotoImage(Image.open(File))
    canvas.create_image(0,0,image=img,anchor="nw")
    #canvas.config(scrollregion=canvas.bbox(ALL))

    start = Button(f2,text = "Starting Point",font = ('TimeRomans',10,'bold'),bg = "yellow")
    finish = Button(f2,text = "Ending Point",font = ('TimeRomans',10,'bold'),bg = "yellow")
    send = Button(f2,text = "Send data",font = ('TimeRomans',15,'bold'),bg = "green")

    start_coord_label = Label(f2,textvariable = start_coord, font = ('TimeRomans',10,'bold'),bg = "yellow")
    end_coord_label = Label(f2,textvariable = end_coord, font = ('TimeRomans',10,'bold'),bg = "yellow")


    start.grid(row = 0,column= 2,sticky = W+E+N+S)
    finish.grid(row = 1, column = 2,sticky = W+E+N+S)
    start_coord_label.grid(row = 0, column = 3,sticky = W+E+N+S)
    end_coord_label.grid(row = 1, column = 3,sticky = W+E+N+S)
    send.grid(row = 5, column = 4,sticky = W+E+N+S)
    #MAP.protocol("WM_DELETE_WINDOW", close_window)

    start.configure(command = start_pos)
    finish.configure(command = end_pos)
    send.configure(command = send_data)


    def printcoords(event):
        #outputting x and y coords to console
        global x
        global l4
        print (event.x,event.y)
        l = []
        l2 = []
        l3 = []
        l.append(str(event.x))
        l.append(str(event.y))
        #print(type(event.x))
        print(l)
        coord = ",".join(l)
        print(coord)
        if x == 0:
            start_coord.set(coord)
            l2 = l[:]
            l4 = l2[:]
            x = 3
        if x == 1:
            l3 = l[:]
            x = 3
            l4 = l4 + l3
            end_coord.set(coord)


    canvas.bind("<Button 1>",printcoords)
    MAP.mainloop()



cur_var.set(i)
vol_var.set(i)
cap_var.set(i)
top.grid_columnconfigure(2, minsize=100)
top.grid_rowconfigure(2, minsize=20)  # Here
bat_vol = Label(top,text = "Battery Voltage",font = ('TimeRomans',20,'bold'),bg = "light pink")
bat_cur = Label(top,text = "Battery Current",font = ('TimeRomans',20,'bold'),bg = "light pink")
bat_cap = Label(top,text = "Battery Capacity",font = ('TimeRomans',20,'bold'),bg = "light pink")
camera = Label(top,text = "Camera",font = ('TimeRomans',20,'bold'),bg = "light pink")
title = Label(top,text = "AGV SPECIFICATIONS",font = ('TimeRomans',30,'bold'),bg = "light green")
map = Label(top,text = "Map",font = ('TimeRomans',20,'bold'),bg = "light pink")

vol = Label(top,textvariable = vol_var,font = ('TimeRomans',20,'bold'),bg = "orange")
cur = Label(top,textvariable = cur_var,font = ('TimeRomans',20,'bold'),bg = "orange")
cap = Label(top,textvariable = cap_var,font = ('TimeRomans',20,'bold'),bg = "orange")

map_loc = Button(top,textvariable = "Location",font = ('TimeRomans',20,'bold'),bg = "orange")
q = Button(top,text = "Quit",font = ('TimeRomans',20,'bold'),bg = "red")
cam = Button(top,text = "Live Feed",font = ('TimeRomans',20,'bold'),bg = "orange")

title.grid(row = 0,column = 1,sticky = N)
bat_cur.grid(row = 1,column = 0,sticky = W+E)
bat_vol.grid(row = 2,column = 0,sticky = W+E)
bat_cap.grid(row = 3,column = 0,sticky = W+E)
camera.grid(row = 4,column = 0,sticky = W+E+N+S)
map.grid(row = 5,column=0,sticky = W+E+N+S)
q.grid(row = 6,column = 3)


q.configure(command = quit_func)
cam.configure(command = show_cam)
map_loc.configure(command = show_map)

cur.grid(row = 1,column = 1,sticky = W+E)
vol.grid(row = 2,column = 1,sticky = W+E)
cap.grid(row = 3,column = 1,sticky = W+E)
cam.grid(row = 4,column = 1,sticky = W+E)
map_loc.grid(row = 5,column = 1,sticky = W+E)

top.after(2000, update_vol_var)
top.after(3000, update_cur_var)
top.after(5000, update_cap_var)

top.mainloop()
