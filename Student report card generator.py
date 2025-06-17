def avg(marks):
    total = sum(marks.values())
    return total / len(marks)

def grade(avrg):
    if avrg >= 80:
        return 'A'
    elif avrg >= 60:
        return 'B'
    elif avrg >= 40:
        return 'C'
    else:
        return 'F'

add_bonus = lambda x: x + 5

name, age = input("Enter name and age [e.g. Ali,21] ").split(",")
marks = {}
marks['eng'], marks['urd'], marks['math'] = [int(x) for x in input("Enter marks for Eng, Urdu, Math [e.g. 80,75,90] ").split(",")]

bonus = input("Add 5 bonus marks to all subjects? (yes/no): ").lower()
if bonus == 'yes':
    marks = {subject: add_bonus(score) for subject, score in marks.items()}

avrg = avg(marks)
grd = grade(avrg)

rep = f"""Name: {name}
Age: {age}
Math: {marks['math']}
English: {marks['eng']}
Urdu: {marks['urd']}
Average: {avrg:.2f}
Grade: {grd}"""

with open("rep.txt", 'w') as file:
    file.write(rep)

with open("rep.txt", 'r') as file:
    repp = file.read()

print(repp)