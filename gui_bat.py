from Tkinter import*
import time
import sys
import cv2
import Image, ImageTk
i = 5


def quit_func():
    sys.exit()


def update():
    global i                          #To update values for batttery Capacity,Current,Voltage
    i = i+3
    vol_var.set(i)
    top.update()
    time.sleep(0.2)
    #top.after(100,update)


def show_cam():
    cv2.namedWindow("preview")
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


                              # exit



top = Tk(className = " AGV Specifications")
top.configure(bg = "light blue")
vol_var = IntVar()
cur_var = IntVar()
cap_var = IntVar()

def show_map():

    MAP  = Toplevel()

    def start_pos():
        MAP.quit()
    def end_pos():
        MAP.quit()
    def close_window():
        print "Window closed"
        MAP.destroy()


    PhotoImage(master = MAP, width = 500, height = 700)
    canvas = Canvas(MAP,width = 450,height = 670)
    canvas.grid(row=0, column=0,sticky=N+S+E+W)
    File = '/home/paresh/Pictures/map.jpeg'
    img = ImageTk.PhotoImage(Image.open(File))
    canvas.create_image(0,0,image=img,anchor="nw")
    #canvas.config(scrollregion=canvas.bbox(ALL))
    start = Button(MAP,text = "Starting Point",font = ('TimeRomans',10,'bold'),bg = "magenta")
    finish = Button(MAP,text = "Ending Point",font = ('TimeRomans',10,'bold'),bg = "magenta")

    start.grid(row = 0,column= 2)
    finish.grid(row = 0, column = 3)
    MAP.protocol("WM_DELETE_WINDOW", close_window)

    start.configure(command = start_pos)
    finish.configure(command = end_pos)



    def printcoords(edvent):
        #outputting x and y coords to console
        print (edvent.x,edvent.y)
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)
    top.mainloop()
    MAP.mainloop()



cur_var.set(i)
vol_var.set(i)
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

#top.after(100, update)
#MAP.mainloop()
top.mainloop()
