# SAT-SUDOKU-SOLVER

# **SAT Sudoku Solver**

This Python-based SAT Sudoku Solver leverages SAT (Boolean satisfiability problem) solving techniques to efficiently solve Sudoku puzzles. By encoding Sudoku rules into a series of logical constraints, this solver transforms Sudoku puzzles into a CNF (Conjunctive Normal Form) format that can be processed by any SAT solver. This transformation allows for the rapid identification of solutions to even the most challenging Sudoku puzzles.

## **Features**
**Variable Encoding:** Converts Sudoku cell positions and possible values into unique variables, facilitating their representation in SAT format.

**Constraint Encoding:** Implements a comprehensive set of Sudoku rules, including cell uniqueness, row, column, and sub-grid constraints, as well as handling pre-filled cells.

**Inverse Variable Mapping:** Provides functionality to map SAT solver output back to Sudoku grid coordinates, enabling the reconstruction of the solved puzzle.

**Performance Metrics:** Parses SAT solver output to extract performance metrics such as CPU time, memory usage, and conflict resolution details, aiding in the analysis of solver efficiency.
Usage

## **How To Use Solver**

**Step 1: Cloning the Repository**
git clone https://github.com/jayme2002/sat-sudoku-solver.git

**Step 2: Run Program**
Write the following commands:
chmod u+x sud2sat.py
chmod u+x sat2sud.py

./sud2sat.py < top_95/top_95_1.txt > puzzle.cnf

minisat puzzle.cnf assign.txt > stat.txt

./sat2sud.py < assign.txt > solution.txt

cat solution.txt

After executing the above commands the solved sudoku puzzle will be output to the terminal

*KEEP IN MIND MINISAT EXECUTABLE MUST BE INSTALLED TO RUN PROPERLY*

## **Example**
<div>
<img width="86" alt="Screenshot 2024-02-29 at 2 28 10 PM" src="https://github.com/Jayme2002/SAT-SUDOKU-SOLVER/assets/132419605/51430609-351e-4612-aec3-129b40ca0ebd"><img width="93" alt="Screenshot 2024-02-29 at 2 28 38 PM" src="https://github.com/Jayme2002/SAT-SUDOKU-SOLVER/assets/132419605/02d898c5-3c96-48ff-9870-5992f6391109">


</div>

##**How to Use Parser**

**Step 1: Make sure Script can be executed**
Run the command: chmod u+x parse.py

**Step 2: Run the parser**
Run the command: python3 parse.py <top_95_stats >test_results.csv

This will create a file named test_results.csv that holds detailed statistics regarding the performance of the sudoku solver. This was used to refine the solver to become more efficient.

<img width="365" alt="Screenshot 2024-02-29 at 2 22 52 PM" src="https://github.com/Jayme2002/SAT-SUDOKU-SOLVER/assets/132419605/9296fb2c-e1a8-4849-88bb-acb4c7efa6f6">



