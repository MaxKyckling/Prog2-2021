run = 1
while run == 1:
    line = input("Välj två tal som ska adderas")
    a, b = line.split()
    a = int(a)
    b = int(b)
    if a < 0 or b < 0 or a > 1000000 or b > 1000000:
        print("Talet måste vara mellan 0 och 1000000")
        run = 1
        break
    else:
        try:
            print(a+b)
            answer = input("Vill du addera igen?")
            try:
                if answer == "y":
                    run = 1
                    break
                if answer == "n":
                    run = 0
                    break
            except:
                print("Något gick fel")
        except:
            print("Något gick fel, försök igen!")
            run = 1
            break



