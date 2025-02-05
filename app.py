from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


# ---- Number Property Checks ----
def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number (sum of proper divisors equals the number)."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n // 2 + 1) if n % i == 0]
    return sum(divisors) == n


# ---- Helper Functions ----
def digit_sum(n):
    """Calculate the sum of digits of a number."""
    return sum(int(d) for d in str(n))

def fetch_fun_fact(number):
    """Fetch a fun fact from the Numbers API."""
    url = f"http://numbersapi.com/{number}/math"
    try:
        response = requests.get(url, timeout=5)  # Avoid infinite waiting
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.text
    except requests.RequestException:
        return "No fun fact found."


# ---- Main Processing Function ----
def get_math_facts(number):
    """Generate number properties and fetch a fun fact."""
    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")

    properties.append("even" if number % 2 == 0 else "odd")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fetch_fun_fact(number)
    }


# ---- API Route ----
@app.route('/math/<number>', methods=['GET'])
def math_info(number):
    """Handle requests and return number properties."""
    if not number.isdigit():
        return jsonify({"number": number, "error": True}), 400  # 400 Bad Request

    number = int(number)
    return jsonify(get_math_facts(number))


# ---- Run Flask App ----
if __name__ == '__main__':
    app.run(debug=True)
