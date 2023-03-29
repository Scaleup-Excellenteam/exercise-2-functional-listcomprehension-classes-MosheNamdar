from time import time


def timer(f, *args, **kwargs):
    """
      A function that times the execution of a given function and returns the time taken.

      Args:
      f (function): A function to be timed.
      *args: Any number of positional arguments to be passed to the function.
      **kwargs: Any number of keyword arguments to be passed to the function.

      Returns:
      the_final_time (float): The time taken to execute the given function.
      """
    start = time()
    f(*args, **kwargs)
    finish = time()
    the_final_time = finish - start
    return the_final_time


#a = timer(print, "Hello")
#b = timer(zip, [1, 2, 3], [4, 5, 6])
#c = timer("Hi {name}".format, name="Bug")
#print(c)