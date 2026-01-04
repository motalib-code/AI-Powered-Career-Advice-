import math
from typing import Union, List

class Calculator:
    """
    Advanced Calculator with support for basic and scientific operations.
    """
    
    def __init__(self):
        self.history = []
        self.memory = 0
    
    # Basic Operations
    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide two numbers with error handling"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def modulus(self, a: float, b: float) -> float:
        """Get remainder of division"""
        result = a % b
        self.history.append(f"{a} % {b} = {result}")
        return result
    
    def power(self, base: float, exponent: float) -> float:
        """Raise base to the power of exponent"""
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    # Scientific Operations
    def square_root(self, n: float) -> float:
        """Calculate square root"""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(n)
        self.history.append(f"√{n} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate factorial"""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers!")
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result
    
    def sin(self, angle_deg: float) -> float:
        """Calculate sine (angle in degrees)"""
        angle_rad = math.radians(angle_deg)
        result = math.sin(angle_rad)
        self.history.append(f"sin({angle_deg}°) = {result}")
        return result
    
    def cos(self, angle_deg: float) -> float:
        """Calculate cosine (angle in degrees)"""
        angle_rad = math.radians(angle_deg)
        result = math.cos(angle_rad)
        self.history.append(f"cos({angle_deg}°) = {result}")
        return result
    
    def tan(self, angle_deg: float) -> float:
        """Calculate tangent (angle in degrees)"""
        angle_rad = math.radians(angle_deg)
        result = math.tan(angle_rad)
        self.history.append(f"tan({angle_deg}°) = {result}")
        return result
    
    def log(self, n: float, base: float = 10) -> float:
        """Calculate logarithm"""
        if n <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers!")
        result = math.log(n, base)
        self.history.append(f"log{base}({n}) = {result}")
        return result
    
    # Memory Operations
    def memory_add(self, value: float) -> float:
        """Add value to memory"""
        self.memory += value
        return self.memory
    
    def memory_subtract(self, value: float) -> float:
        """Subtract value from memory"""
        self.memory -= value
        return self.memory
    
    def memory_recall(self) -> float:
        """Recall memory value"""
        return self.memory
    
    def memory_clear(self) -> None:
        """Clear memory"""
        self.memory = 0
    
    # History Operations
    def get_history(self) -> List[str]:
        """Get all calculations history"""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history"""
        self.history = []
    
    def print_history(self) -> None:
        """Print formatted history"""
        if not self.history:
            print("No calculation history available.")
            return
        
        print("\n" + "="*50)
        print("CALCULATION HISTORY")
        print("="*50)
        for i, calc in enumerate(self.history, 1):
            print(f"{i:2d}. {calc}")
        print("="*50 + "\n")


def interactive_calculator():
    """Interactive calculator with menu-driven interface"""
    calc = Calculator()
    
    print("\n" + "#"*50)
    print("#" + " "*48 + "#")
    print("#" + "  ADVANCED CALCULATOR".center(48) + "#")
    print("#" + " "*48 + "#")
    print("#"*50)
    
    menu = """
    \nOperations:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Modulus (%)
    6. Power (^)
    7. Square Root (√)
    8. Factorial (!)
    9. Sine (sin)
    10. Cosine (cos)
    11. Tangent (tan)
    12. Logarithm (log)
    13. Memory Add (M+)
    14. Memory Recall (MR)
    15. Clear Memory (MC)
    16. Show History
    17. Exit
    """
    
    while True:
        print(menu)
        choice = input("Enter your choice (1-17): ").strip()
        
        try:
            if choice == '1':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.add(a, b)}")
            
            elif choice == '2':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.subtract(a, b)}")
            
            elif choice == '3':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.multiply(a, b)}")
            
            elif choice == '4':
                a = float(input("Enter dividend: "))
                b = float(input("Enter divisor: "))
                print(f"Result: {calc.divide(a, b)}")
            
            elif choice == '5':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.modulus(a, b)}")
            
            elif choice == '6':
                base = float(input("Enter base: "))
                exp = float(input("Enter exponent: "))
                print(f"Result: {calc.power(base, exp)}")
            
            elif choice == '7':
                n = float(input("Enter number: "))
                print(f"Result: {calc.square_root(n)}")
            
            elif choice == '8':
                n = int(input("Enter number: "))
                print(f"Result: {calc.factorial(n)}")
            
            elif choice == '9':
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {calc.sin(angle):.6f}")
            
            elif choice == '10':
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {calc.cos(angle):.6f}")
            
            elif choice == '11':
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {calc.tan(angle):.6f}")
            
            elif choice == '12':
                n = float(input("Enter number: "))
                base = input("Enter base (default 10): ").strip() or "10"
                print(f"Result: {calc.log(n, float(base)):.6f}")
            
            elif choice == '13':
                value = float(input("Enter value to add to memory: "))
                print(f"Memory: {calc.memory_add(value)}")
            
            elif choice == '14':
                print(f"Memory Value: {calc.memory_recall()}")
            
            elif choice == '15':
                calc.memory_clear()
                print("Memory cleared!")
            
            elif choice == '16':
                calc.print_history()
            
            elif choice == '17':
                print("\nThank you for using the calculator!")
                calc.print_history()
                break
            
            else:
                print("Invalid choice! Please enter a number between 1 and 17.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        interactive_calculator()
    except KeyboardInterrupt:
        print("\n\nCalculator interrupted. Goodbye!")
    except Exception as e:
        print(f"Fatal error: {e}")
