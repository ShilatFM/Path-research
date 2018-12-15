import sys

def argument_cmd():
    # Reading input with the file name line
    arguments = sys.argv
    if len(arguments) == 1:
        print("goodby")
    else:
        print(arguments)

    # Reading input in the middle of the program
    end_input = 1
    while(end_input):
        var = input()
        arr_inputs = var.split(" ")
        print(var)
        print(arr_inputs)
        if var == 'close':
            end_input = 0

argument_cmd()