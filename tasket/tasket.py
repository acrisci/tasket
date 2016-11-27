#from functools import wraps
import sys
import inspect
import os
from .task import Task
from argparse import ArgumentParser, RawTextHelpFormatter

class Tasket():
    tasks = {}

    def __init__(self):
        pass

    @staticmethod
    def add_task(task):
        Tasket.tasks[task.name] = task

    @staticmethod
    def find(name):
        if name not in Tasket.tasks:
            return None
        else:
            return Tasket.tasks[name]

    @staticmethod
    def has_task(name):
        if name not in Tasket.tasks:
            return False
        else:
            return True


    @staticmethod
    def get_tasks():
        return list(Tasket.tasks.values())

    @staticmethod
    def get_epilog():
        target_texts = ["\ntargets:"]

        # right justification of the text in length of spaces
        just_len = max(len(name) for name in
                       [n.name for n in Tasket.get_tasks()])
        just_len += 5

        # TODO: it would be nice to order the tasks by dependencies here,
        # putting tasks that are lower in the chain first
        for task in Tasket.get_tasks():
            txt = "  {}".format(task.name).ljust(just_len)
            txt += "- {}".format(task.description)
            target_texts.append(txt)

        return str.join("\n", target_texts)


    def run(self, argv=sys.argv):
        # XXX won't work if they chdir before the call to run
        script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

        print('task runner running')
        parser = ArgumentParser(epilog=Tasket.get_epilog(),
                                formatter_class=RawTextHelpFormatter)

        parser.add_argument('targets',
                            nargs='*')
        args = parser.parse_args(argv[1:])

        if not args.targets:
            parser.print_help()
            sys.exit(0)

        # validate tasks
        for task in Tasket.get_tasks():
            for d in task.dependencies:
                if not Tasket.has_task(d):
                    parser.error('could not find dependency for task %s: %s' % (task.name, d))

        # validate target arguments
        for target_name in args.targets:
            if not Tasket.find(target_name):
                parser.error('could not find target: %s' % target_name)


        # run the targets in order
        for name in args.targets:
            task = Tasket.find(name)
            # first run all the dependencies
            for d in task.dependencies:
                dependency_task = Tasket.find(d)
                dependency_task.run(args, script_dir)


            # run the task itself
            task.run(args, script_dir)


def task(name='', dependencies=[]):
    if callable(name):
        # the decorator was given with no arguments
        func = name
        task_name = func.__name__
        dependencies = []
        current_task = Task(task_name, func, dependencies)
        Tasket.add_task(current_task)
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
            Tasket.add_task(current_task)
            
            def wrapper(*args, **kwargs):
                print('running the wrapper for %s' % current_task.name)
                # TODO call with our args
                return func(args)

            return wrapper

        return decorator
