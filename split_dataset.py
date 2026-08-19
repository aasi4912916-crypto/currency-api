import os, shutil, random

def split_folder(src, dst_train, dst_val, dst_test):
    images = [f for f in os.listdir(src)
              if f.lower().endswith(('.jpg','.jpeg','.png','.bmp'))]
    random.shuffle(images)
    n = len(images)
    train_end = int(n * 0.8)
    val_end = int(n * 0.9)
    splits = {
        dst_train: images[:train_end],
        dst_val:   images[train_end:val_end],
        dst_test:  images[val_end:]
    }
    for dst, files in splits.items():
        os.makedirs(dst, exist_ok=True)
        for f in files:
            shutil.copy(os.path.join(src, f), os.path.join(dst, f))
        print(f'{dst}: {len(files)} images')

print('Splitting Genuine...')
split_folder(
    'dataset\\train\\genuine',
    'dataset\\final\\train\\genuine',
    'dataset\\final\\validation\\genuine',
    'dataset\\final\\test\\genuine'
)

print('Splitting Counterfeit...')
split_folder(
    'dataset\\train\\counterfeit',
    'dataset\\final\\train\\counterfeit',
    'dataset\\final\\validation\\counterfeit',
    'dataset\\final\\test\\counterfeit'
)

print('\nSplit Complete!')
print('Train genuine:', len(os.listdir('dataset\\final\\train\\genuine')))
print('Train counterfeit:', len(os.listdir('dataset\\final\\train\\counterfeit')))
print('Val genuine:', len(os.listdir('dataset\\final\\validation\\genuine')))
print('Val counterfeit:', len(os.listdir('dataset\\final\\validation\\counterfeit')))
print('Test genuine:', len(os.listdir('dataset\\final\\test\\genuine')))
print('Test counterfeit:', len(os.listdir('dataset\\final\\test\\counterfeit')))