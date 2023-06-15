#1.**Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# Input                Output                      Process
# -Oral stories       -Traslated languages         -Create a classes called Story, Storyteller, Traslator. 
#                                                   -I am going to use inheritance to create different types of stories
#                                                   -I am going to use inheritance to create different types of storytellers
#                                                   -I am going to use inheritance to create different types of translators

class Story:
    def __init__(self, name, length, moral_lesson, age_group):
        self.name = name
        self.length = length
        self.moral_lesson = moral_lesson
        self.age_group = age_group
class Storyteller:
    def __init__(self, name, language):
        self.name = name
        self.language = language  
class Translator:
    def __init__(self, source_language, target_language):
        self.source_language = source_language
        self.target_language = target_language  

# Stories
class Folktale(Story):
    pass
class Myth(Story):
    pass
class Legend(Story):
    pass 

# Storyteller
class OralStoryteller(Storyteller):
    pass
class WrittenStoryteller(Storyteller):
    pass

# Traslators
class HumanTranslator(Translator):
    pass
class MachineTranslator(Translator):
    pass

                                                            
#2.**African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

# Input                Output                                              Process
# -African Cuisens    -Recipes of different African countries.            -Create a class called Recipe. 
#                     -Unique ingredients.                                -Create subclasses for different types of recipes.
#                     -Preparation time.                                  -Create different to function to perfom different tasks like get a recipe by name,
#                     -Cooking method.                                     add a new recipe and to to print all recipes
#                     -Nutritional information.                           -Add some recipe to the list

class Recipe:
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_information):
        self.name = name
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_information = nutritional_information

class MoroccanRecipe(Recipe):
    pass

class EthiopianRecipe(Recipe):
    pass

class NigerianRecipe(Recipe):
    pass 

def get_recipe(name):
    for recipe in recipes:
        if recipe.name == name:
            return recipe
def print_recipes():
    for recipe in recipes:
        print(recipe) 
def print_recipes():
    for recipe in recipes:
        print(recipe) 
        
recipes = []             
add_recipe(EthiopianRecipe("Injera", ["water", "teff flour"], 20, "baking", {"calories": 400, "fat": 30, "protein": 40}))
add_recipe(NigerianRecipe("Jollof Rice", ["rice", "tomatoes", "peppers", "onions"], 45, "simmering", {"calories": 600, "fat": 30, "protein": 40}))
add_recipe(MoroccanRecipe("Burger", ["scone", "chicken", "onions", "lentiles leaves"], 40, "braising", {"calories": 600, "fat": 30, "protein": 40}))

print_recipes()

#3.**Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to
# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.
    

#4.**African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.

# 5.Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

# 6.Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
    
# 7. Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.
    
# 8.Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.