import os
import sys
import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import Menu
from tkinter import simpledialog
from tkinter import messagebox
from turtle import RawTurtle, ScrolledCanvas

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
    shape_loop()

#Icon usage
if getattr(sys, 'frozen', False):
    base_path=sys._MEIPASS
else:
    base_path=base_path = os.path.dirname(os.path.abspath(__file__))
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

menu_bar.add_command(label="Start", command=main)

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
    for i in range(5):
        t.seth(angle)
        t.fd(100)
        angle += 144
#Curved_Shapes
#Circle

def circle():
    for i in range(360):
        t.seth(i)
        t.fd(1)
def semicircle():
    t.seth(0)
    t.fd(115)
    for i in range(90,271,1):
        t.seth(i)
        t.fd(1)

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
#User_Input
def user_input():
    text_input=simpledialog.askstring("Enter the name of the shape you want:","Which shape do you want me to draw?", parent=dialog_root).lower().strip().replace("_"," ").replace(",","").replace(".","")
    global body
    if text_input=="circle":
        circle()
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
        ellipse_input=simpledialog.askstring("Enter the type of the ellipse:","Which kind of Ellipse you want me to draw.\nIs it vertical(Major axis:vertical &  Minor axis:horizontal) or horizontal(Major axis:horizontal & Minor axis:vertical)\nType Vertical for Vertical Ellipse or Horizontal for Horizontal Ellipse", parent=dialog_root).lower().strip().replace("_"," ").replace(",","").replace(".","")
        if ellipse_input=="vertical":
            vertical_ellipse()
        elif ellipse_input=="horizontal":
            horizontal_ellipse()
        else:
            messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
            body=f"Error in ellipse input: {ellipse_input}"
            send_shape_error_report_email()
    elif text_input=="triangle":
        triangle_input=simpledialog.askstring("Enter the type of triangle:","Which kind of Triangle you want me to draw?/nEnter the type of triangle you wnat me to draw", parent=dialog_root).lower().strip().replace("_"," ").replace(",","").replace(".","")
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
        convave_hexagon()
    elif text_input=="concaveheptagon" or text_input=="irregularheptagon":
        concave_heptagon()
    elif text_input=="concaveoctagon" or text_input=="irregularoctagon":
        concave_octagon()
    elif text_input=="concavenonagon" or text_input=="irregularnonagon":
        concave_nonagon()
    elif text_input=="concavedecagon" or text_input=="irregulardecagon" or text_input=="star":
        concave_decagon()
    else:
        messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
        body=f"Error in text input: {text_input}"
        send_shape_error_report_email()
#Close_Program
def close_program():
    root.destroy()

#Goodbye_Popup
def goodbye_popup():
    popup = tk.Toplevel()
    popup.title("Goodbye! ❤️")
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


#Loop
def shape_loop():
    while True:
        screen=t.getscreen()
        txtloop_input=simpledialog.askstring("Enter the name of the shape you want:","What do you want me to draw next?", parent=dialog_root).lower().strip().replace("_"," ").replace(",","").replace(".","")
        global body
        if txtloop_input=="circle":
            circle()
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
            ellipse_input=simpledialog.askstring("Enter the type of the ellipse:","Which kind of Ellipse do you want me to draw?/nIs it vertical (Major axis: vertical & Minor axis: horizontal) or horizontal(Major axis: horizontal & Minor axis: vertical)?/nType 'vertical' for Vertical Ellipse or 'horizontal' for Horizontal Ellipse: ", parent=dialog_root).lower().strip().replace("_"," ").replace(",","").replace(".","")

            if ellipse_input=="vertical":
                vertical_ellipse()
            elif ellipse_input=="horizontal":
                horizontal_ellipse()
            else:
                messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
                body=f"Error in ellipse input: {ellipse_input}"
                send_shape_error_report_email()
        elif txtloop_input=="triangle":
            triangle_input=simpledialog.askstring("Enter the type of triangle:","Which kind of Triangle do you want me to draw?\nEnter the type: ", parent=dialog_root).lower().strip().replace("_"," ").replace(",","").replace(".","")
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
            convave_hexagon()
        elif txtloop_input=="concaveheptagon" or txtloop_input=="irregularheptagon":
            concave_heptagon()
        elif txtloop_input=="concaveoctagon" or txtloop_input=="irregularoctagon":
            concave_octagon()
        elif txtloop_input=="concavenonagon" or txtloop_input=="irregularnonagon":
            concave_nonagon()
         elif txtloop_input=="concavedecagon" or txtloop_input=="irregulardecagon" or txtloop_input=="star":
            concave_decagon()
        
        else:
            messagebox.showerror("Invalid Input", "Sorry,I cannot draw it")
            body=f"Error in text loop input: {txtloop_input}"
            send_shape_error_report_email()


        again =simpledialog.askstring("Enter one of the option:","Do you want me to draw more? Yes or No", parent=dialog_root).lower().strip().replace("_"," ").replace(",","").replace(".","")
        if again == "yes":
            continue
        elif again == "no":
             goodbye_popup()
             break
        else:
            messagebox.showerror("Invalid Input", "Sorry,I do not get it")


#Shape_Error_Report
def send_shape_error_report_email():
    sender_email = "xxxxxxxx@gmail.com"
    reciever_email = "xxxxxx@gmail.com"
    password = "xxxx xxxx xxxx xxxx"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = reciever_email
    msg["Subject"] = "Error Report"

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)


def run_tk():
    root.mainloop()

run_tk()
