# ⚙️ HNG DevOps Internship Tasks

This repository contains tasks completed during my **HNG DevOps Internship**, showcasing my hands-on learning and practical implementation of DevOps tools and principles.

### 🧪 Task 2: Flask-Based Numbers API Project

In this task, I built a **simple Flask API** that:

- Accepts a number as input via a GET request  
- Returns interesting **mathematical properties** of the number  
- Fetches a **fun fact** from the [Numbers API](http://numbersapi.com)

This task strengthened my skills in:
- Building and testing REST APIs with Flask
- Consuming external APIs
- Working with JSON and HTTP responses

---

## Features
- Determines if a number is **Armstrong, Prime, or Perfect**.
- Identifies whether the number is **Odd or Even**.
- Calculates the **sum of its digits**.
- Fetches a **fun fact** about the number from the Numbers API.
- Handles **CORS (Cross-Origin Resource Sharing)**.
- Includes **error handling** for invalid inputs and API failures.

---

## API Endpoints

### **GET /math/&lt;number&gt;**
#### **Request Example:**
```bash
GET http://127.0.0.1:5000/math/371
```

#### **Response Example:**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **Error Handling (Invalid Input)**
If the input is **not a valid number**, the API returns a `400 Bad Request`.
#### **Example:**
```bash
GET https://b35e-102-89-23-14.ngrok-free.app/api/classify-number
```
#### **Response:**
```json
{
    "number": "abc",
    "error": true
}
```

---

## Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/BorgOwen/HNG-DevOps.git
cd math.py
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
```bash
python math.py
```
The API will be available at:
```bash
http://localhost:5000/api/classify-number?number=000
```

---

## Requirements
Ensure you have the following installed:
- Python 3.7+
- Flask
- Flask-CORS
- Requests
- Ngrok for public access endpoints

Install required dependencies using:
```bash
pip install flask flask-cors requests
```

---

Install ngrok using:
```bash
choco install ngrok
```

## Project Structure
```
math-facts-api/
│── math_api.py          # Main API logic
│── requirements.txt     # Dependencies list
│── README.md            # Project documentation
```

---

## Contributing
Feel free to contribute! Fork the repository, make changes, and submit a pull request.

---


