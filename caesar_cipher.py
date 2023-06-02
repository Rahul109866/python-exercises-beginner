alphabet = 'abcdefghijklmnopqrstuvwxyz ' # this is the accepted set of charecters in our to-be encrypted message 


secret_info = input("Enter the message to be encrypted\n").lower()
#this is the string we are going to encrypt

cipher = int(input('Enter the shift\n'))
#our cipher key

for charecter in secret_info:
    #for edge cases where the message contains charecters outside of our accepted charecter set
    if charecter not in alphabet:
        print("Invalid")
    
    else:
        if charecter == " ":
            print(">", end="") #just a symbol substitution for white space
        else:
            position = (alphabet.lower().index(charecter) + cipher) % 27
            # find the index of each charecter in our message and shift it
            #modulo math ensures we get cyclic rotations in our charecter set
   
            print(alphabet[position],end="") #print it in a single line
       

