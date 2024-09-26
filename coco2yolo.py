import json
import os

import yaml

def convert_coco_to_yolo(json_path, output_path):
    with open(json_path) as f:
        data = json.load(f)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for image in data['images']:
        image_id = image['id']
        file_name = image['file_name']
        width = image['width']
        height = image['height']

        annotations = [ann for ann in data['annotations'] if ann['image_id'] == image_id]
        
        with open(os.path.join(output_path, f"{os.path.splitext(file_name)[0]}.txt"), 'w') as f:
            for ann in annotations:
                category_id = 0 #ann['category_id']
                bbox = ann['bbox']
                x_center = (bbox[0] + bbox[2] / 2) / width
                y_center = (bbox[1] + bbox[3] / 2) / height
                w = bbox[2] / width
                h = bbox[3] / height
                f.write(f"{category_id} {x_center} {y_center} {w} {h}\n")

def yolo_directory_stracture(out):
    
    #data.yaml
    pass


def create_yaml(path: str, train: str, val: str, file_name="data.yaml", name="shrimp"):
    # Data structure for the YAML file
    data = {
        "path": path,
        "train": train,
        "val": val,
        "names": {
            0: name
        }
    }
    # Write to the YAML file
    with open(os.path.join("output",path,file_name), 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

    print(f"YAML file '{file_name}' created successfully.")


# Example usage
create_yaml("datasets", "images/train", "images/val")

json_path = os.path.join("input","json","shrimp_231109.json") 
output_path = './output/datasets/labels/train'
convert_coco_to_yolo(json_path, output_path)