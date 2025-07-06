# 🔐 Task 3 - Secure File Sharing System

This is **Task 3** of the **Future Interns Cyber Security Internship**. It demonstrates a secure file upload and download system using AES encryption built with Python Flask.

---

## ✅ Features

- Upload any file through a web interface
- AES-128 encryption (ECB mode) on upload
- Secure file download with real-time decryption
- Built with Flask, PyCryptodome, and HTML

---

## 🛠 Technologies Used

- Python 3
- Flask (Web Framework)
- PyCryptodome (AES Encryption)
- HTML, JavaScript

---

## 🚀 How to Run Locally

```bash
# Navigate to the folder
cd Task_3_Secure_File_Sharing_System

# Activate virtual environment
venv\Scripts\activate

# Install dependencies (if needed)
pip install -r requirements.txt

# Run the app
python app.py
```

Then open your browser and visit:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Folder Structure

```
Task_3_Secure_File_Sharing_System/
├── app.py
├── encryption.py
├── requirements.txt
├── README.md
├── SECURITY_OVERVIEW.md
├── templates/
│   └── index.html
├── static/
└── uploads/
```

---

## 🔒 Security Notes

- AES key is hardcoded for demo purposes (`encryption.py`)
- Mode used: ECB (for simplicity — not recommended in production)
- See `SECURITY_OVERVIEW.md` for more details

---

## 🎓 Internship Credit

This task is part of:  
**Future Interns – Cyber Security Internship 2025**
