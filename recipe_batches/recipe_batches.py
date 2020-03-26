#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe_amounts = [*recipe.values()]
  ingredient_amounts = [*ingredients.values()]
  max_batches = ingredient_amounts[0] // recipe_amounts[0]

  for i in recipe:
    if ingredients.get(i):
      ratio = ingredients[i] // recipe[i]
      if ratio < max_batches:
        max_batches = ratio
      else:
        max_batches = max_batches
    else:
      max_batches = 0

  return max_batches

recipe = { 'milk': 2, 'sugar': 40, 'butter': 20 }
ingredients = { 'milk': 5, 'sugar': 120, 'butter': 500 }

print(recipe_batches(recipe, ingredients))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))