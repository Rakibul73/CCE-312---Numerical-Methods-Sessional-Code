from sympy import *


def derivative_maximum_value_calculator(function_expression, interval):
    # find maximum value of derivation function at a given interval
    derivative_symbol = symbols('x')
    derivative_function = sympify(function_expression)
    return calculus.util.maximum(derivative_function, derivative_symbol, Interval(interval[0], interval[1]))


def trapezoid_integration(interval, function_expression, partitions=6):
    h = (interval[1] - interval[0]) / partition
    function_variable = var("x")
    function = sympify(function_expression)
    integration_value = function.subs(function_variable, interval[0]) / 2  # calculating function value
    for i in range(1, partitions):
        integration_value += function.subs(function_variable, interval[0] + i * h)  # calculating function value
    integration_value += function.subs(function_variable, interval[1]) / 2  # calculating function value
    second_derivative = diff(function, "x", 2)  # differentiate function by sympy
    second_derivative_maximum_value = derivative_maximum_value_calculator(second_derivative, interval)
    maximum_integration_error = -(pow(h, 3) / 12) * second_derivative_maximum_value
    return "integration value: {}, integration maximum error: {}".format(integration_value, maximum_integration_error)


if __name__ == '__main__':
    given_interval = eval(input("please enter and interval like [a, b] where a and b are numbers: "))
    given_function = input("please enter a function like 2 * x + 3 * sin(x)")
    print(trapezoid_integration(given_interval, given_function))