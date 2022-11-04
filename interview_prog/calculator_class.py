class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y


class B:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def subtract(self):
        if self.x > self.y:
            return self.x - self.y
        else:
            return self.y - self.x


class C:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def mul(self):
            return self.x * self.y

class D(A,B,C):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

    def fun(self):
        return (A.add(self) - self.z)

d = D(2,3,4)
print(d.fun())

