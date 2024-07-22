import random

from sqlalchemy.orm import sessionmaker

from models import engine, Recipe, Chef

Session = sessionmaker(bind=engine)

with Session() as session:
    def create_recipe(name: str, ingredients: str, instructions: str):
        new_recipe = Recipe(
            name=name,
            ingredients=ingredients,
            instructions=instructions
        )
        session.add(new_recipe)
        session.commit()


    def update_recipe_by_name(name: str, new_name: str,  new_ingredients: str, new_instructions: str):
        recipe = session.query(Recipe).filter_by(name=name).first()

        recipe.name = new_name
        recipe.ingredients = new_ingredients
        recipe.instructions = new_instructions

        session.add(recipe)

        session.commit()

    def delete_recipe_by_name(name: str):
        some_recipe = session.query(Recipe).filter_by(name=name).first()

        session.delete(some_recipe)

        session.commit()


    def get_recipes_by_ingredient(ingredient_name: str):
        all_recipes = session.query(Recipe).filter(
            Recipe.ingredients.ilike(f"%{ingredient_name}%")
        )

        return all_recipes


    def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str):
        recipe = session.query(Recipe).filter_by(name=recipe_name).first()

        chef = session.query(Chef).filter_by(name=chef_name).first()

        if chef.id == recipe.chef_id:
            raise Exception(f"Recipe: {recipe.name} already has a related chef")

        else:
            recipe.chef_id = chef.id

            session.add(recipe)
            session.commit()
            return f"Related recipe {recipe.name} with chef {chef.name}"

    def get_recipes_with_chef():
        recipes = session.query(Recipe).all()
        result = []

        for recipe in recipes:
            result.append(f"Recipe: {recipe.name} made by chef: {recipe.chef.name}")

        return "\n".join(result)


print(get_recipes_with_chef())