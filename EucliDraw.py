import os
import sys
import tempfile
import tkinter as tk
import smtplib
from math import pi
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Menu
from tkinter import simpledialog
from tkinter import messagebox
from turtle import RawTurtle, ScrolledCanvas
from cryptography.fernet import Fernet

#Turtle's Actions and Shapes
def clear_canvas():
    t.clear()
def hide_turtle():
    t.hideturtle()
def show_turtle():
    t.showturtle()
def shape_circle():
    t.shape("circle")
def shape_arrow():
    t.shape("arrow")
def shape_triangle():
    t.shape("triangle")
def shape_square():
    t.shape("square")
def shape_turtle():
    t.shape("turtle")
def shape_classic():
    t.shape("classic")
def main():
    user_input()
    t.seth(0)
    t.home()
    proceed = not (user_choice or user_choice_e or user_choice_t)
    if proceed:
        shape_loop()
        t.seth(0)
        t.home()
    return proceed

#Perform Cleanup Tasks
def perform_cleanup_tasks():
    with open("session_log.txt", "a") as f:
        f.write("User closed the app cleanly.\n")
    temp_dir = tempfile.gettempdir()
    temp_file = os.path.join(temp_dir, "euclidraw_tempfile.txt")
    if os.path.exists(temp_file):
        os.remove(temp_file)

#Close_Program
def close_program():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        try:
            perform_cleanup_tasks()
        except Exception as e:
            print(f"Cleanup error: {e}")
        finally:
            try:
                t.bye()
            except:
                pass
            root.destroy()

#Goodbye_Popup
def goodbye_popup():
    popup = tk.Toplevel()
    popup.title("Goodbye!")
    popup.geometry("500x100")
    
    label = tk.Label(popup, text="Thanks for using!", font=("Arial", 12))
    label.pack(pady=20)

    button_frame = tk.Frame(popup)
    button_frame.pack(pady=10, fill="x", padx=20)
    
    continue_btn = tk.Button(button_frame, text="Continue", command=popup.destroy)
    continue_btn.grid(row=0, column=0, sticky="ew", padx=10)

    exit_btn = tk.Button(button_frame, text="Exit", command=lambda: print("Exit clicked"))
    exit_btn.grid(row=0, column=1, sticky="ew", padx=10)

    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)

#Icon usage
if getattr(sys, 'frozen', False):
    base_path=sys._MEIPASS
else:
    base_path= os.path.dirname(os.path.abspath(__file__))
icon_path= os.path.join(base_path, "assets", "EucliDraw_logo.ico")

#Tkinter
root=tk.Tk()
root.title("EucliDraw")
root.iconbitmap(icon_path)
dialog_root= tk.Tk()
dialog_root.withdraw()
menu_bar=Menu(root)

#Turtle Canvas inside the Tkinter GUI
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill="both", expand=True)

turtle_canvas = ScrolledCanvas(canvas_frame)
turtle_canvas.pack(fill="both", expand=True)

t= RawTurtle(turtle_canvas)
t.speed(0)

#Clear Canvas
canvas_menu=Menu(menu_bar, tearoff=0)
canvas_menu.add_command(label="Clear Canvas", command=clear_canvas)
menu_bar.add_cascade(label="Canvas", menu=canvas_menu)

#Visibility of Pointer
pointer_visibility_menu=Menu(menu_bar, tearoff=0)
pointer_visibility_menu.add_command(label="Hide Pointer", command=hide_turtle)
pointer_visibility_menu.add_command(label="Show Pointer", command=show_turtle)
menu_bar.add_cascade(label="Visibility of Pointer", menu=pointer_visibility_menu)

#Appearance of Pointer
pointer_appearance_menu=Menu(menu_bar, tearoff=0)
pointer_appearance_menu.add_command(label="Classic", command=shape_classic)
pointer_appearance_menu.add_command(label="Circle", command=shape_circle)
pointer_appearance_menu.add_command(label="Arrow", command=shape_arrow)
pointer_appearance_menu.add_command(label="Triangle", command=shape_triangle)
pointer_appearance_menu.add_command(label="Square", command=shape_square)
pointer_appearance_menu.add_command(label="Turtle", command=shape_turtle)
menu_bar.add_cascade(label="Appearance of Pointer", menu=pointer_appearance_menu)

