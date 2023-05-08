import csv
import subprocess
import time
from tqdm import tqdm

# Path to the CSV file containing the prompts and the number of times to run the command for each prompt
PROMPTS_FILE = "prompts.csv"

# Path to the text2img.py script
TEXT2IMG_SCRIPT = "scripts/text2img.py"

# Number of images generated per prompt
IMAGES_PER_PROMPT = 9

# Function to run the text2img.py command with a given prompt
def run_text2img(prompt):
    cmd = f"python {TEXT2IMG_SCRIPT} --prompt {prompt}  --ckpt /mnt/c/Users/Fistus/Downloads/v2-1_768-ema-pruned.ckpt --config configs/stable-diffusion/v2-inference-v.yaml --H 768 --W 768 --device cuda"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error running command for prompt '{prompt}': {error}")
    return output

# Read the prompts and number of times to run from the CSV file
with open(PROMPTS_FILE, "r") as f:
    reader = csv.DictReader(f)
    prompts = []
    for row in reader:
        prompt = row["prompt"]
        count = int(row["count"])
        prompts.extend([prompt] * count)

# Iterate over the prompts and run the text2img command for each one
start_time = time.time()
generated_images = 0
for prompt in tqdm(prompts):
    run_text2img(prompt)
    generated_images += IMAGES_PER_PROMPT

# Print the number of generated images and the time taken
end_time = time.time()
time_taken = end_time - start_time
print(f"Generated {generated_images} images in {time_taken:.2f} seconds")
