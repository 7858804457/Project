import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

# ✅ Set correct path to your face image dataset
data_path = '/Users/sonu/PycharmProjects/face_detection/Image/'

# ✅ Get all image file names in the folder
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

Training_Data, Labels = [], []

IMG_SIZE = (200, 200)  # ✅ Fixed image size (required for model)

# ✅ Loop through each file and prepare training data
for i, file_name in enumerate(onlyfiles):
    image_path = join(data_path, file_name)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"Warning: Could not read image: {image_path}")
        continue

    image = cv2.resize(image, IMG_SIZE)  # ✅ Resize to fixed size
    Training_Data.append(np.asarray(image, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)

# ✅ Create and train LBPH recognizer
model = cv2.face.LBPHFaceRecognizer_create()
model.train(Training_Data, Labels)

print("✅ Dataset Model Training Completed")

# Optional: Save model to disk
# model.save('/Users/sonu/PycharmProjects/face_detection/trained_model.yml')
