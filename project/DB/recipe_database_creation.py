import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from variables import category_map

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
                if term in ingredient['ingredientText']:
                    category = key
        categories.append(category)
        try:
            quantities.append(ingredient['quantityText'])
        except:
            quantities.append(None)        



    recipe_database.append({'title': title,
                     'description': description,
                     'url': url,
                     'tags': tags,
                     'nutrition_info': nutrition_info,
                     'serves': int(serves),
                     'ingredients': ingredients,
                     'categories': categories,
                     'quantities': quantities})

    for i in range(len(ingredients)):
        all_lists_database.append({'title': title,
                        'description': description,
                        'url': url,
                        'tags': tags,
                        'nutrition_info': nutrition_info,
                        'serves': int(serves),
                        'ingredients': ingredients[i],
                        'categories': categories[i],
                        'quantities': quantities[i]})


df1 = pd.DataFrame.from_dict(recipe_database)
df1.to_excel('project/DB/recipe_database.xlsx')

df2 = pd.DataFrame.from_dict(all_lists_database)
df2.to_excel('project/DB/all_list_database.xlsx')



                     

