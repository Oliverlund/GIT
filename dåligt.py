firstname = input("Skriv ditt förnamn: ")
lastname = input("Skriv ditt efternamn: ")
print("Hej och välkommen till mitt program ", firstname)
age = 0
while age == 0:
    try: 
        age = int(input("Skriv din ålder: "))
    except:
        print("Du måste ange en siffra!")

    if age == 18:
        print("Du är exakt 18 år gammal")
    elif age >= 18:
        print("Du är gammal nog att köra programmet, grattis!")
    else:
        print("Hej då!") 


