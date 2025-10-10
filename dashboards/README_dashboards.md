# Dashboards del Proyecto TFM — Análisis de Sesgos en COMPAS

Este documento describe los dos dashboards integrados en un único archivo de Looker Studio.  
Ambos fueron diseñados para ofrecer una **visualización clara, comparativa y comprensible** del comportamiento del sistema COMPAS y del modelo alternativo de **regresión logística**, en relación con la reincidencia penal.

---

## 🧩 1. Dashboard — *Análisis de Sesgos en COMPAS*

Este dashboard fue diseñado con el objetivo de ofrecer una **visión integral, visual y comprensible** de cómo el algoritmo COMPAS asigna puntuaciones de riesgo y cómo estas se relacionan con la reincidencia real observada.

Se construyó en **Looker Studio** a partir del dataset `compas_twoyears.csv` (métricas globales).  
La estructura se organizó en **tres paneles**, siguiendo la lógica del análisis de datos:

### 📊 Estructura general
1. **Panel superior:** filtros interactivos (género, etnia, rango_edad) y tarjetas de KPIs globales:  
   - Número de casos  
   - Puntuación media COMPAS  
   - Reincidencia real  
   - Accuracy  
   - Precision  
   - Recall  
   - FNR  
   - FPR  

2. **Panel central:** relación entre riesgo y reincidencia real.  
   - Gráfica *scatter* “Riesgo Medio vs Reincidencia Real”: muestra por etnia la correlación entre el riesgo medio asignado y la reincidencia real.  
   - El tamaño de las burbujas refleja el peso relativo de cada grupo.  
   - Permite observar sobreestimaciones o subestimaciones del algoritmo respecto a la realidad.

3. **Panel inferior:** distribución de riesgo por grupo.  
   - *Boxplot* de puntuaciones COMPAS por etnia.  
   - Barras apiladas que representan reincidencia/no reincidencia por nivel de riesgo.

### 🎨 Diseño visual
- Paleta coherente: **azules** (valores neutros o reales) y **corales** (errores o sobreestimaciones).  
- Fondo blanco y jerarquía clara.  
- Logotipo de *ProPublica* incorporado como referencia a la fuente original.

---

## ⚖️ 2. Dashboard — *Evaluación de Modelos: COMPAS vs Regresión Logística*

Este dashboard fue diseñado con el objetivo de **comparar el rendimiento y la equidad** entre el algoritmo original COMPAS y el modelo de **regresión logística** desarrollado como alternativa.

Se construyó en **Looker Studio** utilizando una única fuente de datos:  
`metricas_looker_v2.csv` — el archivo principal que consolida las métricas necesarias para la comparación.

### 📂 Fuente de datos principal
El archivo `metricas_looker_v2.csv` constituye la **base de datos principal** del dashboard comparativo.  
Este CSV se generó a partir de los resultados obtenidos en los notebooks de análisis, tras calcular las métricas globales de desempeño para ambos modelos:

- **Accuracy**
- **Precision**
- **Recall**
- **F1**
- **Tasa de falsos positivos (FPR)**

Cada fila del archivo representa una **combinación única de modelo y grupo demográfico**, lo que permite visualizar las diferencias de rendimiento entre COMPAS y la regresión logística según variables protegidas como raza o género.  

El archivo se diseñó con un **formato tabular simple** para facilitar su lectura y conexión directa con Looker Studio.  
Desde esta fuente, se construyeron las **tablas dinámicas**, **tarjetas de indicadores** y **gráficos comparativos** que conforman el dashboard.  
De este modo, el CSV actúa como nexo entre el **análisis cuantitativo en Python** y la **visualización interactiva** del proyecto.

---

### 📊 Estructura del dashboard
El dashboard se organiza en torno a tres ejes: **rendimiento global**, **métricas por grupo** y **análisis visual de equidad**.

1. **Encabezado:**  
   Filtros interactivos para personalizar el análisis:  
   - **Modelo:** COMPAS o Regresión Logística  
   - **Métrica:** Accuracy, Precision, Recall, F1, FPR  
   - **Grupo:** raza, género o rango de edad  

2. **Panel superior:**  
   Tarjetas *scorecards* con los valores globales de desempeño de ambos modelos.  
   Permiten comparar rápidamente la efectividad general.

3. **Panel central:**  
   Gráfico de barras comparativo que muestra los resultados porcentuales de cada métrica según el grupo y el modelo seleccionado.  
   Facilita la lectura de diferencias en desempeño y sesgos.

4. **Panel inferior:**  
   Tabla dinámica con mapa de calor que muestra las métricas numéricas por grupo.  
   - Verde = valores altos (mejor rendimiento).  
   - Rojo = valores bajos (peor rendimiento).  
   - En la **tasa de falsos positivos (FPR)** los colores están **invertidos**: verde indica valor bajo.

---

### 🎨 Diseño visual
- **Rojo:** COMPAS (modelo original y sesgado).  
- **Verde:** Regresión Logística (modelo alternativo y más equilibrado).  
- Fondo blanco y diseño limpio para favorecer la comparación directa.

---

## 🧠 Conclusión
Ambos dashboards permiten analizar de forma visual los **patrones de sesgo, desempeño y equidad** del sistema COMPAS frente a un modelo alternativo transparente.  
El enfoque modular y los filtros interactivos facilitan la exploración y la comunicación de resultados a públicos no técnicos.

---

## 🔗 Enlace público
📎 [Abrir dashboards en Looker Studio](https://lookerstudio.google.com/u/0/reporting/2d19f8b3-8325-450c-8fdd-f06a1ab07dec/page/p_rs4hi4mywd)



---
