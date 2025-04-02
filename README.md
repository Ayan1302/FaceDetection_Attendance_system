# Face-Based Attendance System

## 📌 Project Overview
This project is a **Face-Based Attendance System** implemented using **Raspberry Pi 4B** and **facial recognition technology**. The system ensures students are present for the entire class duration by verifying attendance both **before the class starts** and **after the class ends**.

## 🎯 Features
- **Dual Verification**: Students must check in **before** and **after** class to be marked present.
- **Timer Lock**: Prevents multiple scans within a short period to avoid false attendance.
- **Facial Recognition**: Uses OpenCV and face recognition models to verify students.
- **Raspberry Pi Compatible**: Designed to work efficiently on Raspberry Pi 4B.

## 🛠️ Tech Stack
- **Programming Language**: Python
- **Libraries Used**:
  - `OpenCV` - for image processing
  - `face_recognition` - for facial detection & recognition
  - `NumPy` - for numerical operations
  - `Pandas` - for attendance data management

## 🚀 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Ayan1302/FaceDetection_Attendance_system.git
   cd face-attendance-system
   ```
2. Install dependencies:
   ```bash
   pip install opencv-python face-recognition numpy pandas
   ```
3. Run the attendance system:
   ```bash
   python attendance_system.py
   ```

## 📸 How It Works
1. The system captures images of students before and after class.
2. It compares detected faces with the registered database.
3. Attendance is marked only if both scans are successful.
4. A **timer lock** prevents resubmission attempts before class ends.
5. The final attendance report is generated in a CSV file.

## 📂 Project Structure
```
face-attendance-system/
│-- data/                # Folder to store student images
│-- models/              # Trained face recognition models
│-- attendance.csv       # Logs of attendance records
│-- attendance_system.py # Main script
│-- requirements.txt     # List of dependencies
│-- README.md            # Documentation
```

## 📝 Future Improvements
- Integrate with a **web dashboard** for real-time attendance tracking.
- Implement **RFID-based verification** for additional security.
- Optimize **face detection speed** for faster processing.

## 📜 License
This project is open-source under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! Feel free to suggest improvements or report issues.

## 📧 Contact
For any queries, reach out at **your-email@example.com**

---
🚀 Happy Coding!

