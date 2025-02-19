import streamlit as st
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

# 📌 Cargar los datos limpios
file_path = "20250214_6762854051_MiFitness_hlth_center_sport_record.csv"
df = pd.read_csv(file_path)

# Convertir las fechas a formato datetime
df["Time"] = pd.to_datetime(df["Time"], unit="s")
df["UpdateTime"] = pd.to_datetime(df["UpdateTime"], unit="s")

# Extraer valores JSON de la columna 'Value'
def extract_json_values(row):
    try:
        json_data = json.loads(row)
        return pd.Series({
            "calorias": json_data.get("calories", None),
            "frecuencia_card": json_data.get("avg_hrm", None),
            "carga_entrenamiento": json_data.get("train_load", None),
            "duracion": json_data.get("duration", None)
        })
    except:
        return pd.Series({
            "calorias": None,
            "frecuencia_card": None,
            "carga_entrenamiento": None,
            "duracion": None
        })

# Aplicar extracción de datos
df_extracted = df["Value"].apply(extract_json_values)
df = pd.concat([df, df_extracted], axis=1)

# Eliminar columna original de valores JSON
df.drop(columns=["Value"], inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# 📌 Traducir todas las categorías de entrenamiento
traducciones = {
    "strength_training": "Entrenamiento de Fuerza",
    "weight_lifting": "Levantamiento de Pesas",
    "barbell_training": "Entrenamiento con Barra",
    "rope_skipping": "Saltar la Cuerda",
    "free_training": "Entrenamiento Libre",
    "sit_ups": "Abdominales",
    "spinning": "Spinning",
    "outdoor_hiking": "Senderismo al Aire Libre",
    "walking": "Caminata"
}

df["Categoria_Entrenamiento"] = df["Category"].map(traducciones).fillna("Otro")


# 🎨 Configuración de la Interfaz
st.set_page_config(page_title="📊 Análisis de Rendimiento Deportivo", layout="wide")

# 📌 Título del Dashboard
st.title("📊 Análisis de Rendimiento Deportivo con Smartwatch")

# 🔍 Filtros Interactivos
st.sidebar.header("🎛 **Filtros de Análisis**")
selected_type = st.sidebar.multiselect("📌 Selecciona el tipo de entrenamiento:", df["Categoria_Entrenamiento"].unique())
selected_calories = st.sidebar.slider("🔥 Filtrar por calorías quemadas:", 
                                      int(df["calorias"].min()), int(df["calorias"].max()), (50, int(df["calorias"].max())))

# 📌 Aplicar los filtros
df_filtered = df.copy()
if selected_type:
    df_filtered = df_filtered[df_filtered["Categoria_Entrenamiento"].isin(selected_type)]

df_filtered = df_filtered[(df_filtered["calorias"] >= selected_calories[0]) & (df_filtered["calorias"] <= selected_calories[1])]

# 🎯 Visualización 1: Distribución de Calorías
st.subheader("🔥 Distribución de Calorías Quemadas")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df_filtered["calorias"], bins=20, kde=True, color="blue", ax=ax)
st.pyplot(fig)

# 🎯 Visualización 2: Relación entre Frecuencia Cardíaca y Calorías
st.subheader("❤️ Relación entre Frecuencia Cardíaca y Calorías Quemadas")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df_filtered, x="frecuencia_card", y="calorias", hue="Categoria_Entrenamiento", palette="coolwarm", ax=ax)
st.pyplot(fig)

# 🎯 Visualización 3: Comparación entre Tipos de Entrenamiento
st.subheader("📌 Comparación de Calorías Quemadas por Tipo de Entrenamiento")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df_filtered, x="Categoria_Entrenamiento", y="calorias", palette="coolwarm", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# 🎯 Visualización 4: Matriz de Correlaciones
st.subheader("📊 Relación entre Variables del Entrenamiento")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df_filtered[["calorias", "frecuencia_card", "carga_entrenamiento", "duracion"]].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig)

st.sidebar.markdown("📌 **Creado por Alexis Gerez**")
