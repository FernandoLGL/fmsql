################################################################################
#                  Autores: Fernando Rosendo e Marcel Souza
#                    Arquivo: "ast.py" (Arvore Sintatica)
################################################################################

#Árvore Sintática da nossa linguagem

#Não tenho certeza se precisa de uma classe pro separador ','

#Tudo está retornando strings

class Num():
    def __init__(self,value):
        self.value = value

    def eval(self):
        return str(int(self.value))

class OpBinaria():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Grt(OpBinaria):
    def eval(self):
        return str(self.left.eval > self.right.eval)

class Lss(OpBinaria):
    def eval(self):
        return str(self.left.eval < self.right.eval)

class Eq(OpBinaria):
    def eval(self):
        return str(self.left.eval == self.right.eval)

class Select():

    #Na versão v0.6 , pode tirar o * do args pra conseguir mostrar(só uma
    #coluna) ao executar o main. Pra voltar a mostrar tupla, colocar o *
    def __init__(self,args, origem, where="teste", box_x="teste", box_y="teste"):
        self.cols = args
        self.origem = origem
        self.where = where
        self.box_x = box_x
        self.box_y = box_y

    def eval(self):
        return f'Selecionadas colunas {self.cols} de {self.origem}, onde {self.where} segue uma condicao, boxplot em x={self.box_x} e y={self.box_y}'

class String():
    def __init__(self,value):
        self.value = value
    
    def eval(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

#class From():
#
#    def __init__(self, origem):
#        self.origem = origem
#
#    def eval(self):
#        return 'da base ' + str(self.origem)

#class Where():
#
#    def __init__(self, col, op, val):
#        self.col = col
#        self.op = op
#        self.val = val
#
#    def eval(self):
#        return ' onde ' + self.col + self.op + ' ' + str(self.val)

#class Boxplot():
#
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#    def eval(self):
#        return ' fazer boxplot de x: ' + self.x + ' e y: ' + self.y

#class Print():
#    def __init__(self, value):
#        self.value = value
#
#    def eval(self):
#        print(self.value.eval())