#Start
menu_bar.add_command(label="Start", command=main)

#Exit
menu_bar.add_command(label="Exit", command=close_program)

root.config(menu=menu_bar)

#Polygons

#Triangles

def equilateral_triangle():
    for i in range(3):
        t.seth(i*120)
        t.fd(100)
def right_angled_triangle():
    for i in range(3):
        t.seth(i*135)
        if i==0:
            t.fd(100)
        if i==1:
            t.fd(141.42)
        if i==2:
            t.fd(100)
def scalene_triangle():
    t.seth(135)
    t.fd(100)
    t.seth(345)
    t.fd(220)
    t.seth(185)
    t.fd(145)
def isosceles_triangle():
    t.seth(0)
    t.fd(180)
    t.seth(135)
    t.fd(130)
    t.seth(225)
    t.fd(130)
def obtuse_triangle():
    t.fd(200)
    t.seth(130)
    t.fd(260)
    t.seth(260)
    t.fd(204)
def isosceles_obtuse_triangle():
    t.fd(100)
    t.seth(30)
    t.fd(100)
    t.seth(195)
    t.fd(195)

#Quadrilaterals

def square():
    for i in range(4):
        t.seth(i*90)
        t.fd(100)
def rectangle():
    for i in range(4):
        angle=i*90
        t.seth(angle)
        if 0<=angle<90 or 180<=angle<270:
            t.fd(100)
        if 90<=angle<180 or 270<=angle<360:
            t.fd(50)
def rhombus():
    for i in range(4):
        t.seth(45+(i*90))
        t.fd(100)
def parallelogram():
    for i in range(4):
        angle=i*90
        if 90<=angle<180 or 270<=angle<360:
            t.seth(angle-15)
        else:
            t.seth(angle)
        t.fd(100)
def trapezium():
    t.seth(0)
    t.fd(140)
    t.seth(90+15)
    t.fd(100)
    t.seth(180)
    t.fd(90)
    t.seth(270-15)
    t.fd(100)
def kite():
    t.seth(48)
    t.fd(100)
    t.seth(125)
    t.fd(62.5)
    t.seth(215)
    t.fd(62.5)
    t.seth(280)
    t.fd(100)

#Polygons

def pentagon():
    for i in range(5):
        angle=360/5
        t.seth((i+1)*angle)
        t.fd(100)
def hexagon():
    for i in range(6):
        angle=360/6
        t.seth((i+1)*angle)
        t.fd(100)
def heptagon():
    for i in range(7):
        angle=360/7
        t.seth((i+1)*angle)
        t.fd(100)
def octagon():
    for i in range(8):
        angle=360/8
        t.seth((i+1)*angle)
        t.fd(100)
def nonagon():
    for i in range(9):
        angle=360/9
        t.seth((i+1)*angle)
        t.fd(100)
def decagon():
    for i in range(10):
        angle=360/10
        t.seth((i+1)*angle)
        t.fd(100)
def hendecagon():
    for i in range(11):
        angle=(360/11)
        t.seth((i+1)*angle)
        t.fd(50)
def dodecagon():
    for i in range(12):
        angle=360/12
        t.seth((i+1)*angle)
        t.fd(50)

#Irregular_Concave_polygons

def concave_quadrilateral():
    t.seth(45)
    t.fd(150)
    t.seth(315)
    t.fd(150)
    t.seth(160)
    t.fd(113)
    t.seth(200)
    t.fd(113)
def concave_pentagon():
    t.seth(90)
    t.fd(100)
    t.seth(180)
    t.fd(100)
    t.seth(225)
    t.fd(70)
    t.seth(315)
    t.fd(70)
    t.seth(360)
    t.fd(100)
def concave_hexagon():
    t.seth(90)
    t.fd(100)
    t.seth(30)
    t.fd(150)
    t.seth(315)
    t.fd(150)
    t.seth(270)
    t.fd(100)
    t.seth(135)
    t.fd(150)
    t.seth(210)
    t.fd(150)
