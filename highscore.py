student_scores=input("Enter the scores of the students seperated by a space: \n").split(" ")
for integers in range(0,len(student_scores)):
    student_scores[integers]=int(student_scores[integers])
    
    
max=student_scores[0]
for num in student_scores:
    if num>max:
        max=num
        

        
print(f"The highest score is: {max}")
