import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import Xception
from tensorflow.keras.layers import GlobalAveragePooling2D, Dropout, Dense, Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers.legacy import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import load_model
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.python.ops.confusion_matrix import confusion_matrix

from dogtrain import RANDOM_STATE, input_tensor




labelsdf = pd.read_csv("/users/chris/projects/labels.csv")
labelsdf["id"] = labelsdf["id"].apply(lambda x: x + "jpg")
plt.figure(figsize=(20,5))
plt.xticks(rotation=90)
sns.countplot(data=labelsdf, x="breed")
plt.title("Distribution of Breeds")

RANDOM_STATE= 42
train_df, test_df = train_test_split(labelsdf, test_size=0.2, random_state=RANDOM_STATE)
train_df, val_df = train_test_split(train_df, test_size=0.2, random_state=RANDOM_STATE)

sample_images = train_df.sample(n=9)
plt.figure(figsize=(10,10)

image_sizes = [image.open(f"/users/chris/projects/data/train/{img_id}").size for img_id in train_df["id"]]

#setup model congraints

SIZE = (350,350)
BATCH_SIZE = 32
NUM_CLASSES = len(labelsdf["breed"].unique())
LEARNING_RATE = 0.001
DROPOUT_RATE = 0.7
EPOCHS = 5

train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

# data generators
train_generator = train_datagen.flow_from_dataframe(train_df, "users/chris/projects/data", "id", "breed", target_size = SIZE, batch_size = BATCH_SIZE, class_mode="categorical")
test_generator = test_datagen.flow_from_dataframe(test_df, "users/chris/projects/data", "id", "breed", target_size=SIZE, batch_size = BATCH_SIZE, class_mode="categorical")
val_generator = val_datagen.flow_from_dataframe(val_df, "users/chris/projects/data", "id", "breed", target_size=SIZE, batch_size = BATCH_SIZE, class_mode="categorical")


#base model
input_tensor = input(shape=(SIZE[0], SIZE[1]. 3))
base_model = Xception(weights="imagenet", include_top=False, input_tensor=input_tensor)
base_model.trainable = False

#output Layer
x = base_model.output
x = GlobalAveragePooling2d(),(x)
x = Dropout(DROPOUT_RATE)(x)
output = Dense(NUM_CLASSES, activation="softmax")(x)

#compile model
model = Model(inputs=input_tensor, outputs=output)
model.compile(optimizer=Adam(learning_rate=LEARNING_RATE), loss = "categorical_crossentropy", metrics=["accuracy"])

#train model

history = model.fit(train_generator,
                    validation_data=val_generator,
                    steps_per_epoch=train_generator.samples//BATCH_SIZE,
                    epochs=EPOCHS,
                    callbacks=[early_stopping, model_checkpoint])

#evaluate model on test data

score = model.evaluate(test_genretstor)
print("test loss:", score[0])
print("test accuracy:", score[1])








