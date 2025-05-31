# EucliDraw
from turtle import*
speed(0)
def equilateral_triangle():
    for i in range(3):
        seth(i*120)
        fd(100)
def square():
    for i in range(4):
        seth(i*90)
        fd(100)
def rectangle():
    for i in range(4):
        angle=i*90
        seth(angle)
        if 0<=angle<90 or 180<=angle<270:
            fd(100)
        if 90<=angle<180 or 270<=angle<360:
            fd(50)
def rhombus():
    for i in range(4):
        seth(45+(i*90))
        fd(100)
def parallelogram():
    for i in range(4):
        angle=i*90
        if 90<=angle<180 or 270<=angle<360:
            seth(angle-15)
        else:
            seth(angle)
        fd(100)
def trapezium():
    seth(0)
    fd(140)
    seth(90+15)
    fd(100)
    seth(180)
    fd(90)
    seth(270-15)
    fd(100)
def kite():
    seth(48)
    fd(100)
    seth(125)
    fd(62.5)
    seth(215)
    fd(62.5)
    seth(280)
    fd(100)
def circle():
    for i in range(360):
        seth(i)
        fd(1)
def right_angled_triangle():
    for i in range(3):
        seth(i*135)
        if i==0:
            fd(100)
        if i==1:
            fd(141.42)
        if i==2:
            fd(100)
            
def pentagon():
    for i in range(5):
        angle=360/5
        seth((i+1)*angle)
        fd(100)
def hexagon():
    for i in range(6):
        angle=360/6
        seth((i+1)*angle)
        fd(100)
def heptagon():
    for i in range(7):
        angle=360/7
        seth((i+1)*angle)
        fd(100)
def octagon():
    for i in range(8):
        angle=360/8
        seth((i+1)*angle)
        fd(100)
def nonagon():
    for i in range(9):
        angle=360/9
        seth((i+1)*angle)
        fd(100)
def decagon():
    for i in range(10):
        angle=360/10
        seth((i+1)*angle)
        fd(100)
def hendecagon():
    for i in range(11):
        angle=(360/11)
        seth((i+1)*angle)
        fd(50)
def dodecagon():
    for i in range(12):
        angle=360/12
        seth((i+1)*angle)
        fd(50)
def scalene_triangle():
    seth(135)
    fd(100)
    seth(345)
    fd(220)
    seth(185)
    fd(145)
def isosceles_triangle():
    seth(0)
    fd(180)
    seth(135)
    fd(130)
    seth(225)
    fd(130)
def obtuse_triangle():
    fd(200)
    seth(130)
    fd(260)
    seth(260)
    fd(204)
def isosceles_obtuse_triangle():
    fd(100)
    seth(30)
    fd(100)
    seth(195)
    fd(195)  
def semicircle():
    seth(0)
    fd(115)
    for i in range(90,271,1):
        seth(i)
        fd(1)
def vertical_ellipse():
    for i in range(360):
        seth(i)
        if 0<=i<35 or 145<=i<180 or 180<=i<215 or 325<=i<360:
            fd(1)
        if 35<=i<45 or 135<=i<145 or 215<=i<225 or 315<=i<325:
            fd(1.5)
        if 45<=i<60 or 120<=i<135 or 225<=i<240 or 300<=i<315:
            fd(2)
        if 60<=i<90 or 90<=i<120 or 240<=i<270 or 270<=i<300:
            fd(3)
def horizontal_ellipse():
    for i in range(90,451,1):
        seth(i)
        if 90<=i<125 or 235<=i<270 or 270<=i<305:
            fd(1)
        if 125<=i<135 or 225<=i<235 or 305<=i<315 or 405<=i<415:
            fd(1.5)
        if 135<=i<150 or 210<=i<225 or 315<=i<330 or 390<i<405:
            fd(2)
        if 150<=i<180 or 180<=i<210 or 330<=i<360 or 360<=i<390:
            fd(3)
        if 415<=i<450:
            fd(1.25)
