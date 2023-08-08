pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}
def check_pantry(ingrediants):
    for ingrediant in ingrediants:
        if ingrediant not in pantry or pantry[ingrediant] < 1:
            return False
    return True

def reduce_pantry(ingrediants):
    for ingrediant in ingrediants:
        pantry[ingrediant] -=1

def print_pantry():
    for ingrediant,quantity in pantry.items():
        print(f"{ingrediant.capitalize()}: {quantity}")

def print_recipies():
    for index , recipe in enumerate(recipes):
        print(f"{index + 1}: {recipe}")

while True:
     print("\nWhat would you like to do?")
     print("1. See available recipes")
     print("2. Cook a recipe")
     print("3. Check pantry quantities")
     print("4. Quit")

     choice = input("Enter your choice (1-4): ")

     if choice == "1":
        print("\nAvalible recipes: ")
        print_recipies()
     elif choice == 2:
         recipe_choice = input("\nEnter the number of the recipe you want to cook: ") 
         recipe_choice = int(recipe_choice) - 1

         if recipe_choice < 0 or recipe_choice >= len(recipes):
             print("Invalid recipe number.")
             continue
