class Calculator:
    def add(self, c, d):
        return c + d
    def subtract(self, c, d):
        return c - d
    def multiply(self, c, d):
        return c * d
    def divide(self, c, d):
        return c / d
    def modulo(self, c, d):
        return c % d
    def power(self, c, d):
        return c ** d

if __name__ == "__main__":
    calc = Calculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    print("Modulo: ", calc.modulo(10, 5))
    print("Power: ", calc.power(10, 5))
