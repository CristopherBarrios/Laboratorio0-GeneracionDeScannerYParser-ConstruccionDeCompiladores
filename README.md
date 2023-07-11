# Laboratorio0-GeneracionDeScannerYParser-ConstruccionDeCompiladores

<h1 align="center">
<br>
  <img src="https://mk0tuzolorusfnc7thxk.kinstacdn.com/wp-content/uploads/2016/02/antlr-logo.png" alt="MVC" width="440" height="160">
<br>

</h1>
<hr />

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