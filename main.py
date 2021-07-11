
import Drawing_tool
import Drawing_tool as dt
from tkinter import *

import Philosophy

root = Tk()
root.title("Philosophy")
root.geometry("1000x1000")

canvas = Canvas(root, relief="solid", bd=2)
canvas.pack(fill = "both", expand = True)

theories = [
    Philosophy.Theory("Rationalism"),
    Philosophy.Theory("Empiricism"),
    Philosophy.Theory("Logical positivism", ["Empiricism"], descriptions=["관찰과 경험을 통해서 검증가능한 주장만이 의미가 있다."]),
    Philosophy.Theory("Karl Popper", ["Logical positivism"], descriptions=["틀릴 수 있는 이론만이 과학이론이 될 수 있다."]),
    Philosophy.Theory("My Theory", ["Karl Popper"], descriptions=["틀릴 수 있는 이론만이 과학이론이 될 수 있다."])
]
boxes = list(map(lambda theory: Drawing_tool.LongitudinalBox(canvas, theory.name, theory.descriptions), theories))

center_layout_pt = (400, 400)
layout = Drawing_tool.CircleLayout(radius=300, center=center_layout_pt, start_angle=45, canvas=canvas)

def search_theory(theories, name):
    for theory in theories:
        if theory.name == name:
            return theory
    return None

def search_box(boxes, title):
    for box in boxes:
        if box.title == title:
            return box
    return None

search_base_data = lambda theories, theory_name: search_theory(theories, theory_name).base_theories
search_obj = lambda boxes, base_theory_name: search_box(boxes, base_theory_name)

layout_ = dt.Inheritance_layout(canvas, layout, search_base_data, search_obj)
layout_.layout(objs=boxes, datas=theories)

root.mainloop()




