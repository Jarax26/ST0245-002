import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely import wkt
import networkx as nx

# Recoge los datos del area
area = pd.read_csv('poligono_de_medellin.csv', sep=';')
area['geometry'] = area['geometry'].apply(wkt.loads)
area = gpd.GeoDataFrame(area)

# Recoge los datos de las calles con su riesgo de acoso
edges = pd.read_csv('calles_de_medellin_con_acoso.csv', sep=';')
listaCalles = nx.from_pandas_edgelist(edges, source='origin', target='destination', edge_attr='length')
edges['geometry'] = edges['geometry'].apply(wkt.loads)
edges = gpd.GeoDataFrame(edges)

# Dibuja y guarda el mapa de Medellín con su riesgo de acoso
fig, ax = plt.subplots(figsize=(12, 8))

area.plot(ax=ax, facecolor='black')

edges.plot(ax=ax, linewidth=0.3, column='harassmentRisk', legend=True, missing_kwds={'color': 'dimgray'})

plt.title("Riesgo de acoso en las calles de Medellín")
plt.tight_layout()
plt.savefig("mapa-riesgo-de-acoso.png")

# Dibuja y guarda el mapa de Medellín con la longitud de sus calles
fig, ax = plt.subplots(figsize=(12, 8))

area.plot(ax=ax, facecolor='black')

edges.plot(ax=ax, linewidth=0.3, column='length', legend=True, missing_kwds={'color': 'dimgray'})

plt.title("Longitud en metros de las calles de Medellín")
plt.tight_layout()
plt.savefig("mapa-de-called-con-longitud.png")

# Implementación con dijkstra para encontrar la ruta más corta

a = input('Ingrese la coordenada del origen >>> ')
b = input('Ingrese la coordenada del destino >>> ')
shortest_route = nx.dijkstra_path(listaCalles, source=a, target=b, weight='length')
print(shortest_route)
