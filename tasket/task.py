class Task():
    def __init__(self, name, func, dependencies=[]):
        self.name = name
        self.dependencies = dependencies
        self.func = func
        self.has_run = False
        self.result = None

    def run(self, args):
        if self.has_run:
            return self.result

        self.result = self.func(args)
        self.has_run = True
        return self.result
