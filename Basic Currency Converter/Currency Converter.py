print ("CURRENCY CONVERTER")

print("Welcome to the Currency Converter")

redo = "yes"
while redo == "yes":

    print("Please use the words 'euro', 'pound' or 'dollar'")
    currency = input("Please enter a Currency:")

    excurrency = input ("What currency would you like to convert into? Enter Here:")
          
    amount = float(input("Enter amount you would like to convert:"))
    dollar1 = float(1.10433)
    pound1 = float(0.88662)
    dollar2 = float(1.29953)
    euro1 = float(1.12783)
    pound2 = float(0.769644)
    euro2 = float(0.867893)
    answer = float(0)

    if currency == 'euro' and excurrency == 'dollar':
        answer = amount * dollar1
    elif currency == 'euro' and excurrency == 'pound':
        answer = amount * pound1
    elif currency == 'pound' and excurrency == 'dollar':
        answer = amount * dollar2
    elif currency == 'pound' and excurrency == 'euro':
        answer = amount * euro1
    elif currency == 'dollar' and excurrency == 'pound':
        answer = amount * pound2
    elif currency == 'dollar' and excurrency == 'euro':
        answer = amount * euro2
    elif currency != ['dollar','euro','pound']:
        print("Error. Try Again.")
    elif excurrency != ['dollar','euro','pound']:
        print("Error. Try Again.")
    
    print("Calculating your exchange rate...\nThe Conversion is...",
          answer, excurrency)
    

    redo = str.lower(input("\n\nWould you like to try again? Input Yes/No:"))

    if redo != "yes":
        input("\n\nPress Enter to leave")

