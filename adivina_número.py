
number_to_guess = 2

user_number = int(input("Adivina un número: "))

if number_to_guess == user_number:
    print("Has ganado")
if number_to_guess > user_number:
    print("Estas cerca")
if number_to_guess < user_number:
    print("Te vas alejando")
if user_number == 69:
    print("Samsara")
else:
    print("Has Perdido")
