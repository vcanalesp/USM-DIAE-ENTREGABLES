import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el CSV
df = pd.read_csv('ventas_productos.csv')

# Calcular el precio total por producto
df['precio_total'] = df['cantidad'] * df['precio']

# Crear un gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df['producto'], df['precio_total'], color='skyblue')
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')

# Guardar el gráfico como una imagen PNG
plt.savefig('grafico_precio_total.png')
plt.show()