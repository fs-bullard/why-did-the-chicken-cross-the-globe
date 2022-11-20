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

conversion_dic = {
    "g" : 0.001,
    "kg" : 1,
    "l": 1,
    "ml": 0.001,
    "tsp": 0.00492892,
    "tbsp": 0.015,
    }

def get_possible_foods():
    possible_foods = []
    for key in category_map.keys():
        for food in category_map[key]:
            possible_foods.append(food)
    return possible_foods
