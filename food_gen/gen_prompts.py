import os

# Specify the input file containing the list of ingredients
input_file = "ingredients.txt"

# Specify the directory where the output prompts will be saved
output_dir = "prompts_sing/"

# Create the output directory if it doesn't already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the input file and read the list of ingredients
with open(input_file, "r") as f:
    ingredients = f.read().splitlines()

# Define the list of text prompts to use
prompts = ["one single {} on a clean kitchen table",
           "two {} viewed from middle distance with glasses or cups in the background",
           "one {} viewed from short distance furniture or decor visible in the background",
           "one {} in a shopping cart",
           "one {} on a cutting board with natural light present",
           "three {} in a bowl",
           "some {} on a normal kitchen table",
           "one fresh {} on a kitchen counter with furniture in the background",
           "two {} in a pantry next to a kitchen item",
           "three of {} in a grocery store",
           "one {} at a farmer's market",
           "three {} on a metal table", 
           "{} centered with cooking equipment in the background", 
           "one {} centered on a wooden table",
           "two {} centered with furniture or decor visible in the background",
           "two {} in the center of the frame with low light conditions",
           "three {} centered with cooking equipment in the background",
           "one {} in the center of the frame",
           "one of {} with serving dishes or trays visible in the background"
   ]

# Generate text prompts for each ingredient and save them to separate files
for ingredient in ingredients:
    output_file = os.path.join(output_dir, "{}.txt".format(ingredient.replace(" ", "_")))
    with open(output_file, "a") as f:
        for i in range(len(prompts)):
            prompt = prompts[i].format(ingredient)
            if i == len(prompts) - 1:
                f.write(prompt)
            else:
                f.write(prompt + "\n")
