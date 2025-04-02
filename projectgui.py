import tkinter as tk
import subprocess
from PIL import Image, ImageTk
import webbrowser
from datetime import datetime

class FaceAttendanceSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Attendance System")
        self.master.configure(bg="white")  # Set background color to white

        # Load and resize logo
        self.logo = Image.open("logo.jpeg").resize((150, 150))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(master, image=self.logo, bg="white")
        self.logo_label.pack()

        # Title label
        self.label = tk.Label(master, text="Face Attendance System", font=("Times New Roman", 16, "bold"), fg="blue", bg="white")
        self.label.pack(pady=(10, 20))

        # Capture Faces button with hover effect
        self.capture_button = tk.Button(master, text="Capture Faces", command=self.capture_faces, width=20,
                                        font=("Times New roman ", 12))
        self.capture_button.pack(pady=5)
        self.add_hover_effect(self.capture_button)

        # Train Model button with hover effect
        self.train_button = tk.Button(master, text="Train Model", command=self.train_model, width=20,
                                      font=("Times New Roman", 12))
        self.train_button.pack(pady=5)
        self.add_hover_effect(self.train_button)

        # Take Attendance button
        self.take_attendance_button = tk.Button(master, text="Take Attendance", command=self.take_attendance, width=20,
                                                 font=("Times New Roman ", 12))
        self.take_attendance_button.pack(pady=5)
        self.add_hover_effect(self.take_attendance_button)

        # Quit button with hover effect
        self.quit_button = tk.Button(master, text="Quit", command=master.quit, width=20, font=("TImes new roman", 12))
        self.quit_button.pack(pady=5)
        self.add_hover_effect(self.quit_button)

       
        self.open_app_button = tk.Button(master, text="Show Attendance ", command=self.open_web_app, width=30,
                                         font=("Times new roman", 12))
        self.open_app_button.pack(pady=5)

      
        self.time_label = tk.Label(master, text="", font=("Times new roman", 14), bg="white")
        self.time_label.pack()

       
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=current_time)
        self.master.after(1000, self.update_time)  # Update every second

    def capture_faces(self):
        try:
           
            subprocess.Popen(["python", "get_faces_from_camera_tkinter.py"])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def train_model(self):
        try:
         
            subprocess.Popen(["python", "features_extraction_to_csv.py"])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def take_attendance(self):
        try:
          
            subprocess.Popen(["python", "attendance_taker.py"])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def add_hover_effect(self, widget):
        widget.bind("<Enter>", lambda event: widget.config(bg="#add8e6")) 
        widget.bind("<Leave>", lambda event: widget.config(bg="lightgray"))  

    def open_web_app(self):
        webbrowser.open("http://127.0.0.1:5000")

def main():
    root = tk.Tk()
    root.geometry("400x600")  
    app = FaceAttendanceSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
