# class User:
#     num_users = 0 # class 변수
#     def __init__(self, name):
#         self.name = name # instance 변수 (메소드 안에서 self라는 키워드를 사용해서 선언하는 변수)
#         User.num_users += 1

# u = User('monkey')
# print(User.num_users, u.name) # 1 monkey
# u2 = User('sunshine')
# print(User.num_users, u2.name) # 2 sunshine
# print(User.num_users, u.num_users, u2.num_users) # 2, 2, 2
# # 클래스 변수는 모든 인스턴스들 간에 값을 공유한다.
# # class User의 인스턴스 u, u2 모두 똑같은 num_users 값을 가진다.


# =====================================================================


# class Text:
#     def __init__(self, str):
#         self.text = str

#     def __str__(self):
#         return "Text Class: " + self.text

# class User:
#     numUsers = 0 # 클래스 변수
#     def __init__(self, name):
#         self.numArticle = 0 # 인스턴스 변수로 초기화
#         self.name = name
#         self.articles = [] # 인스턴스 변수
#         User.numUsers += 1

#     def write(self, text):
#         self.articles.append(text)
#         self.numArticle += 1

#     def __str__(self):
#         return 'User class : %s, %s' % (self.name, [str(p) for p in self.articles]) # 방법 2
#         # return "User class: %s, %s" % (self.name, ' / '.join(str(p) for p in self.articles)) #방법 1

# t = Text('This is some text')
# t2 = Text('This is some text2')
# user = User('monkey')
# user.write(t)
# user.write(t2)

# print(t) 
# print(user,',',user.numArticle)


# =====================================================================


# class Text:
#     def __init__(self, str):
#         self.text = str

#     def __str__(self):
#         return "Text Class " + self.text

#     def getLength(self):
#         return len(self.text)

# class Article(Text): #Article 클래스(자식클래스)는 Text 클래스(부모클래스, 슈퍼클래스)를 상속 받았다.
#     def __init__(self, title, text):
#         self.title = title
#         self.text = text

#     def __str__(self):
#         return 'Article Class %s %s' % (self.title, self.text)

# class User:
#     numUsers = 0 # 클래스 변수
#     def __init__(self, name):
#         self.numArticle = 0 # 인스턴스 변수로 초기화
#         self.name = name
#         self.articles = [] # 인스턴스 변수
#         User.numUsers += 1

#     def write(self, text):
#         self.articles.append(text)
#         self.numArticle += 1

#     def __str__(self):
#         return "%s, %s" % (self.name, ' / '.join(str(p) for p in self.articles))

# t = Article('hello', 'This is some text') 
# t2 = Article('hello2', 'This is some text2')
# user = User('monkey')
# user.write(t)
# user.write(t2)

# # print([t][0])
# print(t,', ',t.getLength()) 
# print(user,',',user.numArticle)


# =====================================================================


