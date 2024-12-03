import datetime as datetime

now = ""
tzOne = ""

class Person:
    def __init__(self, idNum, name, tz):
        self.idNum = idNum
        self.name = name
        self.tz = tz

timezones = open("timezones.txt","r")

def displayMenu():
    print("|**************************************|\n|                                      |\n| 1. Add a new person                  |\n| 2. Show all people                   |\n| 3. Save people                       |\n| 4. End Program                       |\n|                                      |\n|                                      |\n****************************************")

def findTime(timezone):
    now = datetime.datetime.now()
    nowHour = int(now.strftime("%H")) + int(timezone)
    nowMins = now.strftime("%M")
    print(f"{nowHour}:{nowMins}")

def displayUsers():
    for peopleNum in range(len(people)):
        tzTemp = people[peopleNum].tz
        print(f"{people[peopleNum].idNum} | {people[peopleNum].name} | {findTime(tzOne)}\n")

print(displayMenu())

p1 = Person(1, "Bob", "-5")
p2 = Person(2, "James", "8")

people = []


now = datetime.datetime.now()
print(now)



people.append(p1)
people.append(p2)

idNum = int(len(people)) + 1
name = str(input("What is your persons name? "))
country = str(input("What country is your person from (CAPITALISE THE FIRST LETTER E.G., 'Australia')? "))

p1 = Person(idNum, name, country)

people.append(p1)

displayUsers()

for i in range(len(people)):
    print(f"{people[i].idNum} | {people[i].name} | {people[i].tz}\n")
    print()

# # # # # # # # # # LEAVE HERE DO NOT DELETE # # # # # # # # # #
timezones.close()
# # # # # # # # # # LEAVE HERE DO NOT DELETE # # # # # # # # # #
