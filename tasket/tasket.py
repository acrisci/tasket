#from functools import wraps
import sys
import inspect
from .task_runner import TaskRunner
from .task import Task

class Tasket():
    runner = TaskRunner()

    def __init__(self):
        pass

    def run(self, argv=sys.argv):
        Tasket.runner.run(argv)


def task(name='', dependencies=[]):
    if callable(name):
        # the decorator was given with no arguments
        func = name
        task_name = func.__name__
        dependencies = []
        current_task = Task(task_name, func, dependencies)
        Tasket.runner.add_task(current_task)
        def wrapper(*args, **kwargs):
            # TODO call with our args
            func(args)

        return wrapper

    else:
        # the decorator was called with arguments
        def decorator(func):
            task_name = name
            if name == '':
                task_name = func.__name__
            current_task = Task(task_name, func, dependencies)
            Tasket.runner.add_task(current_task)
            
            def wrapper(*args, **kwargs):
                print('running the wrapper for %s' % current_task.name)
                # TODO call with our args
                return func(args)

            return wrapper

        return decorator
