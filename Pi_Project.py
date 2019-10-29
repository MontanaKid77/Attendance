# create a dictionary of students and pins
students = {"robert": 4499, "jimmie": 5032, "sarah": 5901, "ethan": 4201, "jennifer": 1523, "brian": 4065, "emily": 3029, "paul": 5544, "anna": 6798}

admin = {"bdog": 1009, "colton": 1010, "cherry": 1011}

present = []


while(True):
    student = (raw_input("What is your name? ")).lower()
    if (student in admin):
        
        while(True):
            pin = input("Please enter your pin: ")

            if (pin == admin.get(student)):
                print "Your options are 'add student', 'remove student' 'check attendance', 'exit'"
                getOption = raw_input("What would you like to do? ").lower()

                if (getOption == "add student"):
                    newStudent = raw_input("Do you need to add a student? ")
                    newPin = input("Enter their new pin: ")
                    students[newStudent] = newPin
                    
                elif (getOption == "remove student"):
                    studentRemove = raw_input("Which student would you like to remove? ")
                    confirmation = raw_input("Are you sure you would like to remove {} ").lower().format(studentRemove)

                    if confirmation == ['yes', 'y']:
                        students.pop(studentRemove)
                        
                    elif confirmation == ['no', 'n']:
                        
                    else:
                        print "Please enter 'yes', 'no', 'y', or 'n'"
                        
                 elif (get Option == "exit"):
                    break
            
    elif (student == "Done"):
        break
    
    elif (student not in students):
        print "This name is not correct please try again."

    elif (student in present):
        print "You have already been signed in, next please."
        
    else:

        pin = input("Please enter your pin: ")
        
        
        if (pin != students.get(student)):
            print "This pin is not correct please try again."
            pin = input("Please enter your pin: ")
            
        if (pin == students.get(student)):
            print "Welcome back {}".format(str(student))
            present.append(student)

        else:
            print "Didn't work."



print "These students are present. {}".format(present)

    

