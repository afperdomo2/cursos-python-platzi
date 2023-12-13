import random

user_option = input("🕹️ piedra, papel o tijera: ")
computer_option = random.choice(["piedra", "papel", "tijera"])

print(f"🧙 {user_option} vs {computer_option} 🤖")

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
