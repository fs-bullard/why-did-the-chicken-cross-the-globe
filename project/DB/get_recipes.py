from variables import get_possible_foods, category_map
import pandas as pd

def get_recipes(ingredients):
    data = pd.read_excel('project/DB/recipe_database.xlsx')
    df = pd.DataFrame(data)
    return_recipe_list = []

    for recipe in df.values.tolist():
        include_list = []
        for ingredient in ingredients:
            include = False
            for category in eval(recipe[9]):
                if category:
                    for food_type in category_map[category]:
                        if food_type == ingredient.lower():
                            include = True
            include_list.append(include)
        if all(term is True for term in include_list):
            return_recipe_list.append(recipe[1])

    return return_recipe_list

def get_recipe_data(recipes):
    data = pd.read_excel('project/DB/recipe_database.xlsx')
    df = pd.DataFrame(data)
    recipes_data = {}
    for recipe_data in df.values.tolist():
        if recipe_data[1] in recipes:
            recipes_data[recipe_data[1]] = {
                'description': recipe_data[2], 
                'url': recipe_data[3],
                'image': recipe_data[4],
                'ingredients': recipe_data[8],
                'carbon_footprint': recipe_data[13],
                'land_use': recipe_data[15],
            }
    return recipes_data
