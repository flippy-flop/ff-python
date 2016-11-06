"""
 An implementation of the Flippy Flop data structure.
 The Flippy Flop is backed by a list with a few quirks.
"""

from random import randint

class FlippyFlop(object):
    def __init__(self):
        self._data = []

    @property
    def count(self):
        return len(self._data)
    
    def flip(self, element):
        success = randint(0, 1) > 0
        if success:
            position = randint(0, self.count)
            self._data.insert(position, element)
        return success

    def flop(self):
        ret = None
        if self.count > 0:
            position = randint(0, self.count - 1)
            ret = self._data[position]
            shouldRemove = randint(0, 1) > 0
            if shouldRemove:
                self._data.pop(position)
        return ret
