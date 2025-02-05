from flask import Flask, request, jsonify
from flask_cors import CORS
import math
import requests

app = Flask(__name__)
CORS(app)

# ---- Number Property Checks ----
def is_prime(n):
    """Check if a number is prime."""
    if n < 2 or not n.is_integer():
        return False
    n = int(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number (sum of proper divisors equals the number)."""
    if not n.is_integer():
        return False
    n = int(n)
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    if not n.is_integer():
        return False
    digits = [int(d) for d in str(abs(int(n)))]
    return sum(d ** len(digits) for d in digits) == int(n)

# ---- API Routes ----
@app.route('/')
def home():
    return "Welcome to the Number Classification API! Use /api/classify-number?number=<your_number> to classify a number."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Ensure number is included in the error response
    try:
        number = float(number)  # Accept both integers and floats
    except (ValueError, TypeError):
        return jsonify({"number": number, "error": True, "message": "Invalid number format"}), 400 

    properties = []

    # Classify the number based on various properties
    classifications = {
        "prime": is_prime(number),
        "perfect": is_perfect(number),
        "armstrong": is_armstrong(number),
        "even": number % 2 == 0,
        "odd": number % 2 != 0
    }

    # Dynamically construct the properties list based on classifications
    for prop, is_valid in classifications.items():
        if is_valid:
            properties.append(prop)

    digit_sum = sum(int(digit) for digit in str(abs(int(number))))

    # Generate the fun fact dynamically for Armstrong numbers
    fun_fact = None
    if classifications["armstrong"]:
        fun_fact = f"{int(number)} is an Armstrong number because " + " + ".join(
            [f"{d}^{len(str(int(number)))}" for d in str(abs(int(number)))]) + f" = {int(number)}"
    
    # Fetch a fun fact from the Numbers API
    try:
        response = requests.get(f'http://numbersapi.com/{int(number)}/math?json=true', timeout=5)
        if response.status_code == 200:
            fun_fact = response.json().get('text', 'No fun fact found.')
    except requests.RequestException:
        fun_fact = "No fun fact found."

    # Build the response dynamically
    response_data = {
        "number": number,
        "is_prime": classifications["prime"],
        "is_perfect": classifications["perfect"],
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact if fun_fact else "No fact found."
    }

    return jsonify(response_data), 200

# ---- Run Flask App ----
if __name__ == '__main__':
    app.run(debug=True)
