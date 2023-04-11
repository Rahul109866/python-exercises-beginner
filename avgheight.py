student_heights=input("Enter the heights seperated by space!").split(" ")
totalheight=0
counter=0
for i in student_heights:
    #print(i)
   
    totalheight+=int(i)
    counter+=1
    
avgheight=round(totalheight/counter)
print(avgheight)
    
