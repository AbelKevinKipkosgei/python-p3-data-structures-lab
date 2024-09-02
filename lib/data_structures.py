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
    spicy_foods_list = [food["name"] for food in spicy_foods]
    print(spicy_foods_list)
    return spicy_foods_list

def get_spiciest_foods(spicy_foods):
    spiciest_foods_dict_list = [food for food in spicy_foods if food["heat_level"] > 5]
    print(spiciest_foods_dict_list)
    return spiciest_foods_dict_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_foods_by_cuisine_dict = {}
    for food in spicy_foods:
        if cuisine.title() == food["cuisine"]:
            if cuisine.title() not in spicy_foods_by_cuisine_dict:
                spicy_foods_by_cuisine_dict.update(food)
    print(spicy_foods_by_cuisine_dict)
    return spicy_foods_by_cuisine_dict

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    heat_level_list = [food["heat_level"] for food in spicy_foods]
    average_heat_level = sum(heat_level_list) / heat_level_list.__len__()
    print(heat_level_list)
    print(average_heat_level)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_food = [food for food in spicy_foods]
    new_spicy_food.append(spicy_food)
    print(new_spicy_food)
    return new_spicy_food

get_names(spicy_foods)
get_spiciest_foods(spicy_foods)
print_spicy_foods(spicy_foods)
get_spicy_food_by_cuisine(spicy_foods, "american")
print_spiciest_foods(spicy_foods)
get_average_heat_level(spicy_foods)
create_spicy_food(spicy_foods, {'name': 'Griot',
                                'cuisine': 'Haitian',
                                'heat_level':10})