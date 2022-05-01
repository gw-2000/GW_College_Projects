int_file = open("integers.txt")
first_list = []

for line in int_file:
    first_list.append(int(line.strip()))

#I will use this function to sort my numbers...

def insertion_sort(int_list):

    for i in range(1, len(int_list)):
        q = i

        while q > 0 and int_list[q] < int_list[q-1]:
            int_list[q], int_list[q - 1] = int_list[q - 1], int_list[q]
            q -= 1
    return int_list
        
answer = insertion_sort(first_list)

print('The list of numbers in the file are: ', '\n\n', first_list)
print('\n\nNumbers sorted in ascending order:  ', '\n\n',
      answer)

input("\n\n\nPress enter to leave:")

#Saving the sorted numbers to a new file
new_list = open("sorted_integers.txt", "w+")
new_list.write(str(answer))
new_list.close()




        
    



    
        
    


    








    