def concave_heptagon():
    t.seth(90)
    t.fd(100)
    t.seth(45)
    t.fd(100)
    t.seth(345)
    t.fd(100)
    t.seth(235)
    t.fd(100)
    t.seth(305)
    t.fd(100)
    t.seth(215)
    t.fd(100)
    t.seth(138)
    t.fd(116)
def concave_octagon():
    t.seth(80)
    t.fd(100)
    t.seth(280)
    t.fd(100)
    t.seth(350)
    t.fd(100)
    t.seth(190)
    t.fd(100)
    t.seth(260)
    t.fd(100)
    t.seth(100)
    t.fd(100)
    t.seth(170)
    t.fd(100)
    t.seth(10)
    t.fd(100)
def concave_nonagon():
    t.seth(75)
    t.fd(80)
    t.seth(305)
    t.fd(100)
    t.seth(55)
    t.fd(100)
    t.seth(305)
    t.fd(80)
    t.seth(200)
    t.fd(100)
    t.seth(275)
    t.fd(100)
    t.seth(180)
    t.fd(50)
    t.seth(75)
    t.fd(100)
    t.seth(160)
    t.fd(78)
def concave_decagon():
    angle=0
    for i in range(10):
        t.seth(angle)
        t.fd(100)
        angle += 144

#Star_Polygons

def pentagram():
    n = 5
    step = 2
    angle = (360 * step) / n

    for i in range(n):
        t.seth(i * angle)
        t.fd(100)

def hexagram():
    radius = 100
    points = []
    for i in range(6):
        angle = 60 * i
        t.seth(angle)
        t.penup()
        t.goto(0, 0)
        t.fd(radius)
        points.append(t.pos())
        t.penup()
        t.goto(points[0])
        t.pendown()
        t.goto(points[2])
        t.goto(points[4])
        t.goto(points[0])
        t.penup()
        t.goto(points[1])
        t.pendown()
        t.goto(points[3])
        t.goto(points[5])
        t.goto(points[1])

def heptagram():
    n=7
    step=3
    angle = (360*step)/n
    for i in range(n):
        t.seth(i*angle)
        t.fd(100)
def octagram():
    n=8
    step=3
    angle = (360*step)/n
    for i in range(n):
        t.seth(i*angle)
        t.fd(100)
def nonagram():
    n=9
    step=5
    angle = (360*step)/n
    for i in range(9):
        t.seth(i*angle)
        t.fd(100)
def decagram():
    n=10
    step=7
    angle = (360*step)/n
    for i in range(n):
        t.seth(i*angle)
        t.fd(100)
def hendecagram():
    n=11
    step=2
    angle = (360*step)/n
    for i in range(n):
        t.seth(i*angle)
        t.fd(100)
def dodecagram():
    n=12
    step=5
    angle = (360*step)/n
    for i in range(n):
        t.seth(i*angle)
        t.fd(100)
def tridecagram():
    n=13
    step=5
    angle = (360*step)/n
    for i in range(n):
        t.seth(i*angle)
        t.fd(100)

#Curved_Shapes
#Circle

def circle(radius):
    for i in range(360):
        step=2*pi*radius/360
        t.seth(i)
        t.fd(step)
def semicircle():
    t.seth(0)
    t.fd(115)
    for i in range(90,271,1):
        t.seth(i)
        t.fd(1)
def heart():
    t.seth(45)
    t.fd(150)
    for i in range(90,271,1):
        t.seth(i)
        t.fd(1)
    for i in range(90,271,1):
        t.seth(i)
        t.fd(1)
    t.seth(319)
    t.fd(163)
def quatrefoil():
    for i in range(180):
        t.seth(i)
        t.fd(1)
    for i in range(90,270,1):
        t.seth(i)
        t.fd(1)
    for i in range(180,361,1):
        t.seth(i)
        t.fd(1)
    for i in range(270,450,1):
        t.seth(i)
        t.fd(1)
def sector_of_circle():
    t.seth(45)
    t.fd(50)
    for i in range(90,136,1):
        t.seth(i)
        t.fd(1)
    t.seth(256)
    t.fd(81)
