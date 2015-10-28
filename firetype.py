#!/usr/bin/env python

# The FireType interpreter.
# Runs under Python 2 and 3.
import sys

class Array(object):
    def __init__(self):
        self.array = []
        self.ptr = 0

    def push_zero(self):
        if self.ptr == len(self.array):
            self.array.append(0)
        else:
            self.array[self.ptr] = 0
        self.ptr += 1

    def left(self):
        self.ptr -= 1
        assert self.ptr >= 0 and self.array, 'pointer underflow (at %d)' % i

    def right(self):
        self.ptr += 1
        assert self.ptr <= len(self.array), 'pointer overflow (at %d)' % i

    def sort(self):
        lhs = self.array[:self.ptr-1]
        rhs = self.array[self.ptr-1:]
        lhs.sort()
        lhs.reverse()
        self.array = lhs + rhs

    def __call__(self, *args):
        args = list(args)
        assert self.array, 'out-of-bounds (at %d)' % i
        if not args:
            return self.array[self.ptr-1]
        self.array[self.ptr-1] = args.pop()
        assert not args

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return 'Array(array=%s, ptr=%s)' % (self.array, self.ptr)

    def __repr__(self):
        return 'Array(array=%r, ptr=%r)' % (self.array, self.ptr)

def execute(lines):
    global i, array
    i = 0
    array = Array()
    rep = 0
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue
        line = line[0]
        if line == '_':
            array.push_zero()
        elif line == '+':
            array(array() + 1)
        elif line == '-':
            array(array() - 1)
        elif line == '*':
            array(array() * 2)
        elif line == '/':
            array(int(array() / 2))
        elif line == '%':
            i += array()
            array.left()
        elif line == '=':
            i = array()-1
            array.left()
        elif line == ',':
            array.push_zero()
            array(ord(sys.stdin.read(1)))
        elif line == '.':
            sys.stdout.write(str(array()))
        elif line == '!':
            rep = array()
            array.left()
            i += 1
        elif line == '<':
            array.left()
        elif line == '>':
            array.right()
        elif line == '^':
            array(int(chr(array())))
        elif line == '~':
            array(int(not array()))
        elif line == '|':
            array(array() ** 2)
        elif line == '@':
            array(len(array))
        elif line == '`':
            top = array()
            array.push_zero()
            array(top)
        elif line == '\\':
            array.sort()
        elif line == '#':
            array(-array())

        if rep:
            rep -= 1
        else:
            i += 1

def main(args):
    try:
        _, path = args
    except ValueError:
        sys.exit('usage: %s <file to run, - for stdin>')

    if path == '-':
        data = sys.stdin.read()
    else:
        with open(path) as f:
            data = f.read()

    try:
        execute(data.split('\n'))
    except:
        print('ERROR!')
        print('Array was %r' % array)
        print('Re-raising error...')
        raise

if __name__ == '__main__':
    main(sys.argv)
