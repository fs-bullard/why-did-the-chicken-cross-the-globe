import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from variables import category_map, conversion_dic

recipe_database = []
all_lists_database = []
collection = requests.get("https://www.bbcgoodfood.com/recipes/collection/easy-dinner-recipes")
soup = BeautifulSoup(collection.content, 'html.parser')
links = soup.find_all("a",{"class":"link d-block"})

for link in links:
    page_url = "https://www.bbcgoodfood.com" + link['href']
    recipe = requests.get(page_url)
    new_soup = BeautifulSoup(recipe.content, 'html.parser')
    details = new_soup.find("script",{"type":"application/json",
                                               "id":"__NEXT_DATA__"})
    json_object = json.loads(details.contents[0])


    title = json_object['props']['pageProps']['title']
    serves = json_object['props']['pageProps']['servings'].split(' ')[1]
    if 'enough' in serves:
        serves = 3
    description = json_object['props']['pageProps']['description'][3:-4]
    url = json_object['props']['pageProps']['image']['url']
    nutrition_info = json_object['props']['pageProps']['permutiveModel']['recipe']['nutrition_info']
    tags = json_object['props']['pageProps']['permutiveModel']['article']['tags']
    ingredients = []
    categories = []
    quantities = []

    for ingredient in json_object['props']['pageProps']['ingredients'][0]['ingredients']:
        ingredients.append(ingredient['ingredientText'])
        category = None
        for key in category_map.keys():
            for term in category_map[key]:
                if term in ingredient['ingredientText'].lower():
                    category = key
        categories.append(category)
        try:
            quantities.append(ingredient['quantityText'])
        except:
            quantities.append(None) 


        syntaxed_quantities = []
        for quantity in quantities:
            syntaxed_quantity = quantity
            if quantity == None:
                syntaxed_quantity = 0
            if '½' in str(syntaxed_quantity):
                syntaxed_quantity = quantity.replace('½', '.5')
            if '¼' in str(syntaxed_quantity):
                syntaxed_quantity = quantity.replace('¼', '.25')
            syntaxed_quantities.append(str(syntaxed_quantity))

        kg_quantities = []
        for quantity in syntaxed_quantities:
            kg_quantity = quantity
            multiplier = 1
            split_quantity = quantity.split(' ')
            if 'x' in split_quantity:
                multiplier = float(split_quantity[0])
                split_quantity = split_quantity[2:] 
            if not quantity[0] in ['1','2','3','4','5','6','7','8','9','0','.']:
                kg_quantity = 0 
            elif split_quantity[0][-2:] == 'kg':
                kg_quantity = float(split_quantity[0].split('kg')[0]) * conversion_dic['kg']
            elif split_quantity[0][-1] == 'g':
                kg_quantity = float(split_quantity[0].split('g')[0]) * conversion_dic['g']
            elif split_quantity[0][-2:] == 'ml':
                kg_quantity = float(split_quantity[0].split('ml')[0]) * conversion_dic['ml']
            elif split_quantity[0][-1] == 'l':
                kg_quantity = float(split_quantity[0].split('l')[0]) * conversion_dic['l']
            elif 'tsp' in split_quantity:
                kg_quantity = float(split_quantity[0]) * conversion_dic['tsp']
            elif 'tbsp' in split_quantity:
                if '-' in split_quantity[0]:
                    kg_quantity = float(split_quantity[0].split('-')[0]) * conversion_dic['tbsp']
                else:
                    kg_quantity = float(split_quantity[0]) * conversion_dic['tbsp']
            else:
                try:
                    kg_quantity = float(quantity) * 0.1
                except:
                    kg_quantity = 0
            kg_quantities.append(kg_quantity*multiplier/int(serves))


    carbon = []
    land_use = []
    data = pd.read_excel('project/DB/food-footprints.xlsx')
    eco_data = pd.DataFrame(data).values.tolist()
    eco_dict = {}
    for datum in eco_data:
        eco_dict[datum[0]] = (datum[1], datum[2])
    for index, category in enumerate(categories):
        if category is None:
            carbon.append(0)
            land_use.append(0)
        else:
            carbon.append(eco_dict[category][0] * kg_quantities[index])
            land_use.append(eco_dict[category][1] * kg_quantities[index])
        




    recipe_database.append({'title': title,
                     'description': description,
                     'url': url,
                     'tags': tags,
                     'nutrition_info': nutrition_info,
                     'serves': int(serves),
                     'ingredients': ingredients,
                     'categories': categories,
                     'quantities': quantities,
                     'quantities_per_portion_kg': kg_quantities,
                     'carbon_emission_per_ingredient_kg': carbon,
                     'total_carbon_emission_per_portion_kg': sum(carbon),
                     'land_use_per_ingredient_m^2': land_use,
                     'total_land_per_portion_kg': sum(land_use)})

    for i in range(len(ingredients)):
        all_lists_database.append({'title': title,
                        'description': description,
                        'url': url,
                        'tags': tags,
                        'nutrition_info': nutrition_info,
                        'serves': int(serves),
                        'ingredients': ingredients[i],
                        'categories': categories[i],
                        'quantities': quantities[i],
                        'quantities_per_portion_kg': kg_quantities[i],
                        'carbon_emission_per_ingredient_kg': carbon[i],
                        'total_carbon_emission_per_portion_kg': sum(carbon),
                        'land_use_per_ingredient_m^2': land_use[i],
                        'total_land_per_portion_kg': sum(land_use)})


df1 = pd.DataFrame.from_dict(recipe_database)
df1.to_excel('project/DB/recipe_database.xlsx')

df2 = pd.DataFrame.from_dict(all_lists_database)
df2.to_excel('project/DB/all_list_database.xlsx')

import json
with open('project/DB/recipe_database.json', 'w') as f:
    json.dump(recipe_database, f)




                     

