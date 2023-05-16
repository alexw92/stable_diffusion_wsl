import csv
import subprocess
from tqdm import tqdm
import os
import glob

# Path to the CSV file containing the prompts and the number of times to run the command for each prompt
PROMPT_FILE_DIR = "/mnt/c/Users/Fistus/Desktop/food_gen/prompts_sing"
ARGS_1 = " --ckpt /mnt/c/Users/Fistus/Downloads/v2-1_768-ema-pruned.ckpt --config configs/stable-diffusion/v2-inference-v.yaml --H 768 --W 768 --device cuda"
OUTDIR_ARG =  "--outdir /mnt/c/Users/Fistus/Desktop/generated_samples_15_05_23_2"
FROM_FILE_ARG = "--from-file"
# Path to the text2img.py script
TEXT2IMG_SCRIPT = "scripts/txt2img.py "

# Function to run the text2img.py command with a given prompt
def run_text2img(FROM_FILE):
    cmd = f"python {TEXT2IMG_SCRIPT} {ARGS_1} {OUTDIR_ARG} {FROM_FILE_ARG} {FROM_FILE}"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error running command for prompt_file '{FROM_FILE}': {error}")
    return output
	

def find_text_files(prompts_dir):
    """
    Returns a list of full paths for all the text files in the current directory
    and its subdirectories.
    """
    text_files = []
    for root, dirs, files in os.walk(prompts_dir):
        for file in files:
            if file.endswith(".txt"):
                text_files.append(os.path.join(root, file))
    return text_files
	

txt_files = find_text_files(PROMPT_FILE_DIR)
for file_path in tqdm(txt_files, desc='prompt_files'):
# Read the prompts to run from the CSV file
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        prompts = []
        for row in reader:
            prompts.append(row)

    run_text2img(file_path)
