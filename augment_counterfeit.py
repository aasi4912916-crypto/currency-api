import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from PIL import Image
import numpy as np

COUNTERFEIT_DIR = 'dataset\\train\\counterfeit'
OUTPUT_DIR = 'dataset\\train\\counterfeit'
TARGET_COUNT = 4000

datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    brightness_range=[0.7, 1.3],
    fill_mode='nearest'
)

current_images = [f for f in os.listdir(COUNTERFEIT_DIR)
                  if f.lower().endswith(('.jpg','.jpeg','.png'))]
current_count = len(current_images)
print(f"Current counterfeit images: {current_count}")
print(f"Target: {TARGET_COUNT}")
print(f"Need to generate: {TARGET_COUNT - current_count} more images")

generated = 0
i = 0

while current_count + generated < TARGET_COUNT:
    img_name = current_images[i % len(current_images)]
    img_path = os.path.join(COUNTERFEIT_DIR, img_name)

    try:
        img = load_img(img_path, target_size=(224, 224))
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        for batch in datagen.flow(
            x,
            batch_size=1,
            save_to_dir=OUTPUT_DIR,
            save_prefix='aug_fake',
            save_format='jpg'
        ):
            generated += 1
            if generated % 100 == 0:
                print(f"Generated {generated} images...")
            break
    except Exception as e:
        pass

    i += 1

print(f"\nAugmentation Complete!")
print(f"Total counterfeit images: {len(os.listdir(COUNTERFEIT_DIR))}")