# miniPascal Compiler

> El nombre en realidad no significa gran cosa, excepto que, bueno, tiene la palabra PASCAL en ella y va derecho al corazón de todos los lenguajes de
programación.
El lenguaje es en gran parte derivado de Pascal y lenguajes similares. Sin embargo, se ha simplificado
enormemente para hacer la creacion del compilador un poco más fácil. Por ejemplo, no hay punteros, registros, arreglos multi-dimensionales u objetos. Del mismo modo, el lenguaje es escaso a la hora de características avanzadas. Sin embargo, usted encontrará que es un proyecto lo suficientemente difícil.

Implementacion de un compilador para el lenguaje mini-pascal para el desarrollo del curso de Compiladores de la Universidad Tecnologica de Pereira. El compilador genera un archivo .s en codigo ensamblador spark listo para ser compilado.
 
Una especificacion completa del lenguaje se encuentra en el archivo: _**"Mini Pascal.pdf"**_


## Uso:
miniPascal esta hecho para ser ejecutado bajo **Python 2.7** y no es compatible con Python 3, ademas requiere tener instaladas las librerias **'docopt'** y **'ply'**

Para usar el compilador desde la linea de comandos ejecute:

	Para realizar un analisis completo y generar codigo:
		python mpascal.py <file.pas>

	Para realizar un analisis lexico:
		python mpascal.py lex <file.pas>

	Para ver el arbol de sintaxis:
		python mpascal.py ast <file.pas>
