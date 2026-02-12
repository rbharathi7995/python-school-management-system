students={
    20:{
        "name":"Bharathi",
        "age":18,
        "marks":(100,99,98),
        "section":"CSE"
    },
    21:{
        "name":"Sowjanya",
        "age":17,
        "marks":(99,91,95),
        "section":"ECE"
    },
    22:{
        "name":"Ranjana",
        "age":19,
        "marks":(97,90,98),
        "section":"ECE"
    }
}
while True:
    print("1.Add Student")
    print("2.Display All")
    print("3.Search")
    print("4.Remove")
    print("5.Class Topper")
    print("6.Sections")
    print("Exit")
    
   
    try:
        option=int(input("enter your option:"))
        if(option==1):
            roll=int(input("Enter roll number"))
            if roll in students:
                print("Already Exists")
            else:
                print("ADD DETAILS:")
                name=input("Enter student name")
                age=int(input("Enter student's age"))
                maths=int(input("Enter maths marks"))
                C=int(input("Enter C marks"))
                Eng=int(input("Enter english marks"))
                marks=(maths,C,Eng)
                section=input("Enter section")
                
                students[roll]={
                    "name":name,
                    "age":age,
                    "marks":marks,
                    "section":section
                }
        elif(option==2):
            if (students=={}):
                print("There is no data")
            else:
                for i in students:
                    print(i)
                    print(students[i])
        elif(option==3):
            roll=int(input("Enter student's roll number:"))
            if roll in students:
                print(roll)
                print(students[roll])
            else:
                print("Student details not found")
        elif(option==4):
            roll=int(input("Enter student's roll number:"))
            if roll in students:
                del students[roll]
               # print(students)
            else:
                print("Student details not found")
        elif(option==5):
            if not students:
                print("There is no data")
            else:
                max_total=0
                stu_roll=None
                for roll in students:
                   # manual way
                   # data=students[roll]["marks"]
                   #total=0
                    #for i in data:
                      #  total=total+i
                    total=sum(students[roll]["marks"])
                    if(total>max_total):
                        max_total=total
                        stu_roll=roll
                print("Class Topper:")
                print(students[stu_roll])
        elif(option==6):
            sets=set()
            for roll in students:
                section=students[roll]["section"]
                sets.add(section)
            print(sets)
            
        else:
            break
                
    except:
        print("invalid input")    
        
    