def user_input():
    text_input=input("Which shape do you want me to draw?").lower().strip().replace("_"," ").replace(",","").replace(".","")
    if text_input=="circle":
        circle()
    if text_input=="equilateraltriangle":
        equilateral_triangle()
    if text_input=="square":
        square()
    if text_input=="rectangle":
        rectangle()
    if text_input=="rhombus":
        rhombus()
    if text_input=="parallelogram":
        parallelogram()
    if text_input=="trapezium":
        trapezium()
    if text_input=="kite":
        kite()
    if text_input=="pentagon":
        pentagon()
    if text_input=="hexagon":
        hexagon()
    if text_input=="heptagon":
        heptagon()
    if text_input=="octagon":
        octagon()
    if text_input=="nonagon":
        nonagon()
    if text_input=="decagon":
        decagon()
    if text_input=="rightangledtriangle" or text_input=="rightangletriangle" or text_input=="righttriangle":
        right_angled_triangle()
    if text_input=="scalenetriangle":
        scalene_triangle()
    if text_input=="isoscelestriangle":
        isosceles_triangle()
    if text_input=="semicircle":
        semicircle()
    if text_input=="isoscelesrightangledtriangle" or text_input=="isoscelesrightangletriangle" or text_input=="isoscelesrighttriangle":
        right_angled_triangle()
    if text_input=="acutetriangle":
        equilateral_triangle()
    if text_input=="isoscelesacutetriangle" or text_input=="acuteisoscelestriangle":
        isosceles_triangle()
    if text_input=="scaleneacutetriangle" or text_input=="acutescalenetriangle":
        scalene_triangle()
    if text_input=="obtusetriangle":
        obtuse_triangle()
    if text_input=="scaleneobtusetriangle" or text_input=="obtusescalenetriangle":
        obtuse_triangle()
    if text_input=="isoscelesobtusetriangle" or text_input=="obtuseisoscelestriangle":
        isosceles_obtuse_triangle()
    if text_input=="verticalellipse":
        vertical_ellipse()
    if text_input=="horizontalellipse":
        horizontal_ellipse()
    if text_input=="ellipse":
        ellipse_input=input("Which kind of Ellipse you want me to draw."
                            "Is it vertical(Major axis:vertical &  Minor axis:horizontal) or horizontal(Major axis:horizontal & Minor axis:vertical)"
                            "Type Vertical for Vertical Ellipse or Horizontal for Horizontal Ellipse").lower().strip().replace("_"," ").replace(",","").replace(".","")
        if ellipse_input=="vertical":
            vertical_ellipse()
        if ellipse_input=="horizontal":
            horizontal_ellipse()
        else:
            print("Sorry,I cannot draw it")
    if text_input=="triangle":
        triangle_input=input("Which kind of Triangle you want me to draw?"
                             "Enter the type of triangle you wnat me to draw")
        if triangle_input == "rightangledtriangle" or triangle_input == "rightangletriangle" or triangle_input == "righttriangle":
            right_angled_triangle()
        if triangle_input == "scalenetriangle":
            scalene_triangle()
        if triangle_input == "isoscelestriangle":
            isosceles_triangle()
        if triangle_input == "isoscelesrightangledtriangle" or triangle_input == "isoscelesrightangletriangle" or triangle_input == "isoscelesrighttriangle":
            right_angled_triangle()
        if triangle_input == "acutetriangle":
            equilateral_triangle()
        if triangle_input == "isoscelesacutetriangle" or triangle_input == "acuteisoscelestriangle":
            isosceles_triangle()
        if triangle_input == "scaleneacutetriangle" or triangle_input == "acutescalenetriangle":
            scalene_triangle()
        if triangle_input == "obtusetriangle":
            obtuse_triangle()
        if triangle_input == "scaleneobtusetriangle" or triangle_input == "obtusescalenetriangle":
            obtuse_triangle()
        if triangle_input == "isoscelesobtusetriangle" or triangle_input == "obtuseisoscelestriangle":
            isosceles_obtuse_triangle()
        if triangle_input == "equilateraltriangle":
            equilateral_triangle()
        else:
            print("Sorry,I cannot draw it")
    if text_input=="hendecagon":
        hendecagon()
    if text_input=="dodecagon":
        dodecagon()
    else:
        print("Sorry,I cannot draw it")
user_input()

