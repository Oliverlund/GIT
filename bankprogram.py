print("*** Välkommen till Internetbanken ***")
Insättning = ""
Uttag = ""
meny = 0
while meny != 4:
    print("1. Insättning\n"
    +"2. Uttag\n"
    +"3. Visa saldo"
    +"4. Avsluta")
    try:
         meny = int(input("Välj vad du vill göra: ")
    except:
        print("Du måste ange en siffra!")

    if meny == 1:
        Insättning += input("Ange en siffra: ") 
    elif meny == 2:
        Uttag += input("Ange en siffra: ")
    elif meny == 3:
        print("Din Saldo:" Instättning+Uttag)
    elif meny == 4:
        print("*** Välkommen åter ****")
    else:
        print("Du gjorde inte ett korrekt val")
    

