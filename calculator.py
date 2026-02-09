class Calculator:
    def add(self, var_satu, var_dua):
        return var_satu + var_dua
    def subtract(self, var_satu, var_dua):
        return var_satu - var_dua
    def multiply(self, var_satu, var_dua):
        return var_satu * var_dua
    def divide(self, var_satu, var_dua):
        return var_satu / var_dua
    def modulo(self, var_satu, var_dua):
        return var_satu % var_dua
    def power(self, var_satu, var_dua):
        return var_satu ** var_dua

if __name__ == "__main__":
    calc = Calculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    print("Modulo: ", calc.modulo(10, 5))
    print("Power: ", calc.power(10, 5))
