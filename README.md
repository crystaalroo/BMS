# BMS

La actividad II de la Materia de inteligencia Artificial tiene como objetivo, identificar sobre un grafo cuales son los nodos que te podrían sugerir una ruta buena para lograr llegar a una casilla de destino. Ademas de conservar información valiosa con respecto a que tan bueno es incluir una casilla en una ruta.
Para esto se uso un sistema de premios y castigos, de tal manera que la ruta del entrenamiento se premia si esta es mejor que la media entre el valor de la ruta maxima y el valor de la ruta minima que han sido calculados hasta ese momento.
Una vez que se tiene el premio o castigo de la ruta, es necesario sumarle este valor a todos los miembros de la misma.
