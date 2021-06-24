row = int(input())
col = int(input())
count  = int(input())
colstrokes = set()
rowstrokes = set()

for i in range(count):
    temp = (input().split())

    if(temp[0] == 'R'):
        if(int(temp[1]) not in rowstrokes):
            rowstrokes.add(int(temp[1]))
        else:
            rowstrokes.remove(int(temp[1]))
    else:
        if(int(temp[1]) not in colstrokes):
            colstrokes.add(int(temp[1]))
        else:
            colstrokes.remove(int(temp[1]))

g = len(rowstrokes) * (col - len(colstrokes)) + len(colstrokes) * (row - len(rowstrokes))

print(g)
j5 is really simple
once u get the idea
class Section:
    def init(self):
        self.l = 0
        self.m = 0
        self.s = 0

    def add(self, book):
        if(book == 'L'):
            self.l +=1
        if(book == 'M'):
            self.m +=1
        if(book == 'S'):
            self.s +=1

books = input()
total = Section()

l = Section()
m = Section()
s = Section()

for book in books:
    total.add(book)

j = 0
for i in range(total.l):
    l.add(books[j])
    j += 1

for i in range(total.m):
    m.add(books[j])
    j+=1

for i in range(total.s):
    s.add(books[j])
    j+=1

print(l.m + l.s + m.l + m.s - min(m.l, l.m))
