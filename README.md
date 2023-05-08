# DataScienceInvestigation-1

### Descripción:
Es una investigación básica donde el objetivo de la misma es predecir el ganador del mundial de la FIFA 2022, 
teniendo en cuenta la información de todos los partidos de los mundiales hasta el 2018.

### Extracción de los datos:
La información de los partidos de los mundiales se obtuvo realizando WebScrapping a todas las páginas de Wikipedia de los mundiales, 
utilizando librerias como BeautifulSoup y Selenium, posteriormente se extrajo la información a archivos CSV.

### Limpieza de datos:
Se cargó y se analizó los DataSets para revisar que no hubiesen datos atípicos ni filas o columnas relevantes en blanco.

### Modelo:
Utilizando la libreria poisson de scipy.stats con la información ya limpia, analiza los resultados de sus partidos disputados anteriormente
y predice un futuro ganador, es un modelo predictivo básico para saber cual es el posible país ganador, que sabiendo los países ya clasificados
ordena, analiza, predice y clasifica en cada grupo(A,B,C,D,E,F,G,H) hasta encontrar los finalistas y el posible ganador del mundial de la FIFA 2022.

