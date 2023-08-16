spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
   #return [foods['name'] for foods in spicy_foods ]
    food =[]
    for foods in spicy_foods:
       food.append(foods['name'])
    return food   
       
def get_spiciest_foods(spicy_foods):
    #return [foods for foods in spicy_foods if foods['heat_level'] > 5]
    food = []
    for foods in spicy_foods:
        if foods['heat_level'] > 5:
            food.append(foods)
        return food    

def print_spicy_foods(spicy_foods):
    for foods in spicy_foods:
        heat_level = foods['heat_level']
        chilli = "🌶" * heat_level
        print(f"{foods['name']} ({foods['cuisine']}) | Heat Level: {chilli}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for foods in spicy_foods:
        if cuisine.lower() == foods['cuisine'].lower():
            return foods

def print_spiciest_foods(spicy_foods):
    for foods in spicy_foods:
        heat_level = foods['heat_level']
        chilli = "🌶" * heat_level
        if foods['heat_level'] > 5:
            print(f"{foods['name']} ({foods['cuisine']}) | Heat Level: {chilli}")

def get_average_heat_level(spicy_foods):
    sum = 0
    for foods in spicy_foods:
        sum = sum + foods['heat_level']
        avg = sum / len(foods)
    return avg

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
