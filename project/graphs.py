import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from variables import get_all_recipe_dict, get_all_recipe_list

def plot_bar_charts(recipes):
    plt.figure(figsize=(10,5))
    num_categories = 0
    categories = []
    for run, title in enumerate(recipes):
        recipe = get_all_recipe_dict()[title]
        if num_categories <= len(recipe['categories']):
            num_categories = len(recipe['categories'])
        
        running_height = 0
        for index in range(len(recipe['categories'])):
            if not recipe['categories'][index] is None:
                plt.bar([run*0.2], [recipe['carbon_emission_per_ingredient_kg'][index]], width=0.1,
                bottom=[running_height], label = recipe['categories'][index])
                running_height += recipe['carbon_emission_per_ingredient_kg'][index]
    
    plt.xticks(np.linspace(0, len(recipes)*0.2-0.2, num=len(recipes)), recipes)
    plt.xlabel('Recipe')
    plt.legend(prop={'size': 5})
    plt.ylabel('Carbon emissions per ingredient [kg]')
    plt.show()

#plot_bar_charts(['Chicken pasta bake', 'Chicken & chorizo ragu', 'Vegetarian lasagne'])

def plot_pie_charts(recipes):
    plt.figure(figsize=(10,5))
    for title in recipes:
        recipe = get_all_recipe_dict()[title]
        plt.pie(recipe['carbon_emission_per_ingredient_kg'], labels=recipe['ingredients'], shadow=True)
    plt.show()

#plot_pie_charts(['Chicken pasta bake'])

def fake_history():
    all_recipes = get_all_recipe_list()
    plt.figure(figsize=(10,5))
    dates = ['{}th'.format(i+1) for i in range(3,20)]
    random_i = [random.randint(0, len(all_recipes)-1) for i in range(3,20)]
    x = []
    y = []
    for index,date in enumerate(dates):
        x.append(date)
        y.append(all_recipes[random_i[index]]['total_carbon_emission_per_portion_kg'])
    plt.plot(x, y, linestyle='-', marker='o')
    plt.xlabel('Day of meal in November')
    plt.ylabel('Total Carbon emissions per portion of meal [kg]')
    plt.title('Tracking the carbon footprint history of your meals:')
    plt.ylim(bottom=0)
    plt.show()

fake_history()

            


        
        