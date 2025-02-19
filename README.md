# sports-performance-analytics
Análisis de datos biométricos de entrenamientos usando datos de smartwatch. Exploramos la relación entre calorías quemadas, frecuencia cardíaca y carga de entrenamiento con Python, Pandas y Seaborn. Incluye limpieza de datos, visualización y correlaciones clave para optimizar el rendimiento deportivo.

# 📊 Análisis y Visualización de Datos Biométricos de Entrenamiento con Python y Smartwatch Data  

## 📌 Resumen del Proyecto  
Este proyecto analiza datos de rendimiento físico recopilados desde un **smartwatch**, utilizando **Python, Pandas, Matplotlib y Seaborn** para la limpieza, exploración y visualización de datos. Se investigan patrones de entrenamiento, la relación entre la **frecuencia cardíaca** y las **calorías quemadas**, y se optimiza la interpretación de los datos para la toma de decisiones en entrenamientos.  

## 📌 Entendimiento del Negocio  
### 🎯 **Problema a Resolver**  
Muchos deportistas y entrenadores dependen de dispositivos **wearables** como smartwatches para medir su desempeño. Sin embargo, estos datos no siempre son intuitivos ni fáciles de interpretar. El objetivo es:  
- **Identificar patrones** en la quema de calorías y carga de entrenamiento.  
- **Determinar si existe una relación entre frecuencia cardíaca y calorías quemadas** en distintos tipos de ejercicios.  
- **Optimizar la toma de decisiones en el entrenamiento** con datos reales.  

## 📌 Comprensión de los Datos  
El dataset utilizado proviene de un **smartwatch**, con registros de sesiones de entrenamiento, calorías quemadas, duración de la sesión, frecuencia cardíaca promedio, y carga de entrenamiento.  
📌 **Estructura de los datos:**  
- **Uid, Sid** → Identificadores de usuario y sesión.  
- **Key, Category** → Tipo de ejercicio realizado (fuerza, calentamiento, etc.).  
- **Time, UpdateTime** → Fechas en formato Unix (convertidas a datetime).  
- **Value** → Datos JSON con métricas como:  
  - `calories`: Calorías quemadas.  
  - `avg_hrm`: Frecuencia cardíaca promedio.  
  - `train_load`: Carga de entrenamiento.  
  - `duration`: Duración de la sesión.  

📊 **Exploración de Datos Inicial**  
- **Conversión de fechas a formato legible.**  
- **Eliminación de columnas con más del 90% de datos faltantes.**  
- **Imputación de valores nulos en métricas clave.**  

## 📌 Modelización y Evaluación  
Se realizaron distintos análisis exploratorios para entender mejor la relación entre variables:  
✔ **Histogramas** de distribución de calorías y frecuencia cardíaca.  
✔ **Mapas de calor de correlaciones** entre calorías, bpm, carga de entrenamiento y duración.  
✔ **Comparaciones por tipo de entrenamiento** (fuerza vs. calentamiento).  
✔ **Filtrado de datos no representativos** (sesiones con menos de 50 calorías).  

## 📌 Conclusión  
📌 **Hallazgos clave:**  
🔹 Las sesiones de mayor duración muestran un incremento significativo en calorías quemadas.  
🔹 La frecuencia cardíaca no siempre tiene una correlación fuerte con la quema de calorías, lo que sugiere que otros factores influyen en la quema de energía.  
🔹 Los entrenamientos de **fuerza y resistencia** presentan variaciones significativas en bpm y calorías en comparación con calentamientos.  

🎯 **Próximos Pasos:**  
✔ Implementar un **dashboard interactivo** con Streamlit/Tableau para visualizar en tiempo real el rendimiento físico.  
✔ Incorporar modelos de **predicción de carga de entrenamiento** con Machine Learning.  
✔ Comparar estos datos con benchmarks de fitness y rendimiento.  

---

## 🚀 **Cómo Ejecutar este Proyecto**  
```bash
# Clonar este repositorio
git clone https://github.com/Alexis-Gerez/sports-performance-analytics.git

# Instalar dependencias necesarias
pip install -r requirements.txt

# Ejecutar el análisis de datos
python python app.py
