import ply.lex as lex

#Antonieta Rodriguez Dolores - A01737276
# Actualizado: 14 de abril 2024

#Token
tokens = [ 'INT', 'FLOAT', 'STR' ]

#Especifica los caracteres a ignorar
t_ignore  = ' \t'

def t_STR(t):
    #r'"[^"]*"'
    r'"(\\.|[^\\"])*"'
    t.value = str(t.value)
    return t

#Declaro una funcion para manejar los tokens de tipo flotante
def t_FLOAT(t):
    r'\d*(_\d)*\.\d*([eE][-+]?\d+(_\d)*)?|[1-9][E][1-9](_\d)*'
    t.value = float(t.value)
    return t

#Declaro una funcion para manejar los tokens de tipo entero
def t_INT(t):
    r'\d+(_\d)*'
    t.value = int(t.value)
    return t

#Instancia del analizador lexico
def getLexer():
  return lex.lex()

