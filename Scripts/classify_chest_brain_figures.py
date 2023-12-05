import os
import json
from PIL import Image
import csv

def read_json_and_classify_image(json_path, image_folder):
    
    i = 0

    # Read JSON file
    with open(json_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            image_name = data.get('pdf_hash') + "_" + data.get('fig_uri')

            if image_name:
                image_path = os.path.join(image_folder, image_name)
                if os.path.exists(image_path):
                    # img = Image.open(image_path)
                    # img.show()
                    # print(data.get('text'))
                    # print(data.get('pdf_hash') + "_" + data.get('fig_uri'))
                    if "Brain" in data.get('s2_caption'):

                        img = Image.open(image_path)
                        # folder path to save brain photos
                        img.save("/Users/vokhanh/Downloads/UTM/CSC490/release/brain_figures/brain_figures2/" + image_name, "png")
                    
                    elif "Chest" in data.get('s2_caption'):
                        
                        img = Image.open(image_path)
                        # folder path to save chest photos
                        img.save("/Users/vokhanh/Downloads/UTM/CSC490/release/chest_figures/chest_figures2/" + image_name, "png")
                else:
                    print(f"Image '{image_name}' not found in '{image_folder}'")
            else:
                print("No 'image_name' found in JSON object")

# JSONL file source and medical dataset folder
json_path = '/Users/vokhanh/Downloads/UTM/CSC490/release/s2_full_figures_oa_nonroco_combined_medical_top4_public.jsonl'
image_folder = '/Users/vokhanh/Downloads/UTM/CSC490/release/figures'

read_json_and_classify_image(json_path, image_folder)