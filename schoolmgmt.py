#create a dictionary document to record the inputs. QQ- can I leave the default value blank?
school_dict = {
    "student": [{"f_name": "A", "l_name": "CC", "class_attend":"2A"}],
    "teacher": [{"f_name":"B", "l_name": "C", "subject":"C", "class_teach": "2C" }],
    "homeroom_teacher": [{"f_name": "F", "l_name": "D", "class_lead": "A" }],
}
print(school_dict)



def greeting_message(): 
    print("Hello user, welcome to school management application. Please enter the following commands as you wish:\n ")
    print("end -to leave the application\n")
    print("create -to create a user type: student, teacher or homeroom_teacher")
    print("manage -to manage users you create")

#choose option for the user interact with the application

#create the function create account
# student， let students provide first names， last names and classes they attend
#create the function teacher， let teachers provide first names， last names，subjects they teach and classes they teach
#create the function homeroom teacher， let home teachers provide first names， last names，and classes they lead
#Shall we show the inputs? What about the data structure? Dictionary or list?
def create_account(option):
    while True:
        option = input("Enter the user type you tend to create: ")
        if option== "student":
            name= input("Provide the first name:  ")#student_account():
            last_name = input("Provide the last name:  ")
            students_class = input("Provide the class name of the student: ")
            temp_dict = { "f_name": name,
                "l_name": last_name,
                "class_attend": students_class
            }
            print("The student has been created.") 
            school_dict["student"].append(temp_dict)
        
                      
        elif option == "teacher": #teacher_account():
            name = input("Provide the first name:  ")
            last_name= input("Provide the last name:  ")
            subjects = input("Provide the subject name:  ")
            teacher_teach = input("Provide the class you teach: ")
            temp_dict = { "f_name": name,
                "l_name": last_name,
                "subject": subjects,
                "class_teach":teacher_teach
            }
            print("The teacher has been created.")
            school_dict["teacher"].append(temp_dict)
    
            
            
        elif option == "homeroom_teacher": #def homeroom_teacher_account():
            name = input("Provide the first name:  ")
            last_name = input("Provide the last name:  ")
            Class_youlead= input("Provide the class name you lead: ")
            temp_dict = { "f_name": name,
                "l_name": last_name,
                "class_lead":Class_youlead
            }
            print("The homeroom teacher has been created.")
            school_dict["homeroom_teacher"].append(temp_dict)
        
        elif option == "end":
            break            
            
        else:
            print("It's invalid input! Please try again. ")



def manage_account(option):
    print("Enter user's type or enter class to see the whole class.")
    while True:
        option = input("Enter the user you tend to manage: ")
        if option == "student":
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            for student in school_dict["student"]:
                if student['f_name'] == f_name and student['l_name'] == l_name:
                    print(f"{student['f_name']} {student['l_name']} attends class {student['class_attend']} ")
                    print("Student's teachers:")
            for teacher in school_dict["teacher"]:
                if student['class_attend'] == teacher['class_teach']:
                        print(f"{teacher['f_name']} {teacher['l_name']} teaches this class {teacher['subject']}")
    

        elif option == "teacher":
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            for teacher in school_dict["teacher"]:
                if teacher ['f_name'] == f_name and teacher['l_name'] == l_name:
                    print(f"{teacher['f_name']} {teacher['l_name']} teaches class {student['class_attend']} {teacher['subject']}")
                    print("Student's list:")
            for student in school_dict["student"]:
                if student['class_attend'] == teacher['class_teach']:
                    print(f"{student['f_name']} {student['l_name']} ")


        elif option == "homeroom_teacher":
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            for homeroom_teacher in school_dict["homeroom_teacher"]:
                if homeroom_teacher['f_name'] == f_name and homeroom_teacher['l_name'] == l_name:
                    print(f"Homeroom teacher {f_name} {l_name} leads class {homeroom_teacher['class_lead']} ") 
                    print("Student's list:")
            for student in school_dict["student"]:
                if student['class_attend'] == homeroom_teacher['class_lead']:
                    print(f"{student['f_name']} {student['l_name']} ")

            
        elif option == "class":
            search_class = input("Provide class for search: ")
            for student in school_dict["student"]:
                print("Student's list:")
                if student["class_attend"] == search_class:
                    print(f"{student['f_name']} {student['l_name']} ")
            for homeroom_teacher in school_dict["homeroom_teacher"]:
                if homeroom_teacher["class_lead"] == search_class:
                    print(f"Homeroom teacher {f_name} {l_name} leads class {homeroom_teacher['class_lead']} ")

                
        
        elif option == "end":
            break
        else:
            print("It's invalid input! Please try again. ")



#print avaliable commands of school management application: create, manage and end
while True:
    greeting_message()
    option = input("Choose an option (end, create or manage): ").lower()
    if option == "create":
        create_account (option) 
    elif option == "manage":
        manage_account(option) 
    elif option == "end":
        break
    else:
        print("It's invalid input! Please try again. ")