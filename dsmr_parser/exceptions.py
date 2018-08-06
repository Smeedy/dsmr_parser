class ParseContentError(Exception):
    pass

class InvalidChecksumError(ParseContentError):
    pass

class NoChecksumError(ParseContentError):
    pass