while True:
    txtloop_input=input("What do you want me to draw next?").lower().strip().replace("_"," ").replace(",","").replace(".","")
    if txtloop_input=="circle":
        circle()
    if txtloop_input=="equilateraltriangle":
        equilateral_triangle()
    if txtloop_input=="square":
        square()
    if txtloop_input=="rectangle":
        rectangle()
    if txtloop_input=="rhombus":
        rhombus()
    if txtloop_input=="parallelogram":
        parallelogram()
    if txtloop_input=="trapezium":
        trapezium()
    if txtloop_input=="kite":
        kite()
    if txtloop_input=="pentagon":
        pentagon()
    if txtloop_input=="hexagon":
        hexagon()
    if txtloop_input=="heptagon":
        heptagon()
    if txtloop_input=="octagon":
        octagon()
    if txtloop_input=="nonagon":
        nonagon()
    if txtloop_input=="decagon":
        decagon()
    if txtloop_input=="rightangledtriangle" or txtloop_input=="rightangletriangle" or txtloop_input=="righttriangle":
        right_angled_triangle()
    if txtloop_input=="scalenetriangle":
        scalene_triangle()
    if txtloop_input=="isoscelestriangle":
        isosceles_triangle()
    if txtloop_input=="semicircle":
        semicircle()
    if txtloop_input=="isoscelesrightangledtriangle" or txtloop_input=="isoscelesrightangletriangle" or txtloop_input=="isoscelesrighttriangle":
        right_angled_triangle()
    if txtloop_input=="acutetriangle":
        equilateral_triangle()
    if txtloop_input=="isoscelesacutetriangle" or txtloop_input=="acuteisoscelestriangle":
        isosceles_triangle()
    if txtloop_input=="scaleneacutetriangle" or txtloop_input=="acutescalenetriangle":
        scalene_triangle()
    if txtloop_input=="obtusetriangle":
        obtuse_triangle()
    if txtloop_input=="scaleneobtusetriangle" or txtloop_input=="obtusescalenetriangle":
        obtuse_triangle()
    if txtloop_input=="isoscelesobtusetriangle" or txtloop_input=="obtuseisoscelestriangle":
        isosceles_obtuse_triangle()
    if txtloop_input=="verticalellipse":
        vertical_ellipse()
    if txtloop_input=="horizontalellipse":
        horizontal_ellipse()
    if txtloop_input=="ellipse":
        ellipse_input=input("Which kind of Ellipse do you want me to draw? "
                        "Is it vertical (Major axis: vertical & Minor axis: horizontal) or horizontal "
                        "(Major axis: horizontal & Minor axis: vertical)? "
                        "Type 'vertical' for Vertical Ellipse or 'horizontal' for Horizontal Ellipse: ").lower().strip().replace("_"," ").replace(",","").replace(".","")
        if ellipse_input=="vertical":
            vertical_ellipse()
        if ellipse_input=="horizontal":
            horizontal_ellipse()
        else:
            print("Sorry,I cannot draw it")
    if txtloop_input=="triangle":
        triangle_input=input("Which kind of Triangle do you want me to draw? Enter the type: ").lower().strip().replace("_"," ").replace(",","").replace(".","")
        if triangle_input == "rightangledtriangle" or triangle_input == "rightangletriangle" or triangle_input == "righttriangle":
            right_angled_triangle()
        if triangle_input == "scalenetriangle":
            scalene_triangle()
        if triangle_input == "isoscelestriangle":
            isosceles_triangle()
        if triangle_input == "isoscelesrightangledtriangle" or triangle_input == "isoscelesrightangletriangle" or triangle_input == "isoscelesrighttriangle":
            right_angled_triangle()
        if triangle_input == "acutetriangle":
            equilateral_triangle()
        if triangle_input == "isoscelesacutetriangle" or triangle_input == "acuteisoscelestriangle":
            isosceles_triangle()
        if triangle_input == "scaleneacutetriangle" or triangle_input == "acutescalenetriangle":
            scalene_triangle()
        if triangle_input == "obtusetriangle":
            obtuse_triangle()
        if triangle_input == "scaleneobtusetriangle" or triangle_input == "obtusescalenetriangle":
            obtuse_triangle()
        if triangle_input == "isoscelesobtusetriangle" or triangle_input == "obtuseisoscelestriangle":
            isosceles_obtuse_triangle()
        if triangle_input == "equilateraltriangle":
            equilateral_triangle()
        else:
            print("Sorry,I cannot draw it")
    if txtloop_input=="hendecagon":
        hendecagon()
    if txtloop_input=="dodecagon":
        dodecagon()
    else:
        print("Sorry,I cannot draw it")


    again =input("Do you want me to draw more? Yes or No").lower().strip().replace("_"," ").replace(",","").replace(".","")
    if again == "yes":
        continue
    if again == "no":
        print("Goodbye!❤️")
        break
    else:
        print("Sorry, I didn't get it")
