import logging
from enum import Enum

# Define the arithmetic operations as an enumeration
class ArithmeticOperation(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

# Set up the logger
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)

def log_warning(message):
    logger.warning(message)

def log_debug(message):
    logger.debug(message)

def log_critical(message):
    logger.critical(message)

# Decorator for logging function execution
def log_function_execution(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        log_info(f"Function '{function_name}' started. Args: {args}, Kwargs: {kwargs}")

        try:
            result = func(*args, **kwargs)
            log_info(f"Function '{function_name}' completed successfully. Result: {result}")
            return result
        except Exception as e:
            log_critical(f"Function '{function_name}' failed with error: {e}")
            raise

    return wrapper

@log_function_execution
def add(x, y):
    return x + y

@log_function_execution
def subtract(x, y):
    return x - y

@log_function_execution
def multiply(x, y):
    return x * y

@log_function_execution
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")

        # Convert the input operator to the corresponding enumeration value
        if operator == "+":
            operation = ArithmeticOperation.ADD
        elif operator == "-":
            operation = ArithmeticOperation.SUBTRACT
        elif operator == "*":
            operation = ArithmeticOperation.MULTIPLY
        elif operator == "/":
            operation = ArithmeticOperation.DIVIDE
        else:
            raise ValueError("Invalid operator. Supported operators: +, -, *, /")

        # Perform the selected operation using the enumeration value
        if operation == ArithmeticOperation.ADD:
            result = add(num1, num2)
        elif operation == ArithmeticOperation.SUBTRACT:
            result = subtract(num1, num2)
        elif operation == ArithmeticOperation.MULTIPLY:
            result = multiply(num1, num2)
        elif operation == ArithmeticOperation.DIVIDE:
            result = divide(num1, num2)

        log_info(f"Result of {num1} {operator} {num2} is {result}")
    except Exception as e:
        log_critical(f"Unexpected error: {e}")
        raise
    finally:
        logging.shutdown()
