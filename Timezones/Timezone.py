import datetime

class Person:
    def __init__(self, idNum, name, tz):
        self.idNum = idNum
        self.name = name
        self.tz = tz

def findTime(timezone):
    now = datetime.datetime.now()
    nowHour = now.strftime("%H")
    print(nowHour)
    nowMins = now.strftime("%M")
    print(nowMins)
    print(f"{nowHour + timezone}:{nowMins}")

timezones = open("timezones.txt","r")
"""
for line in timezones:
    print(line)
"""

p1 = Person(1, "Bob", "-5")
p2 = Person(2, "James", "+8")

people = []


nowHour = 0
nowMins = 0


findTime()
print(f"{nowHour + 5}:{nowMins}")


people.append(p1)
people.append(p2)

idNum = int(len(people)) + 1
name = str(input("What is your persons name? "))
country = str(input("What country is your person from (CAPITALISE THE FIRST LETTER E.G., 'Australia')? "))

p1 = Person(idNum, name, country)

people.append(p1)

for i in range(len(people)):
    print(f"{people[i].idNum} | {people[i].name} | {people[i].tz}\n")
    print()




# # # # # # # # # # LEAVE HERE DO NOT DELETE # # # # # # # # # #
timezones.close()
# # # # # # # # # # LEAVE HERE DO NOT DELETE # # # # # # # # # #
