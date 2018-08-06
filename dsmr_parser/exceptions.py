class ParseError(Exception):
    pass

class ParseErrorV4(Exception):
    pass

class InvalidChecksumError(ParseError):
    pass
