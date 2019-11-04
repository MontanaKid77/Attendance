from hashlib import sha256
from math import *
from time import asctime

present = []
old_studentdb_file = open("student_database.txt", "w")
admin_file = open("admin_database.txt", "w")
students = {}
admin = {}
students["colton"] = 1234
admin["cherry"] = 1009

old_studentdb_file.write(str(students))
admin_file.write(str(admin))
old_studentdb_file.close()
admin_file.close()
del old_studentdb_file
del admin_file

old_studentdb_file = open("student_database.txt", "r")
admin_file = open("admin_database.txt", "r")

students = eval(old_studentdb_file.read())
admin = eval(admin_file.read())


old_studentdb_file.close()
admin_file.close()
del old_studentdb_file
del admin_file


def addStudent(name, pin):
    pin = sha256(str(pin)).digest()
    students[name] = pin
    new_studentdb_file = open("student_database.txt", "w")
    new_studentdb_file.write(str(students))
    new_studentdb_file.close()
    del new_studentdb_file

def removeStudent(name):
    new_studentdb_file = open("student_database.txt", "r")
    try:
        students.pop(name)
    except:
        print "{} not found in database.".format(name)
        return
    
    new_studentdb_file.write(str(students))
    new_studentdb_file.close()
    del new_studentdb_file

def attendance():
    att_file = open("attendance_log.txt", "a")
    t = asctime()
    entry = t + " - "
    for i in present:
        entry += i.capitalize()
    att_file.write(entry)
    att_file.close()
    raw_input("Please press enter...")
    exit(0)
    


while(True):
    user = (raw_input("What is your name? ")).lower()
    old_studentdb_file = open("student_database.txt", "r")
    admin_file = open("admin_database.txt", "r")

    students = eval(old_studentdb_file.read())
    admin = eval(admin_file.read())

    
    
    if (user in admin):
        
        while(True):
            pin = raw_input("Please enter your pin: ")

            if (int(pin) == admin.get(user)):
                print "What do you need to do? 'add student', 'remove student', 'check attendance'"
                getOption = raw_input("What would you like to do? ").lower()

                if (getOption == "add student"):
                    newStudent = raw_input("New student name: ")
                    newPin = input("Enter their new pin: ")
                    addStudent(newStudent, newPin)
                if (getOption == "remove student"):
                    name = raw_input("Which student would you like to remove? ")
                    check = raw_input("Are you sure you would like to remove" + str(name) + "from your roll sheet? ")
                    if (check == 'yes', 'y'):
                        for i in range(4):
                            doublecheck = raw_input("Please re-enter your pin: ")
                            if (int(doublecheck) == admin.get(user)):
                                removeStudent(name)
                                break

                            else:
                                i +=1
                                print "Please try again."

                if (getOption == "check attendance"):
                    attendance()

                    
    old_studentdb_file.close()
    del old_studentdb_file






            


