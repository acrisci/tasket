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


@task(dependencies=['build'])
def release(args):
    """
    Send the packages to the release servers

    More description here
    """
    print('releasing with args = %s' % args)


@task(dependencies=['release'])
def fail_depends(args):
    '''This failing dependency demonstrates the retry feature'''
    print('failing')
    #raise Exception('fail-depends has failed!')
    pass


@task(dependencies=['fail_depends'])
def fail(args):
    print('not reached')


@task(dependencies=['generate', 'circular2'])
def circular1(args):
    '''This tests how circular dependencies work'''
    print('running circular1')


@task(dependencies=['circular1'])
def circular2(args):
    '''This tests how circular dependencies work'''
    print('running circular2')


app.add_argument('--build-type',
                 default='Debug',
                 choices=['Debug', 'Release'])


if __name__ == '__main__':
    app.run()
