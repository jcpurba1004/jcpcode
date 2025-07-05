def __eq__(self, other):
    """Tests self and other for equality."""
    if self is other:                   # Object identity?
        return True
    elif type(self) != type(other):     # Types match?
        return False
    else:
        return self.numer == other.numer and \
               self.denom == other.denom
