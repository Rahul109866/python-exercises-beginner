student_scores=input("Enter the scores of the students seperated by a space: \n").split(" ")
for integers in range(0,len(student_scores)):
    student_scores[integers]=int(student_scores[integers])
    
    
max=0
for n in range(1,len(student_scores)):
    if student_scores[n]<student_scores[n-1]:
        student_scores[n]=student_scores[n-1]
        

        
print(student_scores[-1])
