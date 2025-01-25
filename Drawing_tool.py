import tkinter as tk
from tkinter import *
from tkinter import ttk
import Universal as un
from Universal import Calculator as cl

default_canvas_pos = 0

h1 = ("Arial", 25)
h2 = ("Arial", 15)
h3 = ("Arial", 10)
h4 = ("Arial", 8) # default

class Obj:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, master, name):
        self.master = master
        self.frame = Frame(master)
        self.name = name

    def set_position(self, x, y):
        self.frame.place(x = x, y = y)

class LongitudinalBox(Obj):
    datas = []
    item_objs = []
    underlines = []

    def __init__(self, master, title, datas):
        super().__init__(master, name = title)

        self.frame = Frame(master, relief="solid", borderwidth=2)
        self.datas = datas
        self.title = title
        self.title_label = Label(master = self.frame,
                                 text = title,
                                 font = h1)
        self.title_label.pack()
        title_underlie = ttk.Separator(self.frame, orient='horizontal')
        title_underlie.pack(fill='x')

        for data in datas:
            obj = None
            if type(data) == str:
                obj = Label(master = self.frame,
                            text = data,
                            font = h4)

            if obj == None:
                raise Exception("Obj is None")
            obj.pack()
            self.item_objs.append(obj)

            underlie = ttk.Separator(self.frame, orient='horizontal')
            underlie.pack(fill='x')
            self.underlines.append(underlie)

        self.frame.pack()
        self.frame.update()

        self.width = self.frame.winfo_reqwidth()
        self.height = self.frame.winfo_reqheight()

    def set_position(self, x, y):
        self.x = x
        self.y = y

        # center anchor
        width = self.frame.winfo_reqwidth()
        height = self.frame.winfo_reqheight()

        if isinstance(self.master, tk.Canvas):
            self.master.create_window(x, y, window=self.frame)
        else:
            self.frame.place(x = x - width/2, y = y - height/2)

    def box(self):
        width = self.frame.winfo_reqwidth()
        height = self.frame.winfo_reqheight()
        center_x, center_y = self.center()

        return (center_x, center_y, width, height)

    def center(self):
        x = self.frame.winfo_x()
        y = self.frame.winfo_y()
        width = self.frame.winfo_reqwidth()
        height = self.frame.winfo_reqheight()
        return (x + width/2, y + height/2)

class Drawing:
    @staticmethod
    def create_circle(x, y, r, canvasName):  # center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)

class layout:
    def __init__(self, canvas):
        self.canvas = canvas

    def layout(self, objs):
        print("layout!")

class CircleLayout(layout):
    def __init__(self, radius, center, start_angle, canvas):
        super().__init__(canvas)

        self.layout_generator = un.CircleCoordsLayout(radius, center) # coordinate generater
        self.start_angle = start_angle # It means what is the start point of the circle
        self.center = center # center position of circle layout
        self.radius = radius # circle layout's radius

    def layout(self, objs):
        for obj in objs:
            assert isinstance(obj, Obj), "There are not Obj class's instance"

        circumstance_angle = 360
        temp_angle = 0  # object location is allocated in accordance with this variable
        for i in range(0, len(objs)):
            dA = circumstance_angle / len(objs)

            temp_angle += dA
            pt = self.layout_generator.get_pt(temp_angle, self.start_angle)
            Drawing.create_circle(pt[0], pt[1], 2, self.canvas)

            objs[i].set_position(pt[0], pt[1])
        self.canvas.update()

    def draw_center(self):
        Drawing.create_circle(self.center[0], self.center[1], 2, self.canvas)

class Inheritance_layout(layout):
    def __init__(self, canvas, base_layout, search_base_data, search_obj):
        super(Inheritance_layout, self).__init__(canvas)

        self.base_layout = base_layout
        self.search_base_data = search_base_data # It is lambda that finds base data
        self.search_obj = search_obj # It is lambda that finds obj for layouting
        
    def layout(self, objs, datas):
        self.base_layout.layout(objs)

        for i in range(0, len(objs)):
            box = objs[i]

            for base_theory_name in self.search_base_data(datas, box.name):
                searched_box = self.search_obj(objs, base_theory_name)
                if searched_box != None:
                    r1_proximity_pt = cl.find_proximity_pt_between_rects(box.box(), searched_box.box())
                    r2_proximity_pt = cl.find_proximity_pt_between_rects(searched_box.box(), box.box())

                    self.canvas.create_line(r1_proximity_pt[0], r1_proximity_pt[1],
                                       r2_proximity_pt[0], r2_proximity_pt[1],
                                       arrow=tk.FIRST)
        self.canvas.update()