# ============================================================
# Practical 1: Intelligent Agents
# 1. Chatbot
# 2. Recommendation Assistant
# 3. Smart Home Controller Intelligent Agent
# ============================================================

from datetime import datetime

# ------------------------------------------------------------
# 1. Intelligent Agent - Chatbot
# ------------------------------------------------------------
print("========================================")
print("        Welcome to Smart Chatbot")
print("Type 'bye' to exit")
print("========================================")

while True:
    user = input("\nYou: ").lower()
    if user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! Nice to meet you.")
    elif user == "name":
        print("Bot: I am SmartBot, your AI assistant.")
    elif user == "how are you":
        print("Bot: I am fine. Thank you!")
    elif user == "time":
        print("Bot: Current time is", datetime.now().strftime("%H:%M:%S"))
    elif user == "date":
        print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))
    elif user == "python":
        print("Bot: Python is a popular programming language used in AI.")
    elif user == "ai":
        print("Bot: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")
    elif user == "thank you":
        print("Bot: You're welcome!")
    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: Sorry, I don't understand your question.")

# ------------------------------------------------------------
# 2. Intelligent Agent - Recommendation Assistant
# ------------------------------------------------------------
print("========================================")
print("   Welcome to Recommendation Assistant")
print("========================================")
print("\nSelect your interest:")
print("1. Movies")
print("2. Books")
print("3. Music")
choice = input("\nEnter your choice (1/2/3): ")

if choice == "1":
    print("\nChoose Movie Genre:")
    print("a. Action")
    print("b. Comedy")
    print("c. Drama")
    genre = input("Enter genre (a/b/c): ")
    if genre == "a":
        print("Recommended Movie: RRR")
    elif genre == "b":
        print("Recommended Movie: Hera Pheri")
    elif genre == "c":
        print("Recommended Movie: Taare Zameen Par")
    else:
        print("Invalid Genre!")

elif choice == "2":
    print("\nChoose Book Category:")
    print("a. Mythology")
    print("b. Fiction")
    print("c. Motivation")
    category = input("Enter category (a/b/c): ")
    if category == "a":
        print("Recommended Book: The Palace of Illusions")
    elif category == "b":
        print("Recommended Book: The Guide")
    elif category == "c":
        print("Recommended Book: Wings of Fire")
    else:
        print("Invalid Category!")

elif choice == "3":
    print("\nChoose Music Type:")
    print("a. Romantic")
    print("b. Devotional")
    print("c. Party")
    music = input("Enter type (a/b/c): ")
    if music == "a":
        print("Recommended Song: Kesariya")
    elif music == "b":
        print("Recommended Song: Achyutam Keshavam")
    elif music == "c":
        print("Recommended Song: Kala Chashma")
    else:
        print("Invalid Music Type!")

else:
    print("Invalid Choice!")

print("\nThank you for using Recommendation Assistant!")

# ------------------------------------------------------------
# 3. Smart Home Controller Intelligent Agent
# ------------------------------------------------------------
print("=== Smart Home Controller ===")
while True:
    print("\n1. Motion Detection")
    print("2. Temperature Check")
    print("3. Door Status")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        motion = input("Is motion detected? (yes/no): ").lower()
        if motion == "yes":
            print("Motion detected!")
            print("Light turned ON.")
        else:
            print("No motion detected.")
            print("Light turned OFF.")

    elif choice == "2":
        temp = int(input("Enter room temperature (°C): "))
        if temp >= 30:
            print("Temperature is high.")
            print("Fan turned ON.")
        else:
            print("Temperature is normal.")
            print("Fan turned OFF.")

    elif choice == "3":
        door = input("Is the door open? (yes/no): ").lower()
        if door == "yes":
            print("Door is open.")
            print("Security Alarm ON.")
        else:
            print("Door is closed.")
            print("Security Alarm OFF.")

    elif choice == "4":
        print("Exiting Smart Home Controller...")
        break

    else:
        print("Invalid choice! Try again.")
