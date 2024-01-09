import random

options = ("piedra", "papel", "tijera")

user_wins = 0
computer_wins = 0

rounds_to_win = 3
rounds = 1

while True:
    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)

    print("🧙user wins:", user_wins)
    print("🤖computer wins:", computer_wins)

    while True:
        user_option = input("🕹️ ¿Piedra, papel o tijera?:").lower()
        if user_option in options:
            break
        print("🚫 Opción inválida")

    computer_option = random.choice(options)

    print("Jugando...")
    msg = f"🧙 {user_option.capitalize()} vs {computer_option.capitalize()} 🤖"
    print(msg)

    if user_option == computer_option:
        print("🟰 Empate!")
    elif (
        (user_option == "piedra" and computer_option == "tijera")
        or (user_option == "papel" and computer_option == "piedra")
        or (user_option == "tijera" and computer_option == "papel")
    ):
        user_wins += 1
        print("✅ Ganaste!")
    else:
        computer_wins += 1
        print("❌ Perdiste!")

    # Partida finalizada
    if user_wins == rounds_to_win or computer_wins == rounds_to_win:
        print("\nPartida finalizada:")
        if user_wins == rounds_to_win:
            print("🎉🎉🎉 Ganaste la partida!")
        else:
            print("👎👎👎 Perdiste la partida!")
        break
    rounds += 1
    print("\n")
