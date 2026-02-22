def scale_recipe(recipe, target_servings):
    """
    Scale a recipe from its original number of servings to a new target.
    
    Parameters
    ----------
    recipe : dict
        A dictionary containing:
            - 'servings' (int): the number of servings the ingredient list is for.
            - 'ingredients' (list[dict]): each element must contain:
                * 'ingredient' (str)
                * 'grammage'   (float or int) – weight in grams for the recipe's original servings.

        Example::
            {
                "servings": 2,
                "ingredients": [
                    {"ingredient": "Flour",  "grammage": 100},
                    {"ingredient": "Sugar",  "grammage": 200},
                    {"ingredient": "Butter", "grammage": 50}
                ]
            }

    target_servings : int
        The desired number of servings for the scaled recipe.

    Returns
    -------
    dict
        A new dictionary with:
            * 'servings' set to `target_servings`
            * 'ingredients' – each ingredient’s grammage multiplied by the scaling factor

    Raises
    ------
    ValueError
        If either the original or target servings are <= 0.
    """
    
    if recipe.get("servings", 0) <= 0:
        raise ValueError("Original servings must be a positive integer.")
    if target_servings <= 0:
        raise ValueError("Target servings must be a positive integer.")

    factor = target_servings / recipe["servings"]
    
    scaled_ingredients = [
        {
            "ingredient": ing["ingredient"],
            "grammage": ing["grammage"] * factor
        }
        for ing in recipe.get("ingredients", [])
    ]

    return {"servings": target_servings, "ingredients": scaled_ingredients}


# ------------------------------------------------------------------
# Example usage – the exact scenario you described
# ------------------------------------------------------------------

original_recipe = {
    "servings": 2,
    "ingredients": [
        {"ingredient": "Flour",  "grammage": 100},
        {"ingredient": "Sugar",  "grammage": 200},
        {"ingredient": "Butter", "grammage": 50}
    ]
}

scaled = scale_recipe(original_recipe, target_servings=100)

print(scaled)
