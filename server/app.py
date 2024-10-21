from flask import Flask

app = Flask(__name__)

# 1. Index Route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2. Print Route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Output to console
    return parameter  # Display in browser

# 3. Count Route
@app.route('/count/<int:parameter>')
def count(parameter):
    # Create a string of numbers from 0 to parameter-1, each on a new line
    return '\n'.join(str(i) for i in range(parameter))

# 4. Math Route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2  # Division, result will be float
    elif operation == '%':
        result = num1 % num2  # Modulo
    else:
        return "Invalid operation", 400  # Handle invalid operation with 400 status code

    return str(result)  # Return the result as a string

# Run the application if this file is executed directly
if __name__ == '__main__':
    app.run(port=5555, debug=True)
