import cv2
import os
import numpy as np

IMG_SIZE = 128



def load_signature_data():
    path = "../dataset/signature"  
    images = []
    labels = []

    classes = ["genuine", "forged"]

    for label, class_name in enumerate(classes):
        class_path = os.path.join(path, class_name)

        for file in os.listdir(class_path):
            img_path = os.path.join(class_path, file)

            img = cv2.imread(img_path, 0)  # grayscale
            if img is None:
                continue

            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img / 255.0

            images.append(img)
            labels.append(label)

    return np.array(images), np.array(labels)



def load_image_data():
    path = "../dataset/image"   
    images = []
    labels = []

    classes = ["authentic", "tampered"]

    for label, class_name in enumerate(classes):
        class_path = os.path.join(path, class_name)

        for file in os.listdir(class_path):
            img_path = os.path.join(class_path, file)

            img = cv2.imread(img_path)  # color
            if img is None:
                continue

            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            img = img / 255.0

            images.append(img)
            labels.append(label)

    return np.array(images), np.array(labels)