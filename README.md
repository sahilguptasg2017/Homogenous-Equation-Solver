# Homogeneous Equation Solver

This Python program solves a homogeneous system of linear equations of the form Ax=0, where A is a matrix and x is the vector of variables. The program accepts the size of the matrix (number of rows and columns) and the entries of matrix A as input. The solution is then presented in parametric vector form.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sahilguptasg2017/Homogenous-Equation-Solver.git
2. **Navigate to the Project Directory:**
   ```bash
   cd homogeneous-equation-solver
3. **Run the Program:**
   ```bash
   python homogeneous_solver.py
Follow the on-screen instructions to input the size of the matrix and its entries.
## Input
You can provide input in two ways:

- Interactive Mode: The program prompts you to enter the size of the matrix and its entries interactively.

- Text File Input (Optional): If you prefer, create a text file (input.txt) with the following format:
  ```bash
  3 3  # Number of rows and columns
  1 2 3
  4 5 6
  7 8 9
In this example, a 3x3 matrix is represented.
## Output
The program outputs the general solution of the homogeneous system in parametric vector form.
## Algorithm
The code implements algorithms learned in the course to solve the homogeneous system Ax=0.
