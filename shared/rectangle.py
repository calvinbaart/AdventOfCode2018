import re

class Rectangle:
    def __init__(self, id, x, y, w, h, map):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)

        if map is not None:
            for i in range(self.x, self.x + self.w):
                for j in range(self.y, self.y + self.h):
                    key = f"{i}#{j}"

                    if key in map:
                        map[key] = map[key] + 1
                    else:
                        map[key] = 1

    def overlap(self, rect):
        if (
            self.pos_x2() < rect.pos_x() or self.pos_x() >= rect.pos_x2() or
            self.pos_y2() < rect.pos_y() or self.pos_y() >= rect.pos_y2()
        ):
            return False

        leftX = max(self.pos_x(), rect.pos_x())
        rightX = min(self.pos_x2(), rect.pos_x2())
        topY = max(self.pos_y(), rect.pos_y())
        bottomY = min(self.pos_y2(), rect.pos_y2())

        return Rectangle(self.id, leftX, topY, rightX - leftX, bottomY - topY, None)

    def width(self):
        return self.w

    def height(self):
        return self.h

    def pos_x(self):
        return self.x

    def pos_y(self):
        return self.y

    def pos_x2(self):
        return self.x + self.w

    def pos_y2(self):
        return self.y + self.h

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"Rectangle(): {self.id} = {self.pos_x()},{self.pos_y()},{self.pos_x2()},{self.pos_y2()}"

    @staticmethod
    def fromLine(line, map = None):
        regex = r"#(\d*)\s*@\s*(\d*),(\d*):\s*(\d*)x(\d*)"
        matches = re.findall(regex, line, re.MULTILINE)

        return Rectangle(matches[0][0], matches[0][1], matches[0][2], int(matches[0][3]), int(matches[0][4]), map)
