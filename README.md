# Project
#This is my Face Detection Attendance System project


👨‍🎓 Face Detection Attendance System using Python

A real-time Face Recognition-based Attendance System developed using Python, OpenCV, and face_recognition library.
It detects and recognizes faces through the webcam and automatically marks attendance with Name, Date, and Time in an Excel/CSV file.

🚀 Features

✔ Real-time Face Detection & Recognition
✔ Automatic Attendance Marking in CSV / Excel
✔ Records Name, Date, Time
✔ Stores Known Faces for Detection
✔ Uses OpenCV, face_recognition, and NumPy
✔ Simple and User-Friendly Interface
✔ Highly accurate using Deep Learning-based face encodings

🛠️ Technologies Used
Technology	Purpose
Python	Core Programming
OpenCV	Live camera and image processing
face_recognition (Dlib)	Face encoding and recognition
NumPy	Numerical operations
Pandas (optional)	CSV/Excel handling
Tkinter (optional)	GUI (if implemented)
📂 Project Structure
FaceDetectionAttendance/
│
├── Attendace.py          # Main system file (real-time recognition + attendance)
├── EncodeFaces.py        # Generates and stores face encodings
├── ImagesAttendance/     # Folder containing known person images
├── Attendance.csv        # Generated attendance log file
├── README.md             # Project documentation
└── requirements.txt      # Dependencies list

📥 Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/your-username/FaceDetectionAttendance.git
cd FaceDetectionAttendance

2️⃣ Install Required Libraries
pip install -r requirements.txt


Or manually:

pip install opencv-python face_recognition numpy pandas

▶️ How to Run the Project
Step 1: Add Known Faces

Place clear images of known people inside the ImagesAttendance folder.
Name the images as:

PersonName.jpg

Step 2: Encode Faces

Run:

python EncodeFaces.py

Step 3: Start Face Recognition Attendance System
python Attendace.py

🚨 How It Works (Workflow)

1️⃣ Load stored images from ImagesAttendance
2️⃣ Convert them to 128-dimensional Face Encodings
3️⃣ Start webcam using OpenCV
4️⃣ Detect and compare faces with the encoded dataset
5️⃣ If matched ➝ Mark attendance with Name, Date, Time in CSV
6️⃣ Prevents duplicate entries for the same session

📋 Attendance Output Example
Name	Date	Time
Sonu Kumar	2025-05-12	09:15:23
Rahul Sharma	2025-05-12	09:17:42
🧠 Concepts Used
Concept	Usage
Face Detection	Using Haar Cascades / HOG / CNN
Face Recognition	face_recognition library
OOP Principles	Class-based structure (optional)
File Handling	Writing to CSV / Excel
Image Processing	OpenCV functions
Machine Learning	Face encoding & comparison
🌟 Future Enhancements (Ideas)

🔐 Add GUI using Tkinter/PyQt
📧 Email alert when unknown face is detected
🗃 Store attendance directly in MySQL / Firebase database
📸 Capture image of each attendee
📱 Create Android/Desktop application

📝 License

This project is licensed under the MIT License.
Feel free to modify and improve!

🙏 Acknowledgements

Special thanks to:
🧠 Adam Geitgey – creator of face_recognition library
📸 OpenCV community
🎓 Python Open Source Contributors
