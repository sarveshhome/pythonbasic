# Object-oriented programming
# print("Hello ".__add__("World"))

# print((10).__add__(20))

# stuff = list()
# print(dir(stuff))

# x =10
# y =15
# print((x).__add__(y)))

# Starting with programs

# usf = input('Enter the US Floor Number: ')
# wf = int(usf) - 1
# print('Non-US Floor Number is',wf)


class PartyAnimal:

    def __init__(self, name):
        self.x = 0
        self.name = name

    def party(self):
        self.x += 1
        print(self.name, "has", self.x, "guests")


class CricketFan(PartyAnimal):

    def __init__(self, name):
        super().__init__(name)
        self.points = 0

    def six(self):
        self.points += 6
        self.party()
        print(self.name, "points", self.points)


s = PartyAnimal("Sally")

s.party()
s.party()

j = CricketFan("Jim")

j.party()
j.six()

print(dir(j))