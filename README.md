# simple-calculator
This document provides an overview and usage instructions for the Calculator Application, a simple yet functional GUI-based calculator program implemented using Python's 'tkinter' library. The application supports basic arithmetic operations, percentages, parentheses for order of operations, and a clear function. It also features keyboard input integration for enhanced usability.
1. Features
Arithmetic Operations: Supports addition, subtraction, multiplication, and division.
Percentages: Calculates the percentage of a value.
Decimal Support: Allows for decimal numbers in calculations.
Parentheses: Facilitates complex expressions by supporting parentheses for grouping operations.
clear Function: Resets the calculator display with the "AC" button or by pressing "C".
Backspace: Removes the last entered digit with the "←" button or by pressing backspace on the keyboard.
Keyboard Input: Users can input numbers and perform calculations using the keyboard.
Error Handling: Displays "Error" when an invalid operation is attempted.
2.Starting the Application
（1） Ensure you have Python installed on your system.
（2） Download or clone this repository to your local machine.
（3） Navigate to the directory containing the calculator script.
（4） Run the `calculator.py` script using the command: `python calculator.py`.
3. Operating the Calculator
Basic Calculation: Click on the number buttons to enter digits, then use the operator buttons (`+`, `-`, `x`, `÷`) to specify the operation. Press "=" to see the result.
Clear Display: Press "AC" or "C" on your keyboard to clear the current expression.
Delete Last Digit: Use the "←" button or press backspace to remove the last entered digit.
Percentage Calculation: Enter a number and press "%" to find its percentage value.
Brackets: For complex expressions, use "(" and ")" to group operations.
Keyboard Inputs: Directly type numbers and operators on your keyboard. Press "Enter" to execute the calculation.
4.Technical Details
Programming Language: Python
GUI Library: Tkinter
Design Pattern: Model-View-Controller (MVC)
      Model: `CalculatorModel` handles data and logic.
      View: `CalculatorView` manages the visual aspects and user interaction.
      Controller: `CalculatorController` connects the model and view, processing user inputs.
5.Acknowledgments
Thank you for using this Calculator Application. Any feedback for improvements or issues encountered is greatly appreciated. Enjoy calculating!
