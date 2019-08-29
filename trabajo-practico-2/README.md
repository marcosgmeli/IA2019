# Trabajo Practico N2
![Tabla de resultado](https://raw.githubusercontent.com/marcosgmeli/IA2019/master/trabajo-practico-2/tabla.png)


Considere una versión modificada del entorno de la aspiradora del Ejercicio, en el que se penalice al agente con un punto en cada movimiento.
a)¿Puede un agente reactivo simple ser perfectamente racional en este medio? Explíquese.
No, porque desconoce si es más eficiente moverse buscando suciedad o quedarse quieto

b)¿Qué sucedería con un agente reactivo con estado? Diseñe este agente.
Podría tener en cuenta si ya recorrió toda la zona, por lo que podría saber cuando detenerse

c)¿Cómo se responderían las preguntas a y b si las percepciones proporcionan al agente información sobre el nivel de suciedad/limpieza de todas las cuadrículas del entorno?
Sí podría ser completamente racional porque podría evaluar que suciedad conviene ir a limpiar y cual no, y en que orden haccerlo para disminuir las penalizaciones


Considere una versión modificada del entorno de la aspiradora del Ejercicio, en el que la geografía del entorno (su extensión, límites, y obstáculos) sea desconocida,así como, la disposición inicial de la suciedad. (El agente puede ir hacia arriba, abajo, así como hacia la derecha y a la izquierda.)
a)¿Puede un agente reactivo simple ser perfectamente racional en este medio? Ex-plíquese.
No, porque no sabe cuando está chocando contra una pared, por ejemplo, ya que no sabe cuando debe doblar

b)¿Puede un agente reactivo simple con una función de agente aleatoria superar a un agente reactivo simple? Diseñe un agente de este tipo y medir su rendimientoen varios medios.
En esta versión modificada del Ejercicio, sí.

c)¿Se puede diseñar un entorno en el que el agente con la función aleatoria obtenga una actuación muy pobre? Muestre los resultados.
En un entorno muy grande, ya que el aleatorio tiende a dar vueltas por una misma zona.

d)¿Puede un agente reactivo con estado mejorar los resultados de un agente reactivo simple? Diseñe un agente de este tipo y medir su eficiencia en distintos medios. ¿Se puede diseñar un agente racional de este tipo?
Sí porque podría recorrer en espiral, y aunque no tenga nada de información del entorno, tendría mejores resultados
