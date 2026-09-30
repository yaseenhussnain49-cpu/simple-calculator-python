Simple Calculator

A beginner-level command-line calculator developed using Python. The program performs addition, subtraction, multiplication, and division on two numbers.

1. Project Overview

The Simple Calculator accepts two numbers from the user and allows the user to select an arithmetic operation.

The available operations are:

- Addition
- Subtraction
- Multiplication
- Division

The program also handles division by zero and allows the user to perform multiple calculations.

The project is completely command-line based and does not require a graphical interface.

---

2. Requirements

Before running the project, make sure the following is installed:

- Python 3.x
- A terminal or command prompt

No external Python libraries or packages are required.

---

3. Environment Setup

Step 1: Install Python

Download and install Python 3 from the official Python website if it is not already installed.

During installation on Windows, make sure the option to add Python to PATH is enabled.

Step 2: Verify Python Installation

Open a terminal or command prompt and run:

python --version

If "python" does not work on your system, try:

python3 --version

A Python 3.x version should be displayed.

---

4. Getting the Project

Clone the repository using:

 git clone https://github.com/yaseenhussnain49-cpu/simple-calculator-python.git
Then move into the project directory:
cd simple-calculator-python

Alternatively, the repository can be downloaded as a ZIP file and extracted.

---

5. Dependencies

This project does not use any external dependencies.

Only the standard Python interpreter is required.

Therefore, there is no "pip install" command necessary.

No "requirements.txt" file is required for this project.

---

6. Configuration

No additional configuration is required.

The calculator takes all required information directly from the user through the terminal.

---

7. Running the Project

Make sure you are inside the project directory.

Run the program using:

python calculator.py

If your system uses "python3", run:

python3 calculator.py

The calculator will then start in the terminal.

---

8. How to Use

Step 1

Enter the first number when prompted.

Step 2

Enter the second number.

Step 3

Select an operation:

1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division

Step 4

The program displays the result.

Step 5

Choose whether to perform another calculation:

5 - Perform another calculation
6 - Exit

---

9. Example

-----------SIMPLE CALCULATOR---------
Enter the first number 10
Enter the second number 5

Enter 1 if you want to add them
Enter 2 if you want to subtract them
Enter 3 if you want to multiply them
Enter 4 if you want to divide them

Enter your choice 1
15.0

Enter 5 if you want to perform another calculation
Enter 6 if you want to exit
Enter your choice 6

------------Thank you!!------------

Division by Zero

If the user attempts to divide by zero, the program displays:

DIVISION BY ZERO IS NOT POSSIBLE!!!!

The program then allows the user to perform another calculation.

---

10. Project Structure

The repository should have the following structure:

Simple-Calculator/
│
├── README.md
└── calculator.py

"README.md" contains the project documentation and instructions.

"calculator.py" contains the Python source code.

---

11. Features

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers
- Division-by-zero handling
- Multiple calculations in one execution
- Command-line execution
- No external dependencies

---

12. Python Concepts Used

This project uses basic Python concepts including:

- Variables
- "input()"
- "print()"
- "int()"
- "float()"
- "while" loop
- "if" statements
- Arithmetic operators
- "continue"
- User input and output

---

13. Limitations

- Only four basic arithmetic operations are supported.
- Invalid non-numeric input is not currently handled.
- The program runs through the command line.
- Advanced mathematical operations are not included.

---

14. Future Improvements

Possible future improvements include:

- Adding modulus and exponentiation.
- Adding more mathematical operations.
- Improving input validation.
- Adding support for more than two numbers.
- Creating a graphical user interface in a future version.

---

15. Author

Yaseen Hussnain

This project was created as a beginner Python programming project.
