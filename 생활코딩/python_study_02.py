# class Cal(object):
#     def __init__(self, v1, v2):
#         if isinstance(v1, int):
#             self.v1 = v1
#         if isinstance(v2, int):
#             self.v2 = v2
#     def add(self):
#         return self.v1+self.v2
#     def subtract(self):
#         return self.v1-self.v2
#     def setV1(self, v):
#         if isinstance(v, int):
#             self.v1 = v
#     def getV1(self):
#         return self.v1
# class CalMultiply(Cal):
#     def multiply(self):
#         return self.v1*self.v2
# class CalDivide(CalMultiply):
#     def divide(self):
#         return self.v1/self.v2
# c1 = CalMultiply(10,10)
# print(c1.add())
# print(c1.multiply())
# c2 = CalDivide(20,10)
# print(c2, c2.add())
# print(c2, c2.multiply())
# print(c2, c2.divide())


# ===============================================================


# class Cs:
#     @staticmethod
#     def static_method():
#         print("Static method")
#     @classmethod
#     def class_method(cls):
#         print("Class method")
#     def instance_method(self):
#         print("Instance method")
# i = Cs()
# Cs.static_method()
# Cs.class_method()
# i.instance_method()


# ===============================================================


# class Cs:
#     count = 0
#     def __init__(self):
#         Cs.count = Cs.count + 1
#     @classmethod
#     def getCount(cls):
#         return Cs.count
# i1 = Cs()
# i2 = Cs()
# i3 = Cs()
# i4 = Cs()
# print(Cs.getCount())


# ===============================================================


# class Cal(object):
#     _history = []
#     def __init__(self, v1, v2):
#         if isinstance(v1, int):
#             self.v1 = v1
#         if isinstance(v2, int):
#             self.v2 = v2
#     def add(self):
#         result = self.v1+self.v2
#         Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
#         return result
#     def subtract(self):
#         result = self.v1-self.v2
#         Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
#         return result
#     def setV1(self, v):
#         if isinstance(v, int):
#             self.v1 = v
#     def getV1(self):
#         return self.v1
#     @classmethod
#     def history(cls):
#         for item in Cal._history:
#             print(item)
# class CalMultiply(Cal):
#     def multiply(self):
#         result = self.v1*self.v2
#         Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
#         return result
# class CalDivide(CalMultiply):
#     def divide(self):
#         result = self.v1/self.v2
#         Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
#         return result
# c1 = CalMultiply(10,10)
# print(c1.add())
# print(c1.multiply())
# c2 = CalDivide(20,10)
# print(c2, c2.add())
# print(c2, c2.multiply())
# print(c2, c2.divide())
# Cal.history()


# ===============================================================


# class C1:
#     def m(self):
#         return 'parent'
# class C2(C1):
#     def m(self):
#         return super().m() + ' child'
#     pass
# o = C2()
# print(o.m())


# ===============================================================


# class Cal(object):
#     _history = []
#     def __init__(self, v1, v2):
#         if isinstance(v1, int):
#             self.v1 = v1
#         if isinstance(v2, int):
#             self.v2 = v2
#     def add(self):
#         result = self.v1+self.v2
#         Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
#         return result
#     def subtract(self):
#         result = self.v1-self.v2
#         Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
#         return result
#     def setV1(self, v):
#         if isinstance(v, int):
#             self.v1 = v
#     def getV1(self):
#         return self.v1
#     @classmethod
#     def history(cls):
#         for item in Cal._history:
#             print(item)
#     def info(self):
#         return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)
# class CalMultiply(Cal):
#     def multiply(self):
#         result = self.v1*self.v2
#         Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
#         return result
#     def info(self):
#         return "CalMultiply => %s" % super().info()
# class CalDivide(CalMultiply):
#     def divide(self):
#         result = self.v1/self.v2
#         Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
#         return result
#     def info(self):
#         return "CalDivide => %s" % super().info()
 
# c0 = Cal(30, 60)
# print(c0.info())
# c1 = CalMultiply(10,10)
# print(c1.info())
# c2 = CalDivide(20,10)
# print(c2.info())


# ===============================================================


class C1():
    def c1_m(self):
        print("c1_m")
    def m(self):
        print("C1 m")
 
class C2():
    def c2_m(self):
        print("c2_m")
    def m(self):
        print("C2 m")
 
class C3(C2, C1):
    def m(self):
        print("C3 m")
 
c = C3()
c.c1_m()
c.c2_m()
c.m()
print(C3.__mro__)