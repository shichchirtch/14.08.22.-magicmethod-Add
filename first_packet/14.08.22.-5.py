class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    def show_params(self):
        print( f'width = {self.width}, height = {self.height}, depth = {self.depth}')

    def __add__(self, ob2):
        if type(ob2) == Box3D:
            a = self.width+ob2.width
            b = self.height +ob2.height
            c = self.depth + ob2.depth
            new_obj = Box3D(a, b, c)
            return new_obj

    def __mul__(self, other):
        if type(other) == int:
            a = self.width*other
            b = self.height * other
            c = self.depth * other
            new_obj = Box3D(a,b,c)
            return new_obj

    def __rmul__(self, other):
        if type(other) in (int, float):
            return self*other

    def __sub__(self, other):
        if isinstance(other, Box3D):
            a = self.width-other.width
            b = self.height -other.height
            c = self.depth - other.depth
            new_obj = Box3D(a,b,c)
            return new_obj

    def __floordiv__(self, other):
        if isinstance(other, int):
            a = self.width // other
            b = self.height // other
            c = self.depth // other
            new_obj = Box3D(a, b, c)
            return new_obj
    def __mod__(self, other):
        if isinstance(other, int):
            a = self.width % other
            b = self.height % other
            c = self.depth % other
            new_obj = Box3D(a, b, c)
            return new_obj

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box.show_params()
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box.show_params()
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box.show_params()
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box.show_params()
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box.show_params()
box = box2 % 3    # Box3D: width=2, height=1, depth=0
box.show_params()

