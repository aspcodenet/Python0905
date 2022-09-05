finished = False
while not finished:
    print("1. Kör spelet")
    print("2. Avsluta")
    selection = ""
    while True:
        selection = input("Gör val:")
        if selection == "1" or selection == "2":
            break
    if selection == "2":
        finished = True
    elif selection == "1":
        print("Kör spelet....")

#age = int(input("Mata in din ålder"))

start = 1980
slut = 1970
year = start
while year > slut:
    print("Year is:", year)
    if year == 1972:
        print("Då föddes Stefan")
    if year == 1973:
        print("Då föddes Foppa")
    year = year - 1


for year in range(1980,1970,-1):
    print("Year is:", year)
    if year == 1972:
        print("Då föddes Stefan")
    if year == 1973:
        print("Då föddes Foppa")


for year in range(1970,1980):
    print("Year is:", year)
    if year == 1972:
        print("Då föddes Stefan")
    if year == 1973:
        print("Då föddes Foppa")



shouldPlayGame = True
while shouldPlayGame == True:
    print("Kör spelet")
    print("Visa highscore")
    inmatning = input("Vill du spela igen J/N?")
    if inmatning != "J":
        shouldPlayGame = False



while True:
    print("Kör spelet")
    print("Visa highscore")
    inmatning = input("Vill du spela igen J/N?")
    if inmatning != "J":
        break



x = 10
while x > 0:
    print("Nu är x ", x)
    x = x -1
print("Klart")    

# if age > 6:
#     print("Du går i skolan")
# while KLOCKAN > 9 and KLOCKAN < 16:
#     print("Du går i skolan")
#     print("Hej")

print("Klart")    




