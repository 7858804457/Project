import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

# ✅ Path to folder containing face images
data_path = '/Users/sonu/PycharmProjects/face_detection/Image/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

Training_Data, Labels = [], []
            
# ✅ Load and resize training images
for i, file_name in enumerate(onlyfiles):
    image_path = join(data_path, file_name)
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if images is None:
        print(f"Warning: Could not read {image_path}")
        continue

    images = cv2.resize(images, (200, 200))  # Resize to fixed size
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)

# ✅ Train LBPH face recognizer
model = cv2.face.LBPHFaceRecognizer_create()
model.train(Training_Data, Labels)
print("✅ Dataset Model Training Complete!")

# ✅ Load Haar cascade for face detection
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# ✅ Face detector function
def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is None or len(faces) == 0:
        return img, None

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi = img[y:y+h, x:x+w] # roi=region of interest
        roi = cv2.resize(roi, (200, 200))
        return img, roi  # Only return first detected face

    return img, None

# ✅ Live video capture and recognition
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    image, face = face_detector(frame)

    try:
        face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face_gray)



        confidence = int(100 * (1 - result[1] / 300))  # Lower result[1] means better match

        if confidence > 82:
            display_text = f"Sonu - {confidence}%"
            color = (255, 255, 255)
        else:
            display_text = "Unknown"
            color = (0, 0, 255)

        cv2.putText(image, display_text, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
        cv2.imshow('Face Cropper', image)

    except:
        cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('Face Cropper', image)
        pass

    # Press Enter (key 13) to exit
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
