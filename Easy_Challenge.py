class M:
    '''
    A Method Resolution Order Used To Describe Inheritance Properties From A Parent Class Towards Child-Classes.
    '''
    @staticmethod
    def do_nothing():
        '''
        All Child Classes Of M Will Execute This Method Which Returns None.
        '''
        return None

# Classes A And B Inherit Class M's Attr & Method.
# This Is A Case Of A Normal Inheritance.
class A(M):
    def __init__(self):
        M.__init__(self)
        self.do_nothing()
    
class B(M):
    def __init__(self):
        M.__init__(self)
        self.do_nothing()

# Classes X, Y, Z Inherit Both Child Classes(A, B).
# This Is A Case Of A MultiLevel Inheritance For Class X, Since It Inherits From Only One Class Which Is Also A Child Class.
# However, For Classes Y And Z Describe Both MultiLevel And Multiple Inheritances, Since They Both Inherit From Two Child Classes.
class X(A):
    def __init__(self):
        A.__init__(self)
        self.do_nothing()

class Y(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.do_nothing()

class Z(B, M):
    def __init__(self):
        B.__init__(self)
        M.__init__(self)
        self.do_nothing()

# Class Obj Also Describes Both Multiple And MultiLevel Inheritances.
class Obj(X, Y, Z):
    def __init__(self):
        X.__init__(self)
        Y.__init__(self)
        Z.__init__(self)
        self.do_nothing()