def segment_of_circle():
    semicircle()
def annulus():
    t.circle(100)
    t.penup()
    t.seth(270)
    t.fd(5)
    t.seth(0)
    t.pendown()
    t.circle(105)

#Circle_input
def circle_input():
    circle_input=simpledialog.askstring("Enter the data:", "Enter the radius of the circle you want to draw")
    circle_radius=float(circle_input)
    circle(circle_radius)

#Ellipse
def vertical_ellipse():
    for i in range(360):
        t.seth(i)
        if 0<=i<35 or 145<=i<180 or 180<=i<215 or 325<=i<360:
            t.fd(1)
        if 35<=i<45 or 135<=i<145 or 215<=i<225 or 315<=i<325:
            t.fd(1.5)
        if 45<=i<60 or 120<=i<135 or 225<=i<240 or 300<=i<315:
            t.fd(2)
        if 60<=i<90 or 90<=i<120 or 240<=i<270 or 270<=i<300:
            t.fd(3)
def horizontal_ellipse():
    for i in range(90,451,1):
        t.seth(i)
        if 90<=i<125 or 235<=i<270 or 270<=i<305:
            t.fd(1)
        if 125<=i<135 or 225<=i<235 or 305<=i<315 or 405<=i<415:
            t.fd(1.5)
        if 135<=i<150 or 210<=i<225 or 315<=i<330 or 390<i<405:
            t.fd(2)
        if 150<=i<180 or 180<=i<210 or 330<=i<360 or 360<=i<390:
            t.fd(3)
        if 415<=i<450:
            t.fd(1.25)
#Miscellaneous
def swastika():
    t.seth(0)
    t.fd(100)
    t.seth(270)
    t.fd(200)
    t.seth(0)
    t.fd(100)
    t.seth(180)
    t.fd(100)
    t.seth(90)
    t.fd(100)
    t.seth(0)
    t.fd(100)
    t.seth(90)
    t.fd(100)
    t.seth(270)
    t.fd(100)
    t.seth(180)
    t.fd(200)
    t.seth(270)
    t.fd(100)

