import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

category_map = {
    'Apples': ['apples', 'apple'],
    'Bananas': ['bananas', 'banana'],
    'Barley': ['barley'],
    'Beef (beef herd)': ['beef (beef herd), beef', 'venison'],
    'Berries & Grapes': ['berries & grapes, berry', 'grape'],
    'Brassicas': ['brassicas', 'brassica'],
    'Cane Sugar': ['cane sugar', 'sugar'],
    'Cassava': ['cassava'],
    'Cheese': ['cheese', 'mascarpone', 'cheddar', 'mozzarella', 'parmesan', 'ricotta'],
    'Citrus Fruit': ['citrus fruit', 'lemon'],
    'Coffee': ['coffee'],
    'Dark Chocolate': ['dark chocolate', 'chocolate'],
    'Eggs': ['eggs', 'egg'],
    'Fish (farmed)': ['fish (farmed)', 'fish', 'cod', 'anchovy', 'salmon'],
    'Groundnuts': ['groundnuts', 'nut', 'nutmeg', 'almond', 'pine'],
    'Lamb & Mutton': ['lamb & mutton', 'lamb', 'mutton'],
    'Maize': ['maize', 'corn'],
    'Milk': ['milk', 'butter', 'yoghurt', 'crème', 'creme', 'cream'],
    'Oatmeal': ['oatmeal', 'oat', 'oats'],
    'Onions & Leeks': ['onions & leeks', 'onion', 'leak', 'garlic', 'shallot'],
    'Other Fruit': ['other fruit', 'fruit', 'fruits', 'pineapple', 'cucumber', 'cornichon'],
    'Other Pulses': ['other pulses', 'pulse', 'pulses', 'lentils', 'bean', 
        'green olive', 'caper', 'chickpea'],
    'Other Vegetables': ['other vegetables', 'vegtable', 'vegtables', 'oil', 'peppers',
         'aubergine', 'kale', 'salad', 'chipotle', 'mushroom', 'spinach', 
         'basil', 'lettuce', 'broccoli', 'avocado', 'cabbage', 'carrot'],
    'Peas': ['peas', 'pea'],
    'Pig Meat': ['pig meat', 'pig', 'pork', 'bacon', 'chorizo', 'ham', 'pancetta'],
    'Potatoes': ['potatoes', 'potato', 'gnocchi'],
    'Poultry Meat': ['poultry meat', 'poultry', 'chicken',  'turkey'],
    'Prawns (farmed)': ['prawns (farmed)', 'prawn', 'prawns'],
    'Rice': ['rice', 'couscous'],
    'Root Vegetables': ['root vegetables', 'root vegetable'],
    'Soy milk': ['soy milk', 'soy'],
    'Tofu': ['tofu'],
    'Tomatoes': ['tomatoes', 'tomato', 'ketchup'],
    'Wheat & Rye': ['wheat & rye', 'bread', 'pasta', 'penne', 'lasagne sheet', 
        'flour', 'breadcrumb', 'pastry', 'fusilli', 'macaroni'],
    'Wine': ['wine'],
    }

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
                     'serves': serves,
                     'tags': tags,
                     'ingredients': ingredients,
                     'categories': categories,
                     'quantities': quantities})


df = pd.DataFrame.from_dict(recipe_database)
df.to_excel('project/DB/recipe_database.xlsx')
                     

