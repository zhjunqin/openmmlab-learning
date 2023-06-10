
import os

fruit = os.listdir('fruit30_train')

for item in fruit:
    path = os.path.join('fruit30_train', item)
    pics = os.listdir(path)
    length = len(pics)
    train_len = int(length * 0.8)
    os.mkdir(os.path.join('val', item))
    for pic in pics[train_len:]:
       src = os.path.join('fruit30_train', item, pic)
       dst = os.path.join('val', item, pic)
       os.rename(src, dst)
