# from antlr4 import *
# from YAPL.YAPLLexer import YAPLLexer
# from YAPL.YAPLParser import YAPLParser
# import subprocess

# # Importa la librería graphviz para graficar el árbol sintáctico
# from graphviz import Source

# def main():
#     file_path = "test/arith.cl"
#     # Carga el archivo de prueba
#     with open(file_path, 'r') as file:
#         input_stream = InputStream(file.read())
        
#         # Crea un lexer y un parser para procesar el archivo
#         lexer = YAPLLexer(input_stream)
#         stream = CommonTokenStream(lexer)
#         parser = YAPLParser(stream)
        
#         # Ejecuta el parser para obtener el árbol sintáctico
#         tree = parser.program()

#         # Imprime el árbol sintáctico en consola
#         print(tree.toStringTree(recog=parser))
 



# if __name__ == '__main__':
#     main()



# from antlr4 import *
# from YAPL.YAPLLexer import YAPLLexer
# from YAPL.YAPLParser import YAPLParser
# from antlr4.error.ErrorListener import ErrorListener
# import sys

# class CustomErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         # Imprime el mensaje de error
#         #print(f"Error en línea {line}:{column} - {msg}")
        
#         # Finaliza el programa

#         sys.exit(1)

# def main():
#     # Ruta al archivo de prueba
#     file_path = "test/arith.cl"
    
#     # Carga el archivo de prueba
#     with open(file_path, 'r') as file:
#         input_stream = InputStream(file.read())
        
#         # Crea un lexer y un parser para procesar el archivo
#         lexer = YAPLLexer(input_stream)
#         stream = CommonTokenStream(lexer)
#         parser = YAPLParser(stream)
        
#         # Registra el error listener personalizado
#         error_listener = CustomErrorListener()
#         parser.addErrorListener(error_listener)
        
#         # Ejecuta el parser para obtener el árbol sintáctico
#         tree = parser.program()
#         print(tree.toStringTree(recog=parser))


# if __name__ == '__main__':
#     main()


#---------------------------------------------------------
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from YAPL.YAPLParser import YAPLParser
from YAPL.YAPLLexer import YAPLLexer
from graphviz import Digraph
import shutil
import sys
import os


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Imprime el mensaje de error
        #print(f"Error en línea {line}:{column} - {msg}")
        
        # Finaliza el programa
        sys.exit(1)

def cleaner():
    if os.path.exists("output"):
        shutil.rmtree("output")

    # Crea la carpeta de salida si no existe
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    return output_folder

def main():
    output_folder = cleaner()

    # Ruta al archivo de prueba
    file_path = "test/arith.cl"
    
    # Carga el archivo de prueba
    with open(file_path, 'r') as file:
        input_stream = InputStream(file.read())
        
        # Crea un lexer y un parser para procesar el archivo
        lexer = YAPLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = YAPLParser(stream)
        
        # Registra el error listener personalizado
        error_listener = CustomErrorListener()
        parser.addErrorListener(error_listener)
        
        # Ejecuta el parser para obtener el árbol sintáctico
        tree = parser.program()
        print(tree.toStringTree(recog=parser))
        
    Grafic = Digraph()
    def nod(node, parent=None):
        if isinstance(node, ParserRuleContext):
            label = parser.ruleNames[node.getRuleIndex()]
        else:
            label = str(node)
        Grafic.node(str(id(node)), label=label)
        if parent is not None:
                Grafic.edge(str(id(parent)), str(id(node)))
        if isinstance(node, ParserRuleContext) and node.children is not None:
            for child in node.children:
                nod(child,parent=node)
    nod(tree)

    #Grafic.render('tree', format="png", view=False)

    # output_path = os.path.join(output_folder, "tree")
    # Grafic.render(output_path, format="png", view=False)

    output_path = os.path.join(output_folder, "tree.png")
    dot_data = Grafic.pipe(format='png')
    with open(output_path, 'wb') as file:
        file.write(dot_data)

if __name__ == '__main__':
    main()






