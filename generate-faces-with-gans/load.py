import numpy as np 
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt 

datasets = tfds.list_builders()
ds = tfds.load('cifar10', split='train', download=True)
ds = tfds.as_numpy(ds)
print(ds)
_, axes = plt.subplots(3, 3, figsize=(20, 20))
axes = axes.flatten()

i = 0
for example in ds:
    axes[i].imshow(example['image'], cmap='gray_r')
    axes[i].set_title(example['label'])
    axes[i].axis('off')
    i+=1

    if i == 9:
        break

plt.savefig('sample.png')

