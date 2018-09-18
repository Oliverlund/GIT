print("*** Hej och välkommen till Pizzamakaren ***")
topping = ""
meny = 0
while meny != 3:
    print("1. Skriv in ditt val av topping\n"
    + "2. Skriv ut ditt val av topping\n"
    + "3. Avsluta och beställ pizzan. ")
    try:
        meny = int(input("Gör ett val från menyn: "))
    except:
        print("Du måste ange en siffra!")

    if meny == 1:
        topping += input("Skriv in den önskade toppingen: ") + ", "
    elif meny == 2:
        print("Din valda topping är: ", topping)
    elif meny == 3:
        print("Hej då!")
    else: 
        print("Du gjorde inte ett korrekt val, prova igen.")

