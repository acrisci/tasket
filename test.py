#!/usr/bin/env python3

from tasket import task, Tasket

app = Tasket()

@task
def generate(args):
    print('generating with args = %s' % args)

@task(dependencies=['generate'])
def build(args):
    print('building with args = %s' % args)

app.run()
