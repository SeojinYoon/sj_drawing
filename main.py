
import Drawing_tool as dt
from tkinter import Tk, Frame, Canvas, Scrollbar
from tkinter import HORIZONTAL, VERTICAL, BOTH, BOTTOM, RIGHT, X, Y
import Philosophy

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

theories = [
    Philosophy.Theory("Rationalism", descriptions=["추론이 지식의 원천이다."]),
    Philosophy.Theory("Empiricism", descriptions=["지식은 오로지 감각 경험으로부터 온다"]),
    Philosophy.Theory("Logical positivism", base_theories = ["Empiricism"], descriptions=["20c", "관찰과 경험을 통해서 검증가능한 주장만이 의미가 있다."]),
    Philosophy.Theory("Karl Popper", base_theories = ["Logical positivism"], descriptions=["1902~1994", "틀릴 수 있는 이론만이 과학이론이 될 수 있다.", "Falsifiability"]),
    Philosophy.Theory("Freud", descriptions=["1856~1939", "모든 행동의 기저에는 성욕이 있다.", "libido"]),
    Philosophy.Theory("Carl Jung", base_theories = ["Freud"], descriptions=["1875 ~ 1961", "삶의 목표는 자아가 자기(Self)를 찾아 떠나는 여행이다.", "Persona", "Self"]),
    Philosophy.Theory("Adler", base_theories = ["Freud"], descriptions=["1870 ~ 1937", "인간을 움직이는 힘은 불완전함을 극복하려는 의지이다.", "inferiority complex"]),
    Philosophy.Theory("Hume", base_theories = ["Empiricism"], descriptions=["1722 ~ 1785", "인식할 수 있는 것만 유의미하다."]),
    Philosophy.Theory("Monoism", base_theories = ["Idealism"], descriptions=["모든 현상은 동일한 원리로 표현할 수 있다."]),
    Philosophy.Theory("Dualism", base_theories = ["realism"], descriptions=["세계나 사상을 두개의 독립적인 근본 원리로 표현할 수 있다."]),
    Philosophy.Theory("realism", descriptions=["의식, 주관으로부터 독립된 실재가 존재한다."]),
    Philosophy.Theory("Idealism", descriptions=["우리가 알 수 있는 실체는 정신적으로 구성된 것이다."]),
    Philosophy.Theory("베다", base_theories = ["Monoism"], descriptions=["세계와 자아는 하나이다", "범아일여"]),
    Philosophy.Theory("우파니샤드", base_theories = ["베다"], descriptions=["브라만에게 의지하지 말고 각자가 내면을 탐구하자"]),
    Philosophy.Theory("바가바드 기타", base_theories = ["베다", "우파니샤드"], descriptions=["세속과 탈속의 화해", "의무 안에서 신을 발견하자", "의무를 행하되 결과를 기대하지 말라."]),
    Philosophy.Theory("Hinduism", base_theories = ["베다", "우파니샤드"], descriptions=["나의 의지와 행위가 곧 우주의 의지이자 질서가 될 때, 깨닫게 된다.", "윤회", "카르마"]),
]

boxes = list(map(lambda theory: dt.LongitudinalBox(canvas, theory.name, theory.descriptions), theories))

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


radius = 300
center_layout_pt = (500, 500)
search_base_data = lambda theories, theory_name: search_theory(theories, theory_name).base_theories
search_obj = lambda boxes, base_theory_name: search_box(boxes, base_theory_name)

base_layout = dt.CircleLayout(radius = radius, 
                              center = center_layout_pt, 
                              start_angle = 45, 
                              canvas = canvas)
base_layout.draw_center()

layout_ = dt.Inheritance_layout(canvas = canvas, 
                                base_layout = base_layout, 
                                search_base_data = search_base_data, 
                                search_obj = search_obj)
layout_.layout(objs=boxes, datas=theories)

root.mainloop()



class A:
    pass
