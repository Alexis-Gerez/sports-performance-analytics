# Importar librerías necesarias
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns


# Definir la ruta del archivo CSV (ajusta la ruta si es necesario)
file_path = r"C:\Users\Alexis\Desktop\20250214_6762854051_MiFitness_or1_data_copy\20250214_6762854051_MiFitness_hlth_center_sport_record.csv"


# Cargar el archivo CSV
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
            "calories": json_data.get("calories", None),
            "avg_hrm": json_data.get("avg_hrm", None),
            "train_load": json_data.get("train_load", None),
            "duration": json_data.get("duration", None)
        })
    except:
        return pd.Series({
            "calories": None,
            "avg_hrm": None,
            "train_load": None,
            "duration": None
        })

# Aplicar extracción de datos
df_extracted = df["Value"].apply(extract_json_values)
df = pd.concat([df, df_extracted], axis=1)

# Eliminar columna original de valores JSON
df.drop(columns=["Value"], inplace=True)

# Eliminar valores nulos
df.dropna(inplace=True)

# Eliminar duplicados
df.drop_duplicates(inplace=True)

# Mostrar primeras filas del dataset
print(df.head())

# Histogramas de distribución
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.histplot(df["calories"], bins=30, kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Distribución de Calorías Quemadas")

sns.histplot(df["avg_hrm"], bins=30, kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Distribución de Frecuencia Cardíaca Promedio")

sns.histplot(df["train_load"], bins=30, kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Distribución de Carga de Entrenamiento")

sns.histplot(df["duration"], bins=30, kde=True, ax=axes[1, 1])
axes[1, 1].set_title("Distribución de Duración de Sesiones")

plt.tight_layout()
plt.show()

# Mapa de calor de correlaciones
plt.figure(figsize=(8, 6))
sns.heatmap(df[["calories", "avg_hrm", "train_load", "duration"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlación entre Variables")
plt.show()

# Comparación de calorías por tipo de entrenamiento
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Category", y="calories")
plt.xticks(rotation=45)
plt.title("Comparación de Calorías Quemadas por Tipo de Entrenamiento")
plt.show()

# Comparación de frecuencia cardíaca por tipo de entrenamiento
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Category", y="avg_hrm")
plt.xticks(rotation=45)
plt.title("Comparación de Frecuencia Cardíaca por Tipo de Entrenamiento")
plt.show()

# Filtrar sesiones con menos de 50 calorías
df_filtered = df[df["calories"] >= 50]

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x="Time", y="calories")
plt.xticks(rotation=45)
plt.title("Tendencia de Calorías Quemadas a lo Largo del Tiempo")
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=df_filtered, x="Category", y="train_load")
plt.xticks(rotation=45)
plt.title("Comparación de Carga de Entrenamiento por Tipo de Ejercicio")
plt.show()

