import model
import view

# def my_func():
#     raise NotImplementedError()

def my_func():
    num_1 = model.parsing(view.data_in())
    num_2 = model.parsing(view.data_in())
    oper = view.data_op()
    result = model.calculate(num_1, num_2, oper)
    view.print_result(result)

my_func()
