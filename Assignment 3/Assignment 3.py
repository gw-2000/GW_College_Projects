N = 0
evennum = 0
sqrsum = 0 
redo = "yes"
while redo == "yes":
    N = int(input("Please enter a number:"))
    print("All the even numbers between 1 and the number you have chosen",
          "\nwill be squared and added together...")
    while evennum<N-1:
            evennum += 2
            sqrsum = sqrsum + evennum * evennum
    print("Your answer is:" , sqrsum)

    redo = str.lower(input("Would you like to enter another number? Please Input Yes/No:"))

input("\n\nPress enter to leave:")
        





          
    

    
    

        
