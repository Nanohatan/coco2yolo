import cv2
import os
import yaml
import matplotlib.pyplot as plt

# data.yamlのパス
data_yaml_path = 'output/datasets/data.yaml'

# data.yamlの読み込み
with open(data_yaml_path, 'r') as file:
    data = yaml.safe_load(file)

train_image_folder = os.path.join("output",data['path'],data['train'])
train_label_folder = os.path.join( 'output/datasets/labels/train')
class_names = data['names']

def draw_annotations(image_path, label_path):
    # 画像の読み込み
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 画像のサイズ取得
    h, w, _ = image.shape
    
    # アノテーションファイルの読み込み
    with open(label_path, 'r') as file:
        for line in file.readlines():
            class_id, x_center, y_center, width, height = map(float, line.strip().split())
            
            # バウンディングボックスの座標を計算
            x_center *= w
            y_center *= h
            width *= w
            height *= h
            
            x1 = int(x_center - width / 2)
            y1 = int(y_center - height / 2)
            x2 = int(x_center + width / 2)
            y2 = int(y_center + height / 2)
            
            # バウンディングボックスの描画
            color = (255, 0, 0)  # バウンディングボックスの色 (青)
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            
            # クラス名の表示
            # cv2.putText(image, class_names[int(class_id)], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    # 画像の表示
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

# データセット内の画像とラベルを可視化
for image_name in os.listdir(train_image_folder):
    image_path = os.path.join(train_image_folder, image_name)
    label_path = os.path.join(train_label_folder, os.path.splitext(image_name)[0] + '.txt')
    
    if os.path.exists(label_path):
        draw_annotations(image_path, label_path)
    else:
        print(label_path)
