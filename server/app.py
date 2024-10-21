from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Display a heading on the homepage."""
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_text(parameter):
    """Display the parameter in the browser and print it to the console."""
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    """Display numbers from 0 to the given parameter - 1, each on a new line."""
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    """Perform a math operation based on the provided operator."""
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400  # Return a 400 error for invalid operations

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
