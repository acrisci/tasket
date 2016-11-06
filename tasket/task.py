class Task():
    def __init__(self, name, func, dependencies=[]):
        self.name = name
        self.dependencies = dependencies
        self.func = func

    def run(self, args):
        return self.func(args)
