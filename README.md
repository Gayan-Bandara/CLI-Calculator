# Calculator Program

This is a simple command-line calculator program written in Python. It supports basic arithmetic operations and maintains a history of calculations.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Additional operations: power, remainder
- Calculation history
- Input validation
- Termination and reset options

## Usage

Run the program and follow the on-screen prompts. You'll be presented with a menu of operations to choose from:

1. Add      : +
2. Subtract : -
3. Multiply : *
4. Divide   : /
5. Power    : ^
6. Remainder: %
7. Terminate: #
8. Reset    : $
9. History  : ?

Enter the symbol corresponding to the operation you want to perform.

### Input

- For arithmetic operations, you'll be prompted to enter two numbers.
- Enter '#' at any time to terminate the program.
- Enter '$' at any time to reset the current operation.
- Enter '?' to view the calculation history.

### Output

The program will display the result of your calculation and add it to the history.

## Error Handling

- The program validates numeric inputs and prompts for re-entry if invalid.
- Division by zero is handled gracefully.

## History

The program maintains a history of all calculations performed in the current session. You can view this history by entering '?' when prompted for an operation.

## Termination

To exit the program, enter '#' when prompted for an operation or at any number input prompt.

## Notes

- This calculator uses floating-point arithmetic, which may lead to small inaccuracies for certain calculations due to the nature of how computers represent decimal numbers.
- The history is not persistent and will be cleared when the program is terminated.
