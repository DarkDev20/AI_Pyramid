from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def generate_triangle(n: int) -> str:
    """
    Generates a right-aligned triangle pattern of asterisks with n rows.
    
    :param n: The number of rows in the triangle.
    :return: A string representation of the triangle.
    """
    return _recursive_triangle(n, n)


def _recursive_triangle(x: int, n: int) -> str:
    """
    Recursively constructs the triangle pattern.

    :param x: The current row index.
    :param n: The total number of rows.
    :return: A string representation of the triangle from row x to 1.
    """
    if not isinstance(x, int) or not isinstance(n, int):
        raise ValueError("Both input values must be integers.")
    
    if x > n:
        x = n  # Ensure x does not exceed n
    
    if x == 0 or n == 0:
        return ""  # Return an empty string for zero rows
    
    # Construct the current row with leading spaces and asterisks
    leading_spaces = " " * (n - x)
    stars = "*" * x
    current_row = leading_spaces + stars

    # Recursively generate the remaining rows
    if x > 1:
        return current_row + "\n" + _recursive_triangle(x - 1, n)
    
    return current_row


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        n = int(data.get("numRows", 0))
        triangle_pattern = generate_triangle(n)
        return jsonify({"triangle": triangle_pattern})
    except ValueError:
        return jsonify({"error": "Invalid input. Please enter a valid integer."}), 400


if __name__ == "__main__":
    app.run(debug=True)
