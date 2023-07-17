# Laboratorio0-GeneracionDeScannerYParser-ConstruccionDeCompiladores

<h1 align="center">
<br>
  <img src="https://mk0tuzolorusfnc7thxk.kinstacdn.com/wp-content/uploads/2016/02/antlr-logo.png" alt="MVC" width="440" height="160">
<br>

</h1>
<hr />

Existen dos maneras de ver el arbol una es con herramientas de antrl4 y otra con python:

## Con antlr4
1. `antlr -o lib YAPL.g4`
   * Se generaran los archivos relacionados al **lexer** y **parser** de antlr4.
   
2.  
    `cd lib`

    `javac YAPL*.java`
   * Generacion de clases en java.
3. `grun YAPL program -gui ../test/nombredelarchivo.cl`
   * Para generar la interfaz grafica con el arbol de parseo.
  
4. `grun YAPL program ../test/nombredelarchivo.cl`
   * Probar sin interfaz grafica 
  
5. `grun YAPL program -tree ../test/nombredelarchivo.cl`
   * Generar arbol en consola

## Con python
1. `antlr -Dlanguage=Python3 -o YAPL -visitor YAPL.g4`
   * Generar en python

2. `python main.py`
   * Correr main