import random

options = ["piedra", "papel", "tijera"]

user_option = input("🕹️ Piedra, papel o tijera: ").lower()
computer_option = random.choice(options)

msg = f"🧙 {user_option.capitalize()} vs {computer_option.capitalize()} 🤖"
print(msg)

if user_option == computer_option:
    print("🟰 Empate!")
elif (
    (user_option == "piedra" and computer_option == "tijera")
    or (user_option == "papel" and computer_option == "piedra")
    or (user_option == "tijera" and computer_option == "papel")
):
    print("✅ Ganaste!")
else:
    print("❌ Perdiste!")
