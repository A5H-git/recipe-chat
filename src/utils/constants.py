from enum import Enum

MAX_INGREDIENT_TOKENS = 100
MAX_CUISINE_TOKENS = 50

DIVIDER_COLOR = "red"

class IngredientOpts(Enum):
    MISSING = "Include ingredients I might not have"
    SUBS = "Suggest alternatives to fit dietary restrictions, if any"

class DietaryRestrictOpts(Enum):
    GLUTEN_FREE = "Gluten Free"
    DAIRY_FREE = "Dairy Free"
    HALAL = "Halal"
    KOSHER = "Kosher"
    VEGAN = "Vegan"
    VEGETARIAN = "Vegetarian"
    PESCATARIAN = "Pescatarian"
