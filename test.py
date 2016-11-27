#!/usr/bin/env python3

from tasket import task, Tasket

app = Tasket()

@task
def generate(args):
    print('generating with args = %s' % args)


@task(dependencies=['generate'])
def build(args):
    """Build the project"""
    print('building with args = %s' % args)


@task(dependencies=['generate', 'build'])
def release(args):
    """
    Send the packages to the release servers

    More description here
    """
    print('releasing with args = %s' % args)


app.add_argument('--build-type',
                 default='Debug',
                 choices=['Debug', 'Release'])


if __name__ == '__main__':
    app.run()
