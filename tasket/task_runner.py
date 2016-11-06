import sys
from argparse import ArgumentParser

class TaskRunner():
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.name] = task

    def find(self, name):
        return self.tasks[name]

    def get_tasks(self):
        return list(self.tasks.values())

    def run(self, argv):
        print('task runner running')
        parser = ArgumentParser()
        parser.add_argument('--asdf')
        args = parser.parse_args(argv[1:])
        print(args)
