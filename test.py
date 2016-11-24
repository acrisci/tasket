#!/usr/bin/env python3

from tasket import task, Tasket

app = Tasket()

@task
def generate(args):
    print('generating with args = %s' % args)

@task(dependencies=['generate'],
      description='Build the project')
def build(args):
    print('building with args = %s' % args)

@task(dependencies=['generate', 'build'],
      description='Send the packages to the release servers')
def release(args):
    print('releasing with args = %s' % args)

app.run()
