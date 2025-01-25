
from Drawing_tool import LongitudinalBox, CircleLayout, Inheritance_layout
from tkinter import Tk, Frame, Canvas, Scrollbar
from tkinter import HORIZONTAL, VERTICAL, BOTH, BOTTOM, RIGHT, X, Y
from UML import Class, Protocol

root = Tk()
root.title("Philosophy")
root.geometry("800x800")

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

canvas = Canvas(frame, relief="solid", bd=2, scrollregion=(0,0,2000,2000))

hbar=Scrollbar(frame,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)

canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(fill = "both", expand = True)

classes = [
    Class(name = "ABC"),
    Class(name = "DEF", is_a = ["FFF"], has_a = [""]),
    Protocol(name = "FFF", is_a = [])
]

boxes = []
for class_ in classes:
    box = LongitudinalBox(canvas, class_.name, class_.descriptions)
    boxes.append(box)

def search_class(classes, name):
    for class_ in classes:
        if class_.name == name:
            return class_
    return None

def search_box(boxes, title):
    for box in boxes:
        if box.title == title:
            return box
    return None


radius = 300
center_layout_pt = (500, 500)
search_base_data = lambda theories, theory_name: search_class(classes, theory_name).is_a
search_obj = lambda boxes, base_theory_name: search_box(boxes, base_theory_name)

base_layout = CircleLayout(radius = radius, 
                           center = center_layout_pt, 
                           start_angle = 45, 
                           canvas = canvas)
base_layout.draw_center()

layout_ = Inheritance_layout(canvas = canvas, 
                             base_layout = base_layout, 
                             search_base_data = search_base_data, 
                             search_obj = search_obj)
layout_.layout(objs=boxes, datas=classes)

root.mainloop()


