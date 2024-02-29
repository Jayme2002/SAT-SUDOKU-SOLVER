#!/usr/bin/env python3
import sys


def variable(i, j, k):
    res = 81 * (i - 1) + 9 * (j - 1) + (k - 1) + 1
    
    return res


def inverse_variable(variable):
    variable -= 1  # Adjust back by subtracting 1
    k = (variable % 9) + 1
    j = (variable // 9) % 9 + 1
    i = (variable // 81) + 1
    return i, j, k


def encode_every_cell_has_number(vars_set):
  
    clauses = []
    for i in range(1, 10):
        for j in range(1, 10):
            cell_clauses = []
            for k in range(1, 10):

                X_ijk = variable(i, j, k)
                vars_set.add(X_ijk)
                cell_clauses.append(X_ijk)
            clauses.append(cell_clauses)
    return clauses


def encode_unique_numbers_in_rows(vars_set):
   
    clauses = []
    for i in range(1, 10):
        for k in range(1, 10):
            for j in range(1, 9):
                for l in range(j + 1, 10):
                    X_ijk = variable(i, j, k)
                    X_ilk = variable(i, l, k)
                    vars_set.add(X_ijk)
                    vars_set.add(X_ilk)
                    clauses.append([-X_ijk, -X_ilk])
    return clauses


def encode_unique_numbers_in_cols(vars_set):
    
    clauses = []
    for j in range(1, 10):
        for k in range(1, 10):
            for i in range(1, 9):
                for l in range(i + 1, 10):
                    X_ijk = variable(i, j, k)
                    X_ljk = variable(l, j, k)
                    vars_set.add(X_ijk)
                    vars_set.add(X_ljk)
                    clauses.append([-X_ijk, -X_ljk])
    return clauses


def encode_prefilled_cells(sudoku_grid, vars_set):
   
    clauses = []
    for i, row in enumerate(sudoku_grid, start=1):
        for j, cell in enumerate(row, start=1):
            if cell not in ("?", ".", "*", "0"):
                k = int(cell)
                X_ijk = variable(i, j, k)
                vars_set.add(X_ijk)
                clauses.append([X_ijk])  # Add a clause to lock this cell to its value
    return clauses


def encode_number_at_most_once_in_every_sub_grid(set_of_vars):
   
    clauses = []
    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                for u in range(1, 4):
                    for v in range(1, 3):
                        for w in range(v + 1, 4):
                            v1 = variable(3 * a + u, 3 * b + v, k)
                            v2 = variable(3 * a + u, 3 * b + w, k)
                            set_of_vars.add(v1)
                            set_of_vars.add(v2)
                            clauses.append([-v1, -v2])
    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                for u in range(1, 3):
                    for v in range(1, 4):
                        for w in range(u + 1, 4):
                            for t in range(1, 4):
                                v1 = variable(3 * a + u, 3 * b + v, k)
                                v2 = variable(3 * a + w, 3 * b + t, k)
                                set_of_vars.add(v1)
                                set_of_vars.add(v2)
                                clauses.append([-v1, -v2])
    return clauses

def encode_at_most_one_number_per_cell(vars_set):
    clauses = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k1 in range(1, 10):
                for k2 in range(k1 + 1, 10):  # Ensure k2 > k1 to avoid duplicate pairs
                    X_ijk1 = variable(i, j, k1)
                    X_ijk2 = variable(i, j, k2)
                    vars_set.add(X_ijk1)
                    vars_set.add(X_ijk2)
                    # If k1 is in the cell, k2 cannot be, and vice versa
                    clauses.append([-X_ijk1, -X_ijk2])
    return clauses


def encode_every_number_at_least_once_in_rows(vars_set):
    clauses = []
    for i in range(1, 10):
        for k in range(1, 10):
            row_clause = []
            for j in range(1, 10):
                X_ijk = variable(i, j, k)
                vars_set.add(X_ijk)
                row_clause.append(X_ijk)
            clauses.append(row_clause)
    return clauses


def encode_every_number_at_least_once_in_cols(vars_set):
    clauses = []
    for j in range(1, 10):
        for k in range(1, 10):
            col_clause = []
            for i in range(1, 10):
                X_ijk = variable(i, j, k)
                vars_set.add(X_ijk)
                col_clause.append(X_ijk)
            clauses.append(col_clause)
    return clauses

def encode_every_number_at_least_once_in_sub_grids(vars_set):
    clauses = []
    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                sub_grid_clause = []
                for u in range(1, 4):
                    for v in range(1, 4):
                        X_ijk = variable(3 * a + u, 3 * b + v, k)
                        vars_set.add(X_ijk)
                        sub_grid_clause.append(X_ijk)
                clauses.append(sub_grid_clause)
    return clauses

def encode_sudoku(sudoku_grid):
    clauses = []
    set_of_vars = set()
    # Existing constraints
    clauses.extend(encode_every_cell_has_number(set_of_vars))
    clauses.extend(encode_unique_numbers_in_rows(set_of_vars))
    clauses.extend(encode_unique_numbers_in_cols(set_of_vars))
    clauses.extend(encode_number_at_most_once_in_every_sub_grid(set_of_vars))
    clauses.extend(encode_prefilled_cells(sudoku_grid, set_of_vars))
    # Extended constraints
    clauses.extend(encode_at_most_one_number_per_cell(set_of_vars))
    clauses.extend(encode_every_number_at_least_once_in_rows(set_of_vars))
    clauses.extend(encode_every_number_at_least_once_in_cols(set_of_vars))
    clauses.extend(encode_every_number_at_least_once_in_sub_grids(set_of_vars))
    return clauses, set_of_vars


def convert_into_dimac(clauses, set_of_vars):
    """
    p cnf <# variables> <# clauses>
    <list of clauses>

    Each clause is given by a list of non-zero numbers terminated by a 0.
    Each number represents a literal. Positve numbers 1,2,... are unnegated variables.
    Negative numbers are negated variables. Comment lines preceded by a c are allowed.
    For example the CNF formula (x1 ∨ x3 ∨ x4) ∧ (¬x1 ∨ x2) ∧ (¬x3 ∨ ¬x4) would be given by the following file:
    c A sample file p cnf 4 3 1340
    -1 2 0
    -3 -4 0

    so #variables would probably be the number of distinct integers
    and the #clauses would be the length of each clause
    """
  
    res = f"p cnf {len(set_of_vars)} {len(clauses)}"
    for c in clauses:
        res += "\n"
        res += " ".join([str(num) for num in c]) + " 0"
    return res


if __name__ == "__main__":

    soduko_input = sys.stdin.read()

    parsed_soduko_input = ""
    for c in soduko_input:
        if c.isdigit() or c in ("?", ".", "*"):
            parsed_soduko_input += c

    soduko_input = parsed_soduko_input

    soduko_grid = []
    for i in range(9):
        row = soduko_input[i * 9 : i * 9 + 9]
        row = list(row)
        soduko_grid.append(row)

    clauses, vars_set = encode_sudoku(soduko_grid)
    dimac_format = convert_into_dimac(clauses, vars_set)
    print(dimac_format)
