
import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
from matplotlib.pyplot import imread





labels = pd.read_csv('/Users/chrimar3/projects/html/djsite/lab/labels.csv')
valuecount = labels["breed"].value_counts()


filenames=["/Users/chrimar3/projects/dogbreeds/data/train/" + fname + ".jpg" for fname in labels["id"]]
filenames20=filenames[:20]
labels=labels["breed"].to_numpy()
labeldata20=labels[:20]
uniquebreeds = (np.unique(labels))
qtybreeds= len(uniquebreeds)
booleanlabels = [label == uniquebreeds[0] for label in labels]
X = filenames
y = booleanlabels


#loadmodel = load_model('/Users/chrimar3/projects/html/djsite/lab/dogmodel.h5')



