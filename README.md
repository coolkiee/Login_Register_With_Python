# 🐍 Flask User Registration & Login System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-green?style=flat&logo=flask)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=flat&logo=pandas)

This project is a lightweight, web-based user registration and authentication system built with the **Python Flask** framework. Instead of a traditional SQL database, it utilizes a **CSV file** for data persistence, leveraging the **Pandas** library for efficient data manipulation and management.

---

## 👥 Development Team

This project was developed by:

* 👤 **Alp Tuna Akif KOCAOĞLU** (~Coolkie)
* 👤 **Buğrahan Cerit** (~ziwethz)
* 👤 **Muzaffer Bener**

---

## 🚀 Key Features

* **📝 User Registration:** Allows users to sign up with their First Name, Last Name, Email, Password, and Age.
* **🔐 Secure Login:** Authentication system using email and password credentials.
* **💾 Data Persistence:** User data is structured and stored in a local `users.csv` file.
* **🛡️ Security:** User passwords are never stored in plain text; they are hashed using the **SHA-256** algorithm before storage.
* **📊 Data Management:** Utilizes Pandas for robust CSV reading and writing operations.

---

## 🛠️ Prerequisites

To run this project, you need **Python 3.x** installed on your system. The project relies on the following external libraries:

* `Flask` (Web Server & Routing)
* `Pandas` (Data Manipulation)

---

## 📥 Installation & Usage

Follow these steps to set up and run the project locally.

### 1. Clone the Repository
Download the project files from GitHub:

```bash
git clone https://github.com/coolkiee/Login_Register_With_Python.git
cd Login_Register_With_Python

2. Create a Virtual Environment (Recommended)
It is best practice to run Python projects in a virtual environment to avoid dependency conflicts.

# Create the virtual environment
python -m venv venv

Activate the virtual environment:
  *Windows:
    venv\Scripts\activate
  *linux/mac:
    source venv/bin/activate

3. Install Dependencies
  Once the virtual environment is active (you should see (venv) in your terminal), install the required packages:
  pip install flask pandas
4. Run the Application
  Start the Flask server:
    python app.py
  After running the command, you will see a message indicating the server is running. Open your browser and navigate     to:👉 http://127.0.0.1:5000
    
📂 Project Structure
Login_Register_With_Python/
├── app.py              # Main Flask application entry point
├── user_manager.py     # Handles user logic (Register, Login, CSV ops)
├── user.py             # User class definition
├── users.csv           # CSV database file
├── templates/          # HTML templates (Login, Register pages)
└── README.md           # Project documentation
