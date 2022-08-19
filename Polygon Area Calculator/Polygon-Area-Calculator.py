class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, setwidth):
        self.width = setwidth

    def set_height(self, setheight):
        self.height = setheight

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        picturestr = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for x in range(self.height):
                picturestr = picturestr + (self.width) * ("*") + "\n"
            return picturestr

    def get_amount_inside(self, otherobj):
        if otherobj.width > self.width or otherobj.height > self.height:
            return 0
        else:
            widthratio = int(self.width / otherobj.width)
            heightratio = int(self.height / otherobj.height)
            return (widthratio * heightratio)

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):

    def __init__(self, length):
        self.width = length
        self.height = length

    def set_side(self, setlength):
        self.width = setlength
        self.height = setlength

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_width(self, setwidth):
        self.width = setwidth
        self.height = setwidth

    def set_height(self, setheight):
        self.height = setheight
        self.width = setheight