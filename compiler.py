from .lexing import do_source_lexing
from .parsing import do_source_parsing

def parse_source(source_code):
    tokens, possible_tokens = lex_source(source_code)
    
    parser = do_source_parsing(tokens, possible_tokens)
    result = parser.parse(iter(tokens))

def lex_source(src):
    tokens, possible_tokens = do_source_lexing(src)
    return tokens, possible_tokens