#User_Input
def user_input():
    global body, user_choice, user_choice_e, user_choice_t
    ask_text_input=simpledialog.askstring("Enter the name of the shape you want:","Which shape do you want me to draw?", parent=dialog_root)    
    if ask_text_input is None:
        user_choice=messagebox.askyesno("Cancelled", "You pressed Cancel. Do you want to stop drawing")
        if user_choice:
            goodbye_popup()
            return True
        else:
            return False
    elif ask_text_input is not None:
        user_choice=False

    text_input=ask_text_input.lower().strip().replace("_"," ").replace(",","").replace(".","").replace(" ", "")
    if text_input=="circle":
        circle_input()
    elif text_input=="equilateraltriangle" or text_input=="equilateral":
        equilateral_triangle()
    elif text_input=="square":
        square()
    elif text_input=="rectangle":
        rectangle()
    elif text_input=="rhombus":
        rhombus()
    elif text_input=="parallelogram":
        parallelogram()
    elif text_input=="trapezium":
        trapezium()
    elif text_input=="kite":
        kite()
    elif text_input=="pentagon" or text_input=="convexpentagon":
        pentagon()
    elif text_input=="hexagon" or text_input=="convexhexagon":
        hexagon()
    elif text_input=="heptagon" or text_input=="convexheptagon":
        heptagon()
    elif text_input=="octagon" or text_input=="convexoctagon":
        octagon()
    elif text_input=="nonagon" or text_input=="convexnonagon":
        nonagon()
    elif text_input=="decagon" or text_input=="convexdecagon":
        decagon()
    elif text_input=="rightangledtriangle" or text_input=="rightangletriangle" or text_input=="righttriangle":
        right_angled_triangle()
    elif text_input=="scalenetriangle":
        scalene_triangle()
    elif text_input=="isoscelestriangle":
        isosceles_triangle()
    elif text_input=="semicircle":
        semicircle()
    elif text_input=="isoscelesrightangledtriangle" or text_input=="isoscelesrightangletriangle" or text_input=="isoscelesrighttriangle":
        right_angled_triangle()
    elif text_input=="acutetriangle":
        equilateral_triangle()
    elif text_input=="isoscelesacutetriangle" or text_input=="acuteisoscelestriangle":
        isosceles_triangle()
    elif text_input=="scaleneacutetriangle" or text_input=="acutescalenetriangle":
        scalene_triangle()
    elif text_input=="obtusetriangle":
        obtuse_triangle()
    elif text_input=="scaleneobtusetriangle" or text_input=="obtusescalenetriangle":
        obtuse_triangle()
    elif text_input=="isoscelesobtusetriangle" or text_input=="obtuseisoscelestriangle":
        isosceles_obtuse_triangle()
    elif text_input=="verticalellipse":
        vertical_ellipse()
    elif text_input=="horizontalellipse":
        horizontal_ellipse()
    elif text_input=="ellipse":
        ask_ellipse_input=simpledialog.askstring("Enter the type of the ellipse:","Which kind of Ellipse you want me to draw.\nIs it vertical(Major axis:vertical &  Minor axis:horizontal) or horizontal(Major axis:horizontal & Minor axis:vertical)\nType Vertical for Vertical Ellipse or Horizontal for Horizontal Ellipse", parent=dialog_root)    
        if ask_ellipse_input is None:
            user_choice_e=messagebox.askyesno("Cancelled", "You pressed Cancel. Do you want to stop drawing")
            if user_choice_e:
                goodbye_popup()
                return True
            else:
                return False
        elif ask_ellipse_input is not None:
            user_choice_e= False

        ellipse_input=ask_ellipse_input.lower().strip().replace("_"," ").replace(",","").replace(".","").replace(" ", "")
        if ellipse_input=="vertical":
            vertical_ellipse()
        elif ellipse_input=="horizontal":
            horizontal_ellipse()
        else:
            messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
            body=f"Error in ellipse input: {ellipse_input}"
            send_shape_error_report_email()
    elif text_input=="triangle":
        ask_triangle_input=simpledialog.askstring("Enter the type of triangle:","Which kind of Triangle you want me to draw?/nEnter the type of triangle you wnat me to draw", parent=dialog_root)        
        if ask_triangle_input is None:
            user_choice_t=messagebox.askyesno("Cancelled", "You pressed Cancel. Do you want to stop drawing")
            if user_choice_t:
                goodbye_popup()
                return True
            else:
                return False
        elif ask_triangle_input is not None:
            user_choice_t= False

        triangle_input=ask_triangle_input.lower().strip().replace("_"," ").replace(",","").replace(".","").replace(" ", "")
        if triangle_input == "rightangledtriangle" or triangle_input == "rightangletriangle" or triangle_input == "righttriangle" or triangle_input=="rightangle" or triangle_input=="rightangled":
            right_angled_triangle()
        elif triangle_input == "scalenetriangle" or triangle_input=="scalene":
            scalene_triangle()
        elif triangle_input == "isoscelestriangle" or triangle_input=="isosceles":
            isosceles_triangle()
        elif triangle_input == "isoscelesrightangledtriangle" or triangle_input == "isoscelesrightangletriangle" or triangle_input == "isoscelesrighttriangle" or triangle_input=="isoscelesrightangle" or triangle_input=="isoscelesrightangled":
            right_angled_triangle()
        elif triangle_input == "acutetriangle" or triangle_input=="acute":
            equilateral_triangle()
        elif triangle_input == "isoscelesacutetriangle" or triangle_input == "acuteisoscelestriangle" or triangle_input=="isoscelesacute" or triangle_input=="acuteisosceles":
            isosceles_triangle()
        elif triangle_input == "scaleneacutetriangle" or triangle_input == "acutescalenetriangle" or triangle_input == "scaleneacute" or triangle_input == "acutescalene":
            scalene_triangle()
        elif triangle_input == "obtusetriangle" or triangle_input== "obtuse":
            obtuse_triangle()
        elif triangle_input == "scaleneobtusetriangle" or triangle_input == "obtusescalenetriangle" or triangle_input == "scaleneobtuse" or triangle_input == "obtusescalene":
            obtuse_triangle()
        elif triangle_input == "isoscelesobtusetriangle" or triangle_input == "obtuseisoscelestriangle" or triangle_input == "isoscelesobtuse" or triangle_input == "obtuseisosceles":
            isosceles_obtuse_triangle()
        elif triangle_input == "equilateraltriangle" or triangle_input == "equilateral":
            equilateral_triangle()
        else:
            messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
            body=f"Error in triangle input: {triangle_input}"
            send_shape_error_report_email()
    elif text_input=="hendecagon" or text_input=="convexhendecagon":
        hendecagon()
    elif text_input=="dodecagon" or text_input=="convexdodecagon":
        dodecagon()
    elif text_input=="concavequadrilateral" or text_input=="irregularquadrilateral":
        concave_quadrilateral()
    elif text_input=="concavepentagon" or text_input=="irregularpentagon":
        concave_pentagon()
    elif text_input=="concavehexagon" or text_input=="irregularhexagon":
        concave_hexagon()
    elif text_input=="concaveheptagon" or text_input=="irregularheptagon":
        concave_heptagon()
    elif text_input=="concaveoctagon" or text_input=="irregularoctagon":
        concave_octagon()
    elif text_input=="concavenonagon" or text_input=="irregularnonagon":
        concave_nonagon()
    elif text_input=="concavedecagon" or text_input=="irregulardecagon" or text_input=="star":
        concave_decagon()
    elif text_input=="swastika":
        swastika()
    elif text_input=="heart":
        heart()
    elif text_input=="quatrefoil":
        quatrefoil()
    elif text_input=="sectorofcircle":
        sector_of_circle()
    elif text_input=="segmentofcircle":
        segment_of_circle()
    elif text_input=="annulus":
        annulus()
    elif text_input=="pentagram":
        pentagram()
    elif text_input=="hexagram":
        hexagram()
    elif text_input=="heptagram":
        heptagram()
    elif text_input=="octagram":
        octagram()
    elif text_input=="nonagram":
        nonagram()
    elif text_input=="decagram":
        decagram()
    elif text_input=="hendecagram":
        hendecagram()
    elif text_input=="dodecagram":
        dodecagram()
    elif text_input=="tridecagram":
        tridecagram()
    else:
        messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
        body=f"Error in text input: {text_input}"
        send_shape_error_report_email()

