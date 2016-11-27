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
    print('generating with args = %s' % args)

@task(dependencies=['generate'])
def build(args):
    print('building with args = %s' % args)

app.run()
```

## TODO

* Add arguments
* Subtaskets
* Built in help command
* Retry file
* No dependencies run
* Documentation

### Future Todos

* CI Website
* Cross-machine subtaskets
* Plugins
