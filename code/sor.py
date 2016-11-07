"""
Write a program to implement the Spare-SOR algorithm for solving a system of n
linear equations in n unknowns.
Ax = b
with A a nxn matrix in R and x, b nx1 vectors in R
"""

try:
    import numpy as np
    import sys
    from bin import get_filename, raw_input_check, read_inputs, \
        input_checks, convert_to_csr, value_checks, solve_sor, vector_norm, \
        calculate_residual, write_output
except ImportError as import_err:
    print(import_err)
    print("Unable to import required libraries. Please check installation of "
          "sys, numpy, os & re libraries for python 3.5")
    exit(0)


def main():
    input_filename, output_filename = get_filename.check_CM_args(sys.argv)

    if not raw_input_check.read_raw_inputs(input_filename):
        exit("There is a non-decimal entry in the input file. Please amend "
             "the input according to the guidelines in README.md")

    errors = []

    val, col, rowStart, vector_b = read_inputs.read_inputs(input_filename)
    print('Val: ', val, type(val))
    print('Col: ', col, type(col))
    print('rowStart: ', rowStart, type(rowStart))
    print('vector_b: ', vector_b, type(vector_b))

    """
    errors.extend(input_checks.csr_input_checks(val, col, rowStart, vector_b))

    errors = value_checks.value_tests(val, col, rowStart, errors)

    if len(errors) != 0:
        print("The following errors were identified:\n")
        for i in errors:
            print('   - ' + i)
        exit("\nPlease correct these errors and restart the program")

    # Set tolerance
    tol = 1 * 10 ** (-10)

    # Calculate n
    n = rowStart.size - 1

    # Set maximum iterations
    maxits = 100

    w = 1.3
    x = solve_sor.create_initial_x(val, col, rowStart, vector_b, n)
    e = np.finfo(float).eps

    x, stop, maxits, iterations, xseqtol, residual = \
    solve_sor.sor(val, col, rowStart, vector_b, n, maxits, w, x, e, tol)

    # outputs
    write_output.output_text_file(output_filename, stop, maxits, iterations,
                                  e, xseqtol, residual ,w, x)
    """





if __name__ == '__main__':
    main()