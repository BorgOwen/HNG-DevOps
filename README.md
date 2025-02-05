# HNG-DevOps
This is a repository for the tasks done during my HNG DevOps Internship. 

Task 2 was about creating a simple Flask-based API that takes a number as input and returns interesting mathematical properties along with a fun fact from the Numbers API.

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


