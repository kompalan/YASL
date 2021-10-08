from compiler.exceptions import SourceParsingException
from compiler.rply import ParserGenerator

def do_source_parsing(tokens, possible_tokens):
    precedence = [
        ('left', ['ASSIGN']),
        ('left', ['LOGIC_BINARY_OP', 'MATH_NARY_OP', 'LOGIC_UNARY_OP', 'LOGIC_NARY_OP', 'COMPARE_BINARY_OP']),
        ('left', ['MATH_PLUS']),
        ('left', ['MATH_BINARY_OP']),
        ('right', ['MATH_MINUS'])
    ]
    pg = ParserGenerator(possible_tokens, precedence)

    #If we have an error, call this function
    @pg.error  # Note the lack of ()
    def error_handler(p):
        print(f'There was an error processing {p}')
        print(f'Source position {p.source_pos}')


    @pg.production('statement_list : ')
    @pg.production('statement_list : statement EOC statement_list')
    def start(p):
        pass

    
    @pg.production('statement : expr')
    @pg.production('statement : command')
    @pg.production('statement : ')
    def statement(p):
        pass
    

    @pg.production('expr : SCALAR_TYPE IDENTIFIER')
    @pg.production('expr : SCALAR_TYPE IDENTIFIER ASSIGN expr')
    def declare(p):
        pass

    @pg.production('expr : INT_LITERAL')
    def int_literal(p):
        pass

    @pg.production('expr : BOOL_LITERAL')
    def bool_literal(p):
        pass
    
    @pg.production('expr : IDENTIFIER')
    def identifier(p):
        pass

    @pg.production('expr : IDENTIFIER ASSIGN expr')
    def assign(p):
        pass

    @pg.production('expr : MATH_MINUS expr')
    def negate(p):
        pass

    @pg.production('expr : PAREN_OPEN expr PAREN_CLOSE')
    def parenthetical(p):
        pass

    @pg.production('expr : expr MATH_BINARY_OP expr')
    @pg.production('expr : expr MATH_PLUS expr')
    @pg.production('expr : expr MATH_MINUS expr')
    def binary(p):
        pass
    
    @pg.production('expr : LOGIC_UNARY_OP expr')
    def logic_unary(p):
        pass

    @pg.production('expr : expr LOGIC_BINARY_OP expr')
    def logic_binary_op(p):
        pass

    @pg.production('list : expr COMMA list')
    @pg.production('list : expr')
    def list_expr(p):
        pass
    
    @pg.production('expr : LOGIC_NARY_OP BRACE_OPEN list BRACE_CLOSE')
    def logic_nary_op(p):
        pass

    @pg.production('expr : MATH_NARY_OP BRACE_OPEN list BRACE_CLOSE')
    def logic_nary_op(p):
        pass

    @pg.production('expr : expr COMPARE_BINARY_OP expr')
    def compare_binary_op(p):
        pass
    
    @pg.production('expr : INPUTTING')
    def inputting(p):
        pass



    @pg.production('command : PRINTING BRACE_OPEN list BRACE_CLOSE')
    def printing(p):
        pass

    return pg.build()

