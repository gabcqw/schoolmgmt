#create a dictionary document to record the inputs. QQ- can I leave the default value blank?
school_dict = {
    "student": [{"f_name": "A", "l_name": "CC", "class_attended":"2A"}],
    "teacher": [{"f_name":"B", "l_name": "C", "subject":"C", "class_teach": "2C" }],
    "homeroom_teacher": [{"f_name": "F", "l_name": "D", "class_lead": "A" }],
}
print(school_dict)

name = input("Provide name: ")
last_name = input("Provide last name: ")
students_class = input("Provide class for this student: ")

temp_dict = {
  "f_name": name,
  "l_name": last_name,
  "class_attended": students_class
}


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
def create_account(key):
    while True:
        if key == "student":
            f_name= input("Provide the first name:  ")#student_account():
            l_name = input("Provide the last name:  ")
            class_attended = input("Provide the class name: ")
            temp_dict = {}
            temp_dict['f_name'] = f_name
            temp_dict['l_name'] = l_name
            temp_dict['class_attended'] = class_attended
            school_dict["student"].append(temp_dict)
            print("The student has been created.")           
            break
        elif key == "teacher": #teacher_account():
            f_name = input("Provide the first name:  ")
            l_name = input("Provide the last name:  ")
            subject = input("Provide the subject name:  ")
            class_teach = input("Provide the class you teach: ")
            temp_dict = {}
            temp_dict['f_name'] = f_name
            temp_dict['l_name'] = l_name
            temp_dict['subject'] = subject
            temp_dict['class_teach '] = class_teach
            temp_dict["teacher"].append(temp_dict)
            print("The teacher has been created.")
            break
        elif key == "homeroom_teacher": #def homeroom_teacher_account():
            f_name = input("Provide the first name:  ")
            l_name = input("Provide the last name:  ")
            class_lead = input("Provide the class name you lead: ")
            temp_dict = {}
            temp_dict['f_name'] = f_name
            temp_dict['l_name'] = l_name
            temp_dict['class_lead'] = class_lead
            temp_dict["homeroom_teacher"].append(temp_dict)            
            print("The homeroom teacher has been created.")
            break
        else:
            print("It's invalid input! Please try again. ")


def manage_account(key):
    while True:
        if key == "student":
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            for student in school_dict["student"]:
                if student['f_name'] == f_name and student['l_name'] == l_name:
                    print(f"{student['f_name']} {student['l_name']} attends class {student['class_attend']} ")
                    print("Student's teachers:")
                    if student['class_attend'] == teacher['class_teach']:
                        print(f"{teacher['f_name']} {teacher['l_name']} ")

        elif key == "teacher":
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            for teacher in school_dict["teacher"]:
                if teacher ['f_name'] == f_name and teacher['l_name'] == l_name:
                    print(f"{teacher['f_name']} {teacher['l_name']} teaches class {student['class_attend']} ")

        elif key == "homeroom_teacher":
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            for homeroom_teacher in school_dict["homeroom_teacher"]:
                if homeroom_teacher['f_name'] == f_name and homeroom_teacher['l_name'] == l_name:
                    print(f"Homeroom teacher {f_name} {l_name} leads class {homeroom_teacher['class_lead']} ") #can i just put class_lead?
                    print("Student's list:")
                    if student['class_attend'] == homeroom_teacher['class_lead']:
                        print(f"{student['f_name']} {student['l_name']} ")
        #how to print class as a variable? - 
        #'class': Prompt for a class to display (e.g., "3C"), the program should list all students in the class and the homeroom teache
            search_class = input("Provide class for search: ")
            for student in school_dict["student"]:
                if student["class_attended"] == search_class:
                    print(student)
            for student in school_dict["homeroom_teacher"]:
                if homeroom_teacher["class_lead"] == search_class:
                    print(homeroom_teacher)
        
        elif key == "end":
            break
        else:
            print("It's invalid input! Please try again. ")



#print avaliable commands of school management application: create, manage and end
while True:
    greeting_message()
    option = input("Choose an option (end, create or manage): ").lower()
    if option == "create":
        create_account = input("Enter the user type you tend to create: ")
        create_account #do I need to put like create_account(key)?
    elif option == "manage":
        manage_account = input("Enter the user you tend to manage: ")
        pass #create(manage_account)
    elif option == "end":
        break
    else:
        print("It's invalid input! Please try again. ")