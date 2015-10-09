class Bird:
    def __init__(self, kind, call):
        self._kind = kind
        self._call = call

    def do_call(self):
        print 'a %s goes %s' % (self._kind, self._call)


class Parrot(Bird):
    def __init__(self):
        Bird.__init__(self, 'Parrot', 'Kah!')
