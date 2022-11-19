from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

recipe_database = []
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
    serves = json_object['props']['pageProps']['servings'].split(' ')[-1]
    description = json_object['props']['pageProps']['description'][3:-4]
    url = json_object['props']['pageProps']['image']['url']
    nutrition_info = json_object['props']['pageProps']['permutiveModel']['recipe']['nutrition_info']
    tags = json_object['props']['pageProps']['permutiveModel']['article']['tags']
    ingredients = []
    quantities = []

    for ingredient in json_object['props']['pageProps']['ingredients'][0]['ingredients']:
        ingredients.append(ingredient['ingredientText'])
        try:
            quantities.append(ingredient['quantityText'])
        except:
            quantities.append(None)

    recipe_database.append({'title': title,
                     'description': description,
                     'url': url,
                     'tags': tags,
                     'nutrition_info': nutrition_info,
                     'tags': tags,
                     'ingredients': ingredients,
                     'quantities': quantities})


df = pd.DataFrame.from_dict(recipe_database)
df.to_excel('recipe_database.xlsx')
                     

