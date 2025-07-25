import cv2
import numpy as np
import os

# ✅ Load Haar cascade
face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default (1) copy.xml')

# ✅ Face extractor function
def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is None or len(faces) == 0:
        return None

    # Only return the first face
    for (x, y, w, h) in faces:
        return img[y:y+h, x:x+w]

# ✅ Create a folder to save face images
save_path = './Image'
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    face = face_extractor(frame)

    if face is not None:
        count += 1

        face = cv2.resize(face, (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        name = "Sonu"
        file_name_path = os.path.join(save_path, f'{name}_{count}.jpg')

        cv2.imwrite(file_name_path, face)

        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Cropper', face)
    else:
        print("Face not found")
        pass

    if cv2.waitKey(1) == 13 or count == 50:  # Press Enter or stop at 50 images
        break

cap.release()
cv2.destroyAllWindows()
print('✅ Data Set Collection Completed')
