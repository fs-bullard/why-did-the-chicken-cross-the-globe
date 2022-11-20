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
            for category in eval(recipe[8]):
                if category:
                    for food_type in category_map[category]:
                        if food_type == ingredient.lower():
                            include = True
            include_list.append(include)
        if all(term is True for term in include_list):
            return_recipe_list.append(recipe[1])

    return return_recipe_list

        
