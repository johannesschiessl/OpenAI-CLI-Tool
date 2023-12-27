def quit(user_name):
    print(f"🧠 Assistant: 👋 Bye, {user_name}!")
    exit()

def help():
    print("📚 Available commands:")
    print("     /imagine - Generate an image")
    print("     /quit - Exit the program")
    print("     /help - Display the list of commands")

def imagine(prompt):
    print(prompt)

def error():
    print("❌ Invalid command. Please try again.")

