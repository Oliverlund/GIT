print("*** Välkommen till Internetbanken ***")

insattning = 0
uttag = 0
meny = 0
saldo = 0

while meny != 4:
    print("1. Insättning\n"
    +"2. Uttag\n"
    +"3. Visa saldo\n"
    +"4. Avsluta")
    
    try:
         meny = int(input("Gör ett val: "))
    except:
        print("Du måste ange en siffra!")

    if meny == 1:
        insattning = input("Ange en siffra: ")
        saldo = saldo + int(insattning)
    elif meny == 2:
        uttag = input("Ange en siffra: ")
        saldo = saldo - int(uttag)
    elif meny == 3:
        print("Din Saldo: " ,saldo)
    elif meny == 4:
        print("*** Välkommen åter ****")
    else:
        print("Du gjorde inte ett korrekt val")
    

