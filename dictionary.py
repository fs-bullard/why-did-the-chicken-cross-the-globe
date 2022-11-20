#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 22:45:39 2022

@author: charlottebottomley
"""

import numpy as np

conversion_dic = {
    "g" : 0.001,
    "kg" : 1,
    "l": 1,
    "ml": 0.001,
    "tsp": 0.00492892,
    "tbsp": 0.015,
    }

quantities = [
        ['4 tbsp', '1', '2', '¼ tsp', '2 x 400g cans chopped', '1 tsp', '6 tbsp', '4', '300g', '70g', '50g', '½ small bunch of'],
        ['120g', '1', '2', '1 tsp', '80g', '600g', '400g can', '100ml', '1', None],
        ['3', '2', '8 tbsp', '300g', '125g', 'handful'],
        ['100g', '160g', '50g', '3', '½ tsp', 'good handful', '2 tsp', 'few drops', '1 tbsp', '2', '280g'],
        ['1kg', '4 tbsp', '6', None, '6 tbsp', '6 tbsp', '4'],
        ['200g', '1 tbsp', '1 tbsp', '200ml', '½ tsp', '100g', '200g', '50g', '50g', '1', '1 tbsp', None],
        ['1 tbsp', '200g', '30g', '100g', '2 tsp', '1', '1½ tbsp', '1kg', '500g', '320g'],
        ['1½kg boneless ', '2', '2 tbsp', '1 tbsp', '1', '2', '432g can ', '2 tsp', '2 tsp', '1 tsp', '1 tsp', 'grating of fresh '],
        ['2½ tbsp', '1kg', '100g', '2', '2', '200g', '3 tbsp', '1 tbsp', '150ml', '2', '1', '375g'],
        ['2 tbsp', '1', '1', '400g can', '100ml', '200g', '3 tbsp', '½ tbsp', '2'],
        ['1½ tbsp', '1', '2', '1', '½ tsp', '2 x 400g cans chopped', '100g', '500ml', '12', '150g', '½ small bunch of', None],
        ['400g', '1 tbsp', '½ tbsp dried', '1', '½ tsp', '100ml', '1', '½', '2', '2', None, None],
        ['70g', '70g', '1l', '1', '80g', '2 tsp', 'pinch of ', '600g', '250g', '1 whole ', '300g', '12', '50g'],
        ['1', '25g', '1', '1', '1', 'small handful of', '500g Maris Piper or', '10 pitted', '100ml chicken or'],
        ['350g', '200ml', '2 tbsp', '400g', '4', '1 tbsp', '150ml', '1 tsp', '200g', '1 tsp', '250g'],
        ['240g', 'knob of', '1', '140g', '2', '140g', '½', 'small bunch of'],
        ['650ml', '40g', '40g', '2 tsp', '150g', '180g', 'handful of ', '300g', '300g', None],
        ['350g', '1 tsp', '1 tsp', '1½ tbsp ', '1 large ', '3', '1 tbsp', '2 x 400g cans chopped ', '2 tsp', '150g ball ', '4', '25g', None],
        ['1 tbsp', '2 tbsp', '1½ tbsp', '8', '1', '1', '2 tbsp', '125g', '1', '3', '4'],
        ['700g', '2 tbsp', '1', '4', 'small bunch of ', '4', None, '½ tsp ', '300g'],
        ['1', '200g', '3 tbsp', '400g can ', '2', '1 large or 2 small ', '2 tbsp', None],
        ['1', '1 thumb-sized piece', '2', '1 tbsp', '2-3 tbsp', '400g can chopped', '2 tbsp', '½ tbsp', '3', '200g', '3 tbsp', '300g', '1 tbsp', '½ bunch of', None],
        ['2', '1 tbsp', '4 tbsp', '2 tbsp', '3', '1', '1 tbsp', '300g', '50ml', '1 tbsp', '4', '1'],
        ['300g', '300g', '1 tbsp', '1 large bunch of', '1 large', '2 tbsp', '1 tbsp', '50g', '200g']
       ]
serves = [6,4,6,2,4,2,4,6,6,2,4,4,6,2,4,3,6,3,4,3,2,4,4,4]

syntaxed_quantities = []
for quantity in quantities[0]:
    syntaxed_quantity = quantity
    if '½' in syntaxed_quantity:
        syntaxed_quantity = quantity.replace('½', '.5')
    if '¼' in syntaxed_quantity:
        syntaxed_quantity = quantity.replace('¼', '.25')
    syntaxed_quantities.append(syntaxed_quantity)


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
    kg_quantities.append(kg_quantity*multiplier)

print(kg_quantities)

