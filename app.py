import streamlit as st
import pandas as pd
import requests

# URL de la API
API_URL = "https://smartgroup.pythonanywhere.com/api/stock/"

st.set_page_config(page_title="Stock", layout="wide")

st.title("📦 Stock actual")

# Obtener datos desde la API
try:
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    st.error(f"❌ Error al obtener datos: {e}")
    st.stop()

# Convertir a DataFrame
df = pd.DataFrame(data)

# Opcional: ordenar por nombre de producto
df = df.sort_values("producto")

# Filtro de búsqueda por nombre
busqueda = st.text_input("🔍 Buscar producto por nombre:", "")

# Filtrar por coincidencia en nombre (sin distinción de mayúsculas)
if busqueda:
    df_filtrado = df[df["producto"].str.contains(busqueda, case=False, na=False)]
else:
    df_filtrado = df

# Mostrar resultados
st.write(f"Se encontraron {len(df_filtrado)} productos:")
st.dataframe(df_filtrado, use_container_width=True)
