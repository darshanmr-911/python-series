name=input("Enter the student Name:")
usn=input("Enter the usn:")
mark1=int(input("Enter the marks1:"))
mark2=int(input("Enter the marks2:"))
mark3=int(input("Enter the marks3:"))
total_marks=mark1+mark2+mark3
percentage=(total_marks/300)*100
print()
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")