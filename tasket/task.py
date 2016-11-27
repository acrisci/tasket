import os

class Task():
    def __init__(self, name, func, dependencies=[]):
        self.name = name
        self.dependencies = dependencies
        self.func = func
        self.has_run = False
        self.result = None

    @property
    def description(self):
        '''The description of a task is the first line of the doc string'''
        doc = self.func.__doc__

        if not doc:
            return ''

        return doc.lstrip().split("\n")[0].rstrip()

    def run(self, args, cwd):
        os.chdir(cwd)

        if self.has_run:
            return self.result

        self.result = self.func(args)
        self.has_run = True
        return self.result