#Loop
def shape_loop():
    while True:
        ask_txtloop_input=simpledialog.askstring("Enter the name of the shape you want:","What do you want me to draw next?", parent=dialog_root)
        txtloop_input=ask_txtloop_input.lower().strip().replace("_"," ").replace(",","").replace(".","").replace(" ", "")
        global body
        if ask_txtloop_input is None:
            user_choice_l=messagebox.askyesno("Cancelled", "You pressed Cancel. Do you want to stop drawing")
            if user_choice_l:
                goodbye_popup()
                break
            else:
                continue
        if txtloop_input=="circle":
            circle_input()
        elif txtloop_input=="equilateraltriangle":
            equilateral_triangle()
        elif txtloop_input=="square":
            square()
        elif txtloop_input=="rectangle":
            rectangle()
        elif txtloop_input=="rhombus":
            rhombus()
        elif txtloop_input=="parallelogram":
            parallelogram()
        elif txtloop_input=="trapezium":
            trapezium()
        elif txtloop_input=="kite":
            kite()
        elif txtloop_input=="pentagon":
            pentagon()
        elif txtloop_input=="hexagon":
            hexagon()
        elif txtloop_input=="heptagon":
            heptagon()
        elif txtloop_input=="octagon":
            octagon()
        elif txtloop_input=="nonagon":
            nonagon()
        elif txtloop_input=="decagon":
            decagon()
        elif txtloop_input=="rightangledtriangle" or txtloop_input=="rightangletriangle":
            right_angled_triangle()
        elif txtloop_input=="scalenetriangle":
            scalene_triangle()
        elif txtloop_input=="isoscelestriangle":
            isosceles_triangle()
        elif txtloop_input=="semicircle":
            semicircle()
        elif txtloop_input=="isoscelesrightangledtriangle" or txtloop_input=="isoscelesrightangletriangle" or txtloop_input=="isoscelesrighttriangle":
            right_angled_triangle()
        elif txtloop_input=="acutetriangle":
            equilateral_triangle()
        elif txtloop_input=="isoscelesacutetriangle" or txtloop_input=="acuteisoscelestriangle":
            isosceles_triangle()
        elif txtloop_input=="scaleneacutetriangle" or txtloop_input=="acutescalenetriangle":
            scalene_triangle()
        elif txtloop_input=="obtusetriangle":
            obtuse_triangle()
        elif txtloop_input=="scaleneobtusetriangle" or txtloop_input=="obtusescalenetriangle":
            obtuse_triangle()
        elif txtloop_input=="isoscelesobtusetriangle" or txtloop_input=="obtuseisoscelestriangle":
            isosceles_obtuse_triangle()
        elif txtloop_input=="verticalellipse":
            vertical_ellipse()
        elif txtloop_input=="horizontalellipse":
            horizontal_ellipse()
        elif txtloop_input=="ellipse":
            ask_ellipse_input=simpledialog.askstring("Enter the type of the ellipse:","Which kind of Ellipse you want me to draw.\nIs it vertical(Major axis:vertical &  Minor axis:horizontal) or horizontal(Major axis:horizontal & Minor axis:vertical)\nType Vertical for Vertical Ellipse or Horizontal for Horizontal Ellipse", parent=dialog_root)
            ellipse_input=ask_ellipse_input.lower().strip().replace("_"," ").replace(",","").replace(".","").replace(" ", "")

            if ask_ellipse_input is None:
                user_choice_le=messagebox.askyesno("Cancelled", "You pressed Cancel. Do you want to stop drawing")
                if user_choice_le:
                    goodbye_popup()
                    break
                else:
                    continue

            if ellipse_input=="vertical":
                vertical_ellipse()
            elif ellipse_input=="horizontal":
                horizontal_ellipse()
            else:
                messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
                body=f"Error in ellipse input: {ellipse_input}"
                send_shape_error_report_email()
        elif txtloop_input=="triangle":
            ask_triangle_input=simpledialog.askstring("Enter the type of triangle:","Which kind of Triangle you want me to draw?\nEnter the type of triangle you want me to draw", parent=dialog_root)
            triangle_input=ask_triangle_input.lower().strip().replace("_"," ").replace(",","").replace(".","").replace(" ", "")

            if ask_txtloop_input is None:
                user_choice_lt=messagebox.askyesno("Cancelled", "You pressed Cancel. Do you want to stop drawing")
                if user_choice_lt:
                    goodbye_popup()
                    break
                else:
                    continue

            if triangle_input == "rightangledtriangle" or triangle_input == "rightangletriangle" or triangle_input == "righttriangle" or triangle_input == "rightangled" or triangle_input == "rightangle":
                right_angled_triangle()
            elif triangle_input == "scalenetriangle" or triangle_input=="scalene":
                scalene_triangle()
            elif triangle_input == "isoscelestriangle" or triangle_input=="isosceles":
                isosceles_triangle()
            elif triangle_input == "isoscelesrightangledtriangle" or triangle_input == "isoscelesrightangletriangle" or triangle_input == "isoscelesrighttriangle" or triangle_input == "isoscelesrightangled" or triangle_input == "isoscelesrightangle" or triangle_input == "isoscelesright":
                right_angled_triangle()
            elif triangle_input == "acutetriangle" or triangle_input=="acute":
                equilateral_triangle()
            elif triangle_input == "isoscelesacutetriangle" or triangle_input == "acuteisoscelestriangle" or triangle_input == "isoscelesacute" or triangle_input == "acuteisosceles":
                isosceles_triangle()
            elif triangle_input == "scaleneacutetriangle" or triangle_input == "acutescalenetriangle" or triangle_input == "scaleneacute" or triangle_input == "acutescalene":
                scalene_triangle()
            elif triangle_input == "obtusetriangle" or triangle_input=="obtuse":
                obtuse_triangle()
            elif triangle_input == "scaleneobtusetriangle" or triangle_input == "obtusescalenetriangle" or triangle_input == "scaleneobtuse" or triangle_input == "obtusescalene":
                obtuse_triangle()
            elif triangle_input == "isoscelesobtusetriangle" or triangle_input == "obtuseisoscelestriangle" or triangle_input == "isoscelesobtuse" or triangle_input == "obtuseisosceles":
                isosceles_obtuse_triangle()
            elif triangle_input == "equilateraltriangle" or triangle_input=="equilateral":
                equilateral_triangle()
            else:
                messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
                body=f"Error in triangle input: {triangle_input}"
                send_shape_error_report_email()
        elif txtloop_input=="hendecagon":
            hendecagon()
        elif txtloop_input=="dodecagon":
            dodecagon()
        elif txtloop_input=="concavequadrilateral" or txtloop_input=="irregularquadrilateral":
            concave_quadrilateral()
        elif txtloop_input=="concavepentagon" or txtloop_input=="irregularpentagon":
            concave_pentagon()
        elif txtloop_input=="concavehexagon" or txtloop_input=="irregularhexagon":
            concave_hexagon()
        elif txtloop_input=="concaveheptagon" or txtloop_input=="irregularheptagon":
            concave_heptagon()
        elif txtloop_input=="concaveoctagon" or txtloop_input=="irregularoctagon":
            concave_octagon()
        elif txtloop_input=="concavenonagon" or txtloop_input=="irregularnonagon":
            concave_nonagon()
        elif txtloop_input=="concavedecagon" or txtloop_input=="irregulardecagon" or txtloop_input=="star":
            concave_decagon()
        elif txtloop_input=="swastika" or txtloop_input=="nazi":
            swastika()
        elif txtloop_input=="heart":
            heart()
        elif txtloop_input=="quatrefoil":
            quatrefoil()
        elif txtloop_input=="sectorofcircle":
            sector_of_circle()
        elif txtloop_input=="segmentofcircle":
            segment_of_circle()
        elif txtloop_input=="annulus":
            annulus()
        elif txtloop_input=="pentagram":
            pentagram()
        elif txtloop_input=="hexagram":
            hexagram()
        elif txtloop_input=="heptagram":
            heptagram()
        elif txtloop_input=="octagram":
            octagram()
        elif txtloop_input=="nonagram":
            nonagram()
        elif txtloop_input=="decagram":
            decagram()
        elif txtloop_input=="hendecagram":
            hendecagram()
        elif txtloop_input=="dodecagram":
            dodecagram()
        elif txtloop_input=="tridecagram":
            tridecagram()
        else:
            messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
            body=f"Error in text loop input: {txtloop_input}"
            send_shape_error_report_email()
        t.seth(0)

        again =messagebox.askyesno("Choose one of the option:","Do you want me to draw more? Yes or No")
        if again:
            continue
        else:
            goodbye_popup()
            break


#Shape_Error_Report

def send_shape_error_report_email():

    #Encryption_of_data

    with open("EucliDraw_Lock/key.key", "rb") as key_file:
        key = key_file.read()

    fernet = Fernet(key)

    with open("EucliDraw_Lock/pass.bin", "rb") as encrypted_file_pass:
        encrypted_password = encrypted_file_pass.read()

    app_password = fernet.decrypt(encrypted_password).decode()

    with open("EucliDraw_Lock/sender.bin", "rb") as encrypted_file_sender:
        encrypted_sender = encrypted_file_sender.read()

    sender = fernet.decrypt(encrypted_sender).decode()
    
    with open("EucliDraw_Lock/receiver.bin", "rb") as encrypted_file_receiver:
        encrypted_receiver = encrypted_file_receiver.read()

    receiver = fernet.decrypt(encrypted_receiver).decode()

    #Error_report_email
    
    sender_email = sender + "@gmail.com"
    receiver_email = receiver + "@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Error Report"

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)

def run_tk():
    root.mainloop()

run_tk()
