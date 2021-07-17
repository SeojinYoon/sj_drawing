import numpy as np

class Calculator:
    @staticmethod
    def find_proximity_pt_between_rects(ref_rect, other_rect):
        ref_rect_width, ref_rect_height = ref_rect[2], ref_rect[3]

        ref_rect_center_x, ref_rect_center_y = ref_rect[0], ref_rect[1]

        other_rect_center_x, other_rect_center_y = other_rect[0], other_rect[1]

        dx = other_rect_center_x - ref_rect_center_x
        dy = other_rect_center_y - ref_rect_center_y

        if dx == 0:
            slope = np.inf
        else:
            slope = dy / dx

        ref_rect_slope = ref_rect_height / ref_rect_width

        if slope == np.inf and dy >= 0:
            xp = ref_rect_center_x + (ref_rect_width / 2)
            yp = yp = ref_rect_center_y + (ref_rect_height / 2)

            return [xp, yp]
        elif slope == np.inf and dy < 0:
            xp = ref_rect_center_x + (ref_rect_width / 2)
            yp = ref_rect_center_y - (ref_rect_height / 2)

            return [xp, yp]

        # Reference Coords -> Descrartes
        if np.abs(slope) < np.abs(ref_rect_slope):
            if dx > 0:
                xp = ref_rect_center_x + (ref_rect_width / 2)  # right side
                yp = ref_rect_center_y + slope * np.abs((xp - ref_rect_center_x))
            else:
                xp = ref_rect_center_x - (ref_rect_width / 2)  # left side
                yp = ref_rect_center_y - slope * np.abs((xp - ref_rect_center_x))
        else:
            if dy > 0:
                yp = ref_rect_center_y + (ref_rect_height / 2)  # top side
                xp = ref_rect_center_x + (1 / slope) * np.abs((yp - ref_rect_center_y))
            else:
                yp = ref_rect_center_y - (ref_rect_height / 2)  # bottom side
                xp = ref_rect_center_x - (1 / slope) * np.abs((yp - ref_rect_center_y))

        return [xp, yp]

    @staticmethod
    def get_line(pt1, pt2):
        x_pos = 0
        y_pos = 1

        slope = (pt2[y_pos] - pt1[y_pos]) / (pt2[x_pos] - pt1[x_pos])

        x = 0
        bias = slope * (x - pt1[x_pos]) + pt1[y_pos]
        return (slope, bias)

class CircleCoordsLayout:
    """
    This class makes 2d coordinates according to circle
    """
    x_pos = 0
    y_pos = 1

    def __init__(self, radius, center):
        self.center = center
        self.radius = radius

    def get_pt(self, degree, start_angle = 0):
        x, y = convert_polar_to_descrartes2(self.radius, degree + start_angle)

        y = -y # for matching with decrartes coords and computer coords
        return (x + self.center[self.x_pos], y + self.center[self.y_pos])

def convert_descrartes_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    radian = np.arctan(x/y)
    return r, radian

def convert_polar_to_descrartes(r, radian):
    x = r * np.cos(radian)
    y = r * np.sin(radian)
    return x, y

def convert_polar_to_descrartes2(r, degree):
    import math
    radian = math.radians(degree)
    x = r * np.cos(radian)
    y = r * np.sin(radian)
    return x, y

if __name__ == "__main__":
    convert_descrartes_to_polar(1,1)
    convert_polar_to_descrartes(1, np.pi/2)
    convert_polar_to_descrartes2(1, 45)

    Calculator.find_proximity_pt_between_rects([0, 0, 10, 10], [40, 40, 10, 10])
    Calculator.get_line([0,0], [10,10])

    a = CircleLayout(20, (300,300))
    for i in range(0, 45):
        pt = a.get_pt(i)


