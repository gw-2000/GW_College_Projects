print("Hello there! Please enter a word, and I will check to see if it's",
      "a palindrome.")
redo = "yes"
while redo == "yes":
    word1 = str.lower(input("Please enter your word here:"))
    # This is the function I created
    def palfunct(word1):
        word1 = word1.replace(" ","")
        if word1 == word1[::-1]:
            print ("\nThis is a Palindrome")
        else:
            print("\nThis is not a Palindrome")
    #End of the function
    print ("Checking for Palindrome...")
    #function call here
    palfunct(word1)

redo = str.lower(input("\n\nWould you like to enter another word? Input Yes/No:"))

input("\nPress enter to leave:")


    




        
    



    
    
    
