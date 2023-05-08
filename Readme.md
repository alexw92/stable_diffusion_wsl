# Done so far

+ Download weights from (https://huggingface.co/stabilityai/stable-diffusion-2-1/blob/main/v2-1_768-ema-pruned.ckpt)[here (5.2GB)]
clone repo
```
git clone https://github.com/Stability-AI/stablediffusion.git
cd stablediffusion
```

Change python from 3.8.5 to 3.9
```
nano environment.yml
```
#Create the conda env and install requirements
```
conda env create -f environment.yaml
conda activate ldm
pip install -r requirements.txt
```

Install xformers
```
conda install xformers -c xformers/label/dev
```

Run script with ref to weights and given prompt
```
python scripts/txt2img.py --prompt "tomato onion and garlic on a wooden surface" --ckpt /path_to_checkpoint/v2-1_768-ema-pruned.ckpt --config configs/stable-diffusion/v2-inference-v.yaml --H 768 --W 768 --device cuda
```

Dont forget ```--device cuda``` flag otherwise you will get ```RuntimeError: expected scalar type BFloat16 but found Float```
