import streamlit as st
from utils.constants import (
    MAX_CUISINE_TOKENS,
    MAX_INGREDIENT_TOKENS,
    DIVIDER_COLOR,
    IngredientOpts,
    DietaryRestrictOpts,
)


def home():
    st.title("Recipe Chat")
    st.subheader("Your personal recipe bot.")
    st.write("Fill out the form to personalize your recipe!")
    _recipe_form()


def _recipe_form():
    with st.form("Recipe Form"):
        st.write("Fill in each section of the form to help me understand more about what you want.")

        st.header("Ingredients", divider=DIVIDER_COLOR)

        st.write("""Enter your ingredients in the box
            below to generate a recipe. You may include as many
            or as little ingredients as you want.""")

        st.info(
            """Ingredients can be added separated by commas. \n
            For example: Chicken thighs, brie cheese, spaghetti, ...""",
            icon = "💡",
        )

        ingredients = st.text_area(
            label="Enter ingredients in your pantry:",
            value=None,
            max_chars=MAX_INGREDIENT_TOKENS,
        )

        st.header("Options", divider=DIVIDER_COLOR)

        st.subheader("Cuisine")
        cuisine = st.text_input(
            label="Input a cuisine. Example: 'Malaysian', 'Asian', 'Asian American Fusion'",
            max_chars=MAX_CUISINE_TOKENS,
        )
        
        st.subheader("Ingredients")
        ingredient_options = _ingredient_options()

        st.subheader("Dietary Restrictions")
        dieatry_options = _dietary_options()

        submitted = st.form_submit_button("Generate Recipe")


    if submitted:
        st.write(f"{str(ingredient_options)}\n{dieatry_options}")

def _dietary_options():
    options = {
        key: st.checkbox(key.value)
        for key in DietaryRestrictOpts
    }

    return options

def _ingredient_options(): 
    options = {
        key: st.checkbox(key.value)
        for key in IngredientOpts
    }

    return options
    