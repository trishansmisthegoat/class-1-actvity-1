print("Hello! I am not AI Bot . What's your name? : ")

name = input()

print(f"Nice to meet you {name}")

print("How are you feeling today? (good/bad) : ")

mood = input().lower()

if mood == "good":
    print("i'm glad to hear that!")
elif mood == "good ":
    print("i'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. hope thigs get better soon.")
else:
    print("I see. Sometimes its hard to put feelings into words.")

    print(f"It was nice chatting with you {name}. Goodbye!")