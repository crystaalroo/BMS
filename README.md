# BMF

La actividad II de la Materia de inteligencia Artificial tiene como objetivo, identificar sobre un grafo cuales son los nodos que te podrían sugerir una ruta buena para lograr llegar a una casilla de destino. Ademas de conservar información valiosa con respecto a que tan bueno es incluir una casilla en una ruta.
Es decir, a la ponderacion de cada valor se suma la diferencia entre la media y la ruta actual.
Para esto se uso un sistema de premios y castigos, de tal manera que la ruta del entrenamiento se premia si esta es mejor que la media entre el valor de la ruta maxima y el valor de la ruta minima que han sido calculados hasta ese momento.
Una vez que se tiene el premio o castigo de la ruta, es necesario sumarle este valor a todos los miembros de la misma.

# VIDEO DE PRUEBA!!!
-> -> -> https://www.youtube.com/watch?v=wV3fjBZ8x1o <- <- <-

## MAXIMO?

Si bien la actividad establece que el MAX_INT/2 debe ser tomado como inicialización para la matriz ponderada, el trabajar con un entero tan grande, hace que no sea posible aplicar un dijkstra, por lo tanto, definí un nuevo maximo
3*400*8=9600
Ese es un entero que es muy imposible alcanzar, ya que implicaria pasar 8 veces por cada 1 de las 400 casillas y que todas presenten el maximo esfuerzo para cada uno de los atletas. Lo cual no es posible, ya que el problem establece que todos tienen ponderaciones diferentes. Y por lo menos el 20% de la matriz no se puede recorrer, ya que para este caso, hay bombas.

**Recomendación: 30 entrenamientos por deportista


## COMO USAR EL PROGRAMA

Una vez que inicias:
1. Selecciona el porcentaje de bombas 
2. Selecciona el porcentaje de zona de agua. (El porcentaje es respecto a los especios disponibles)
3. Selecciona el porcentaje de zonas montañosas. (El porcentaje es respecto a los especios disponibles)
4. Selecciona el porcentaje de barrancos. (El porcentaje es respecto a los especios disponibles)
5. Elige la posicion de inicio. Será marcada con un lindo shibita
6. Elige la posicion de destino. Será marcada con una medalla
7. Espera a que se complete el entrenamiento.
  -Puedes marcar o desmarcar la casilla de mostrar entrenamiento.
 8. Puedes comenzar a seleccionar posiciones para obtener la mejor ruta.
 
 
## Cosas por mencionar...

Para desarrollar la actividad, realice 20 iteraciones del entrenamiento por cada personaje. 
Cada iteración se realizaba usando un vector de visitados, una pila para controlar el acceso a posiciones marcadas como visitadas y use la matriz con ponderaciones para sobre escribir los datos.
Para realizar la busqueda a cualquier punto en base al entrenamiento aplique dijkstra para cada uno de los deportistas. De esa manera solo llamó a una funcion para imprimir el camino minimo desde ese punto, lo cual se hace checando el padre de cada uno de los nodos.


