from itertools import permutations, product

"""
Riddle:
Young Saul, a budding mathematician and printer, is making
himself a fake ID. He needs it to say he’s 21. The problem
is he’s not using a computer, but rather he has some
symbols he’s bought from the store, and that’s it. He has
one 1, one 5, one 6, one 7, and an unlimited supply of + – * /
(the operations addition, subtraction, multiplication and
division). Using each number exactly once (but you can use
any number of +, any number of -, …) how can he get 21 from 
1, 5, 6, 7?

Note: you can’t do things like 15+6 = 21. You have to use the
four operations as ‘binary’ operations: ((1+5)*6)+7.
"""

var_integer_list = [1, 5, 6, 7]
var_target = 20


def calculate(problem_list):

    while '/' in problem_list or '*' in problem_list or '+' in problem_list or '-'in problem_list:
        for each in range(len(problem_list)):
            if problem_list[each] == '/':
                problem_list[each] = problem_list[each - 1] / problem_list[each + 1]
                del problem_list[each-1]
                del problem_list[each]
                break
            elif problem_list[each] == '*':
                problem_list[each] = problem_list[each - 1] * problem_list[each + 1]
                del problem_list[each-1]
                del problem_list[each]
                break
            elif problem_list[each] == '+':
                problem_list[each] = problem_list[each - 1] + problem_list[each + 1]
                del problem_list[each-1]
                del problem_list[each]
                break
            elif problem_list[each] == '-':
                problem_list[each] = problem_list[each - 1] - problem_list[each + 1]
                del problem_list[each-1]
                del problem_list[each]
                break

    return problem_list[0]


def operations_solver(integer_list, target):

    integer_count = len(integer_list)
    integer_combo_list = list(permutations(integer_list))
    operators_list = ['+', '-', '*', '/']
    operators_combo_list = list(product(operators_list, repeat=integer_count-1))

    for int_combo in integer_combo_list:
        for op_combo in operators_combo_list:
            test_equation_list = [int_combo[0]]

            for each in range(integer_count - 1):
                test_equation_list.append(op_combo[each])
                test_equation_list.append(int_combo[each + 1])

            arbitrary_list = []
            for each in test_equation_list:
                arbitrary_list.append(str(each))
            solution_text = ''.join(arbitrary_list)

            if float(calculate(test_equation_list)) == float(target):
                print(solution_text, test_equation_list)


operations_solver(var_integer_list, var_target)
