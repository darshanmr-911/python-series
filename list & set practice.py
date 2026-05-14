if __name__ == "__main__":                  #main function to execute the program
    record=[]                           #list to store the name and marks of the students
    s=set()                              #set to store the unique marks of the students
    for _ in range(int(input("Enter the number of students:"))):    #loop to input the number of students
        name=input("Enter the name of the student:")                 #input the name of the student
        marks=float(input("Enter the marks of the student:"))         #input the marks of the student
        record.append([name,marks])                                  #add the name and marks to the list
        s.add(marks)                                                #add the marks to the set
    sec_high_marks=sorted(s)[-2]                                    #sort the set and get the second highest marks      
    sec_high_name=[]                                                #list to store the name of the students with the second highest marks
    for name,marks in record:                                      #loop to iterate through the list and get the name and marks of the students
        if marks==sec_high_marks:                                    #if the marks of the student is equal to the second highest marks, then add the name of the student to the list
            sec_high_name.append(name)                               #add the name of the student to the list
        for name in sorted(sec_high_name):                           #print the name of the students with the second highest marks
            print(name)                                               #print the name of the students with the second highest marks




record=[]
s=set()
for _ in range(int(input("Enter the number of student:\t"))):
    name=input("Enter the student name:\t")
    marks=int(input("Enter the marks of the student:\t"))
    record.append([name,marks])
    s.add(marks)
second_low_marks=sorted(s)[1]
second_low_name=[]
for name,marks in record:
    if marks==second_low_marks:
        second_low_name.append(name) 
    for name in sorted(second_low_name):
        print(name)


            