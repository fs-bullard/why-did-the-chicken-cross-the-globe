import numpy as np
import matplotlib.pyplot as plt
from variables import get_all_recipe_dict

def plot_bar_charts(recipes):
    plt.figure(figsize=(10,5))
    num_categories = 0
    categories = []
    for run, title in enumerate(recipes):
        recipe = get_all_recipe_dict()[title]
        if num_categories <= len(recipe['ingredients']):
            num_categories = len(recipe['ingredients'])
        
        running_height = 0
        for index in range(len(recipe['ingredients'])):
            plt.bar([run*0.2], [recipe['carbon_emission_per_ingredient_kg'][index]], width=0.1,
            bottom=[running_height], label = recipe['ingredients'][index])
            running_height += recipe['carbon_emission_per_ingredient_kg'][index]
        plt.legend()
    
    plt.xticks(np.linspace(0, len(recipes)*0.2-0.2, num=len(recipes)), recipes)
    plt.xlabel('Recipe')
    
    plt.ylabel('Carbon emissions per ingredient [kg]')
    plt.show()
plot_bar_charts(['Chicken pasta bake', 'Chicken & chorizo ragu', 'Vegetarian lasagne'])

        
        