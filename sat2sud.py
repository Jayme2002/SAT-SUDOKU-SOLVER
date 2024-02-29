import sys


def inverse_variable(variable):
    variable -= 1  # Adjust back by subtracting 1
    k = (variable % 9) + 1
    j = (variable // 9) % 9 + 1
    i = (variable // 81) + 1
    return i, j, k


if __name__ == "__main__":
    soduko_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    sat_lines = sys.stdin.read().split("\n")
    if sat_lines[0] == "SAT":
        assignments = sat_lines[1]
        values = assignments.split(" ")
        for val in values:
            val = int(val)
            # valid assignment
            if val > 0:
                row, col, value = inverse_variable(val)
                soduko_grid[row - 1][col - 1] = value

        # output the soduko grid in specific format
        for row in soduko_grid:
            print("".join([str(n) for n in row[0:3]]), end=" ")
            print("".join([str(n) for n in row[3:6]]), end=" ")
            print("".join([str(n) for n in row[6:9]]), end="\n")
    else:
        print("unsatisfiable")
