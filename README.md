# Tasket

A task runner library for Python.

**Work in progress**

## About

Tasket is a library for creating a task runner. The task
runner can simplify the task of generating, building, testing,
and releasing the project by abstracting this functionality
into a single script.

## Example

```python
from tasket import task, Tasket

app = Tasket()

@task
def generate(args):
    '''Generate the project'''
    print('generating the project now with, oh, say cmake')

@task(dependencies=['generate'])
def build(args):
    '''Build the project'''
    print('building the project now')

app.run()
```

This gives the following program.

```
usage: example.py [-h] [targets [targets ...]]

positional arguments:
  targets

optional arguments:
  -h, --help  show this help message and exit

targets:
  generate   - Generate the project
  build      - Build the project
```

Now pass the targets you want to complete.

```
$ ./example-tasket.py build

generating the project now with, oh, say cmake
building the project now
```

## TODO

* Subtaskets
* Built in help command
* Retry file
* No dependencies run
* Documentation

### Future Todos

* CI Website
* Cross-machine subtaskets
* Plugins
