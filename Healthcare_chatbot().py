def healthcare_chatbot():
    print("🤖 Hi! I'm your Health Bot. Type 'quit' to stop.\n")

    while True:
        user = input("You: ").lower()

        if user == 'quit':
            print("Bot: Bye! Take care 👋")
            break

        if 'fever' in user or 'cough' in user or 'chills' in user:
            print("Bot: Sounds like a cold or flu. Rest and stay hydrated.")
        elif 'headache' in user or 'migraine' in user:
            print("Bot: Try resting in a quiet, dark room and drink water.")
        elif 'stomach' in user or 'nausea' in user or 'vomit' in user:
            print("Bot: Could be a stomach issue. Eat light and stay hydrated.")
        elif 'chest pain' in user or 'breathing' in user:
            print("Bot: Chest pain is serious. Please get emergency help.")
        else:
            print("Bot: Sorry, I’m not sure. Try describing your symptoms more clearly.")

healthcare_chatbot()