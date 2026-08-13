#lesson1.py The core fundamentals of Python scripting.

# ---- STEP 1: Introduction ---
print("=== Welcome to My IT Journey ===")
print("Let's build your custom introduction profile.\n")
# ---- STEP 2: Collecting Information ----
name = input("What is your name? ")
age = input("How old are you? ")
location = input("Where are you from? ")
# ---- STEP 3: Displaying the Profile ----
print("\n=== Your Custom Introduction Profile ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Location: {location}")
# --- STEP 4: Conclusion ---
print("\n--- Career Path Advice ---")
field=input("Which area of IT interests you most ? (cybersecurity, / coding / business): ").lower().strip()
if field == "cybersecurity":
    print("Awesome! Cybersecurity is critical for proctecting networks and systems.")
elif field == "coding":
    print("Great choice! Software development lets you build awesome applications.")
elif field == "business":
    print("Nice! Combining IT with business opens up roles in tech management and analysis. are valuable in IT management and strategy.")
else:
    print("That sounds like an exciting area! Tech has endless possibilities.")