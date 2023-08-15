def Myfun1(l):
    return len(l)

def Myfun2(l):
    return l[1]
l = ['hello', 'hi', 'bye', 'thank you']
#Sorting using the first letter.
l.sort()
print(l)
#Sorting using the length of the word.
l.sort(key=Myfun1)
print(l)
#Sorting using the second letter of the word.
l.sort(key=Myfun2)
print(l)
l.sort(key=Myfun2, reverse=True)
print(l)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def Myfun3(lst):
    return lst.y
lst = [Point(1, 15), Point(10, 5), Point(1, 8)]
lst.sort(key=Myfun3)
for i in lst:
    print(i.x, i.y)

d1 = {100:'M', 5:'C', 70:'A'}
res = sorted(d1)
print(res)

res1 = sorted(lst, key=Myfun3)
print(res1)
for i in res1:
    print(i.x, i.y)