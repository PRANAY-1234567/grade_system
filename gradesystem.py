total_marks=0
for i in range (6):
    marks=int(input(f"Enter the numbers {i}"))
    total_marks+=marks
    print(total_marks)
avg=total_marks/6
print(avg)
if(avg>=95):
    b="A+"
elif(avg>=85):
    b="A"
elif(avg>=70):
    b="B"
elif(avg>=60):
    b="C"
elif(avg>35):
    b="D"
else:
    b="FAILL"
print(b)