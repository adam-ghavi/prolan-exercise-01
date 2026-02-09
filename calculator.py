class Calculator:
    def add(self, t, h):
        return t + h
    def subtract(self, t, h):
        return t - h
    def multiply(self, t, h):
        return t * h
    def divide(self, t, h):
        return t / h
    def modulo(self, t, h):
        return t % h
    def power(self, t, h):
        return t ** h

if __name__ == "__main__":
    calc = Calculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    print("Modulo: ", calc.modulo(10, 5))
    print("Power: ", calc.power(10, 5))
