# input = 11
# real = 11
# if real == input:
#     print("Hello!")
# else:
#     print("Who are you?")

# ================================================================


# input = 33
# real_egoing = 11
# real_k8805 = "ab"
# if real_egoing == input:
#   print("Hello!, egoing")
# elif real_k8805 == input:
#   print("Hello!, k8805")
# else:
#   print("Who are you?")


# ===============================================================


# input_id = input("아이디를 입력해주세요.\n")
# members = ['egoing', 'k8805', 'leezche']
# for member in members:
#     if member == input_id:
#         print('Hello!, '+member)
#         import sys
#         sys.exit()
# print('Who are you?')


# ===============================================================


# def make_string(str, num):
#     return str*num
# print(make_string('b', 3))


# ===============================================================


# class Cal(object):
#     def __init__(self, v1, v2):
#         self.v1 = v1
#         self.v2 = v2
 
#     def add(self):
#         return self.v1+self.v2
 
#     def subtract(self):
#         return self.v1-self.v2
 
 
# c1 = Cal(10,10)
# print(c1.add())
# print(c1.subtract())
# c2 = Cal(30,20)
# print(c2.add())
# print(c2.subtract())


# ===============================================================


# class C(object):
#     def __init__(self, v):
#         self.value = v
#     def show(self):
#         print(self.value)
 
# c1 = C(10)
# print(c1.value)
# c1.value = 20
# print(c1.value)
# c1.show()


# ===============================================================


# class C(object):
#     def __init__(self, v):
#         self.__value = v
#     def show(self):
#         print(self.__value)
# c1 = C(10)
# #print(c1.__value)
# c1.show()


# ===============================================================


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


class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        result = self.v1+self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result
    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)
    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)
class CalMultiply(Cal):
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result
    def info(self):
        return "CalMultiply => %s" % super().info()
class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result
    def info(self):
        return "CalDivide => %s" % super().info()
 
c0 = Cal(30, 60)
print(c0.info())
c1 = CalMultiply(10,10)
print(c1.info())
c2 = CalDivide(20,10)
print(c2.info())