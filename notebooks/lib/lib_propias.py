# Esta es mi librería de funciones del módulo 4
# Autor: Lara Palacios

# ÍNDICE

## - Exploración inicial
### 1. check_df(): Exploración inicial de datos
## - Limpieza de datos
### 2. id_valores_problem(): Identificación de valores problemáticos (nulos, duplicados y outliers)
### 3. procesar_fecha(): Proceso y estandarización del formato de fechas
### 4. select_outliers(): Selección de outliers
### 5. imputar(): Imputación de nulos u outliers mediante la media, mediana y random
## - EDA
### 6. realizar_crosstab()
### 7. graficar_boxplot_px()
### 8. graficar_boxplot_bivariable_px()
### 9. graficar_histograma_px()
### 10. graficar_histograma_bivariable_px()
### 11. graficar_barras_px()
### 12. graficar_pie_chart()
### 13. graficar_correlacion()
### 14. realizar_correlaciones()
### 15. graficar_proporciones()
## - Segmentación de clientes
### 16. segmentacion_RFM()
## - AB testing
### 17. lift_df()
### 18. calcular_t_student()
### 19. evaluar_p_valor()

# Manipulación y análisis de datos
import pandas as pd
import numpy as np
# Visualización de datos
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
# Nulos
import missingno as msno
# Expresiones regulares
import re
#from fuzzywuzzy import process
# Fechas
from datetime import datetime

# FUNCIONES

## - Exploración inicial
### 1. check_df(): Exploración inicial de datos

def check_df(df, tipo=''):
    if tipo == 'simple':
        print("¿Cuántas filas y columnas hay en el conjunto de datos?")
        num_filas, num_columnas = df.shape
  
        print("\tHay {:,} filas y {:,} columnas.".format(num_filas, num_columnas))

        print("¿Cuáles son las primeras dos filas del conjunto de datos?")
        display(df.head(2))
        print('\n########################################################################################')
    else:
        print("¿Cuántas filas y columnas hay en el conjunto de datos?")
        num_filas, num_columnas = df.shape
        print("\tHay {:,} filas y {:,} columnas.".format(num_filas, num_columnas))
        print('\n########################################################################################')

        print("¿Cuáles son las primeras cinco filas del conjunto de datos?")
        display(df.head())
        print('\n########################################################################################')

        print("¿Cuáles son las últimas cinco filas del conjunto de datos?")
        display(df.tail())
        print('\n########################################################################################')

        print("¿Cómo puedes obtener una muestra aleatoria de filas del conjunto de datos?")
        display(df.sample(n = 5))
        print('\n########################################################################################')

        print("¿Cuáles son las columnas del conjunto de datos? ¿Cuál es el tipo de datos de cada columna?")
        print(df.dtypes)
        print('\n########################################################################################')

        print("¿Cuántas columnas hay de cada tipo de datos?")
        print(df.dtypes.value_counts())
        print('\n########################################################################################')

        print("¿Cuáles son las variables numéricas?")
        df_numericas = df.select_dtypes(include = 'number')
        columnas_numericas = list(df_numericas.columns)
        print(columnas_numericas)
        print('\n########################################################################################')

        print("¿Cuáles son las variables categóricas?")
        df_categoricas = df.select_dtypes(include = 'object')
        columnas_categoricas = list(df_categoricas.columns)
        print(columnas_categoricas)
        print('\n########################################################################################')

        print("¿Cuántos valores únicos tiene cada columna?")
        print(df.nunique())
        print('\n########################################################################################')

        if len(columnas_numericas)>0:
            print("¿Cuáles son las estadísticas descriptivas básicas de las columnas numéricas?")
            display(df.describe(include = 'number'))
            print('\n########################################################################################')

        if len(columnas_categoricas)>0:
            print("¿Cuáles son las estadísticas descriptivas básicas de las columnas categóricas?")
            display(df.describe(include = 'object'))


## - Limpieza de datos
### 2. id_valores_problem(): Identificación de valores problemáticos (nulos, duplicados y outliers)

def id_valores_problem(df, columnas=[]):
    print('###################################################################################')
    print('3.1.1. Proporción de NULOS en cada una de las columnas del conjunto de datos:')
    print(round((df.isnull().sum()/len(df))*100, 2).sort_values(ascending= False))
    print('###################################################################################')
    print(f'3.1.2. Número de DUPLICADOS totales: {df.duplicated().sum()}')
    print('###################################################################################')
    if len(columnas) > 0:
        print(f'3.1.2. Número de DUPLICADOS parciales según las columnas {columnas}: {df.duplicated(subset=columnas).sum()}')
        print('###################################################################################')
    df_numericas = df.select_dtypes(include = 'number')
    columnas_numericas = list(df_numericas.columns)
    if len(columnas_numericas) > 0:
        print('3.1.3. Columnas numéricas con OUTLIERS')
        for var in columnas_numericas:
            Q1 = df[var].quantile(0.25)
            Q3 = df[var].quantile(0.75)
            limite_inferior = Q1 - 1.5 * (Q3 - Q1)
            limite_superior = Q3 + 1.5 * (Q3 - Q1)
            outliers = df[(df[var] < limite_inferior) | (df[var] > limite_superior)]
            print(f'Número de outliers en la columna "{var}": {outliers.shape[0]}')
        print('###################################################################################')
        

### 3. procesar_fecha(): Proceso y estandarización del formato de fechas

def procesar_fecha(fecha):
  '''
    * Separados por "-":
      - Patrón 1: 04-01-2020
      - Patrón 2: 2020-01-10
      - Patrón 3: 01-14-20

    * Separados por "/":
      - Patrón 4: 11/01/2020
      - Patrón 5: 02/03/20
  '''

  # Separador '-'
  # %d-%m-%y'
  patron1 = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{2})$'
  # dia: (0[1-9]|[12][0-9]|3[01])
  # mes: (0[1-9]|1[0-2])
  # año: (\d{2})
  #'%d-%m-%Y'
  patron2 = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$'
  #'%m-%d-%y'
  patron3 = r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{2})$'
  #'%m-%d-%Y'
  patron4 = r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$'
  #'%Y-%m-%d'
  patron5 = r'^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
  
  # Separador '/'
  #'%d/%m/%y'
  patron6 = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})$'
  #'%m/%d/%y'
  patron7 = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{2})$'
  #'%m/%d/%Y'
  patron8 = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})$'
  #'%Y/%m/%d'
  patron9 = r'^(\d{4})/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$'
  #'%Y/%m/%d'
  patron10 = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})$'
  # 12/5/2021
  #'%Y/%m/%d'
  patron11 = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/(\d{4})$'
  
  # Comprueba si la fecha cumple con el patrón
  if pd.notnull(fecha) and re.fullmatch(patron1, fecha):
    # Parsea la fecha al formato deseado y devuelve en formato "aaaa-mm-dd"
    return pd.to_datetime(fecha, format='%d-%m-%y').strftime('%Y-%m-%d')
  elif pd.notnull(fecha) and re.fullmatch(patron2, fecha):
    return pd.to_datetime(fecha, format='%d-%m-%Y').strftime('%Y-%m-%d')
  elif pd.notnull(fecha) and re.fullmatch(patron3, fecha):
    return pd.to_datetime(fecha, format='%m-%d-%y').strftime('%Y-%m-%d')
  elif pd.notnull(fecha) and re.fullmatch(patron4, fecha):
    return pd.to_datetime(fecha, format='%m-%d-%Y').strftime('%Y-%m-%d')
  elif pd.notnull(fecha) and re.fullmatch(patron5, fecha):
    return pd.to_datetime(fecha, format='%Y-%m-%d').strftime('%Y-%m-%d')
  elif pd.notnull(fecha) and re.fullmatch(patron6, fecha):
    return pd.to_datetime(fecha, format='%d/%m/%y').strftime('%Y-%m-%d')
  elif pd.notnull(fecha) and re.fullmatch(patron7, fecha):
      return pd.to_datetime(fecha, format='%m/%d/%y').strftime('%Y-%m-%d')
  elif pd.notnull(fecha) and re.fullmatch(patron8, fecha):
      return pd.to_datetime(fecha, format='%m/%d/%Y').strftime('%Y-%m-%d')
  elif pd.notnull(fecha) and re.fullmatch(patron9, fecha):
      return pd.to_datetime(fecha, format='%Y/%m/%d').strftime('%Y-%m-%d')
  elif pd.notnull(fecha) and re.fullmatch(patron10, fecha):
      return pd.to_datetime(fecha, format='%d/%m/%Y').strftime('%Y-%m-%d')
  # 12/5/2021
  elif pd.notnull(fecha) and re.fullmatch(patron11, fecha):
      return pd.to_datetime(fecha, format='%m/%d/%Y').strftime('%Y-%m-%d')
  else:
      # Devuelve la fecha original si no cumple con el patrón o es NaN
      return pd.NaT  # Retorna Not a Time para fechas que no coinciden con ningún formato
  

### 4. select_outliers(): Selección de outliers

def deteccion_outliers (df, variable):
    # Suponiendo que tienes un DataFrame df y quieres analizar la columna 'columna_de_interes'
    columna = df[variable]

    sns.boxplot(data=df, y=variable)
    plt.show()

    Q1 = columna.quantile(0.25)
    Q3 = columna.quantile(0.75)
    IQR = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    print(f"Los valores atípicos se definen como aquellos que caen fuera del siguiente rango:")
    print(f"\t - Límite inferior (considerado extremadamente bajo): {limite_inferior:.2f}")
    print(f"\t - Límite superior (considerado extremadamente alto): {limite_superior:.2f}")

    outilers = list(columna[((columna < limite_inferior) | (columna > limite_superior))].index)
    num_outliers = len(outilers)
    print(f"Hay {num_outliers} outliers en la variable '{variable}'")
    return outilers


### 5. imputar(): Imputación de nulos u outliers mediante la media, mediana y random

def imputar (df, variable):
    # media
    media = df[variable].mean()
    df[variable + '_media'] = df[variable].fillna(media)

    # mediana
    mediana = df[variable].median()
    df[variable + '_mediana'] = df[variable].fillna(mediana)

    # random
    valores_no_nulos = df[variable].dropna().values
    df[variable + '_random'] = df[variable].apply(lambda x: np.random.choice(valores_no_nulos) if pd.isna(x) else x)
    return df, [variable, variable + '_media', variable + '_mediana', variable + '_random']


## - EDA
### 6. realizar_crosstab()

def realizar_crosstab(df, variable_1, variable_2, normalize):
    # Crear una tabla de contingencia con conteos absolutos
    aux_p1 = pd.crosstab(df[variable_1], df[variable_2], margins=True)

    # Crear una tabla de contingencia con porcentajes
    aux_p2 = (pd.crosstab(df[variable_1], df[variable_2], normalize=normalize, margins=True) * 100).round(2)

    # Concatenar ambas tablas para tener conteos y porcentajes en una sola tabla
    tabla_contingencia = pd.concat([aux_p1, aux_p2], axis=1)

    return tabla_contingencia


### 7. graficar_boxplot_px()

def graficar_boxplot_px(df, variable_analisis):
    # Crear el boxplot usando Plotly Express
    fig = px.box(df, y=variable_analisis)

    # Actualizar títulos del gráfico
    fig.update_layout(title=f'Boxplot: {variable_analisis}', yaxis_title='Frecuencia')

    # Actualizar el fondo del gráfico a blanco
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',
        'xaxis': {'showgrid': True, 'gridcolor': 'lightgrey'},
        'yaxis': {'showgrid': True, 'gridcolor': 'lightgrey'}
    })

    # Mostrar el gráfico
    fig.show()


### 8. graficar_boxplot_bivariable_px()

def graficar_boxplot_bivariable_px (df, variable_analisis, variable_categorica):
    # Crear el boxplot usando Plotly Express
    fig = px.box(df, x=variable_categorica, y=variable_analisis, color=variable_categorica)

    # Actualizar títulos del gráfico
    fig.update_layout(title=f'Boxplot de {variable_analisis} por {variable_categorica}',
                      xaxis_title=variable_categorica,
                      yaxis_title=variable_analisis)

    # Actualizar el fondo del gráfico a blanco
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',
        'xaxis': {'showgrid': True, 'gridcolor': 'lightgrey'},
        'yaxis': {'showgrid': True, 'gridcolor': 'lightgrey'}
    })

    # Mostrar el gráfico
    fig.show()


### 9. graficar_histograma_px()

def graficar_histograma_px (df, variable_analisis):
    fig = px.histogram(df, x=variable_analisis, nbins=20,
                       title=f'Distribución de: {variable_analisis}')

    # Calcular media y mediana
    mean_val = df[variable_analisis].mean()
    median_val = df[variable_analisis].median()

    # Añadir línea vertical para la media
    fig.add_vline(x=mean_val, line_dash="dash", line_color="red",
                  annotation_text=f"Media: {mean_val:.2f}", annotation_position="top right")

    # Añadir línea vertical para la mediana
    fig.add_vline(x=median_val, line_dash="dot", line_color="green",
                  annotation_text=f"Mediana: {median_val:.2f}", annotation_position="top left")

    fig.update_layout(xaxis_title=variable_analisis, yaxis_title='Frecuencia')
    fig.show()


### 10. graficar_histograma_bivariable_px()

def graficar_histograma_bivariable_px (df, variable_analisis, variable_categorica=None, bins=20, show_mean_median=True):
    # Crear el histograma con la opción de segmentar por variable categórica
    if variable_categorica:
        fig = px.histogram(df, x=variable_analisis, color=variable_categorica, nbins=bins,
                           title=f'Distribución de {variable_analisis} por {variable_categorica}')
    else:
        fig = px.histogram(df, x=variable_analisis, nbins=bins,
                           title=f'Distribución de: {variable_analisis}')

    # Opcional: Calcular y mostrar líneas de media y mediana
    if show_mean_median:
        mean_val = df[variable_analisis].mean()
        median_val = df[variable_analisis].median()

        # Añadir línea vertical para la media
        fig.add_vline(x=mean_val, line_dash="dash", line_color="red",
                      annotation_text=f"Media: {mean_val:.2f}", annotation_position="top right")

        # Añadir línea vertical para la mediana
        fig.add_vline(x=median_val, line_dash="dot", line_color="green",
                      annotation_text=f"Mediana: {median_val:.2f}", annotation_position="top left")

    # Actualizar títulos del gráfico
    fig.update_layout(xaxis_title=variable_analisis, yaxis_title='Frecuencia',
                      plot_bgcolor='rgba(255, 255, 255, 1)',
                      xaxis_showgrid=True, xaxis_gridcolor='lightgrey',
                      yaxis_showgrid=True, yaxis_gridcolor='lightgrey')

    # Mostrar el gráfico
    fig.show()


### 11. graficar_barras_px()

def graficar_barras_px (df, variable_analisis):
    # Contar la frecuencia de la variable de análisis
    volumen = df[variable_analisis].value_counts().reset_index()
    volumen.columns = [variable_analisis, 'Volúmen']

    # Crear el gráfico de barras
    fig = px.bar(volumen, x=variable_analisis, y='Volúmen', text='Volúmen')
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(title_text=f'Gráfico de barras: {variable_analisis}',
                      xaxis_title=variable_analisis,
                      yaxis_title='Volúmen',
                      xaxis={'categoryorder':'total descending'})

    # Actualizar el fondo del gráfico a blanco
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',
        'xaxis': {'showgrid': True, 'gridcolor': 'lightgrey'},
        'yaxis': {'showgrid': True, 'gridcolor': 'lightgrey'}
    })

    fig.show()


### 12. graficar_pie_chart()

def graficar_pie_chart(df, variable_analisis):
  df_ = df[variable_analisis].value_counts().reset_index()
  df_.columns = [variable_analisis,'Volúmen']

  fig = px.pie(
      df_,
      names=variable_analisis,
      values='Volúmen',
      title=variable_analisis,
      width=800,
      height=500
  )
  fig.show()


### 13. graficar_correlacion()

def graficar_correlacion(df, variable_x, variable_y):
    # Crear el gráfico de dispersión usando Plotly Express para visualizar la correlación
    fig = px.scatter(df, x=variable_x, y=variable_y,
                     trendline='ols',  # Añade una línea de regresión
                     labels={variable_x: variable_x, variable_y: variable_y},
                     title=f'Correlación entre {variable_x} y {variable_y}')

    # Actualizar el fondo del gráfico a blanco y ajustar la cuadrícula
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',
        'xaxis': {'showgrid': True, 'gridcolor': 'lightgrey'},
        'yaxis': {'showgrid': True, 'gridcolor': 'lightgrey'}
    })

    # Mostrar el gráfico
    fig.show()


### 14. realizar_correlaciones()

def realizar_correlaciones(df, listado_variables):
    sns.heatmap(df[listado_variables].corr(), annot = True)


### 15. graficar_proporciones()

def graficar_proporciones(df, variable_categorica_1, variable_categorica_2):
    # Crear el histograma con barras agrupadas por la segunda variable categórica
    fig = px.histogram(df, x=variable_categorica_1, color=variable_categorica_2,
                       title='Análisis de múltiples variables categóricas',
                       labels={variable_categorica_1: f'Categoría: {variable_categorica_1}',
                               variable_categorica_2: f'Grupo: {variable_categorica_2}'},
                       text_auto=True,
                       barmode='group')

    # Actualizar títulos del gráfico
    fig.update_layout(yaxis_title='Volúmen',
                      legend_title=variable_categorica_2,
                      bargap=0.2)

    # Actualizar el fondo del gráfico a blanco
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',
        'xaxis': {'showgrid': True, 'gridcolor': 'lightgrey'},
        'yaxis': {'showgrid': True, 'gridcolor': 'lightgrey'}
    })

    # Mostrar el gráfico
    fig.show()


## - Segmentación de clientes
### 16. segmentacion_RFM()

def calculate_rfm(dataframe, columna_id, reference_date):
  df_rfm = dataframe.groupby(columna_id).agg({
      'fecha': lambda x: (reference_date - x.max()).days,
      columna_id: 'count',
      'ventas' : 'sum'
  }).rename(columns={'fecha': 'Recencia', 'id_cliente': 'Frecuencia', 'ventas': 'Valor_monetario'})

  etiquetas = ['Bajo','Moderado','Alto','MAlto']
  etiquetas_recencia = ['MAlto', 'Alto', 'Moderado', 'Bajo']

  columnas = df_rfm.columns

  for col in columnas:
      if col == 'Recencia':
        df_rfm[col + '_cut'] = pd.qcut(df_rfm[col], q=4, labels = etiquetas_recencia)
      else:
        df_rfm[col + '_cut'] = pd.qcut(df_rfm[col], q=4, labels = etiquetas)

  df_rfm['Segmento_RFM'] = df_rfm['Recencia_cut'].astype(str) + '_' + df_rfm['Frecuencia_cut'].astype(str) + '_' + df_rfm['Valor_monetario_cut'].astype(str)

  etiquetas = [1, 2, 3, 4]
  etiquetas_recencia = [4, 3, 2, 1]

  for col in columnas:
    if col == 'Recencia':
      df_rfm[col + '_cut_num'] = pd.qcut(df_rfm[col], q=4, labels = etiquetas_recencia)
    else:
      df_rfm[col + '_cut_num'] = pd.qcut(df_rfm[col], q=4, labels = etiquetas)

  df_rfm['Segmento_RFM_num'] = df_rfm['Recencia_cut_num'].astype(int) + df_rfm['Frecuencia_cut_num'].astype(int) + df_rfm['Valor_monetario_cut_num'].astype(int)

  return df_rfm


## - AB testing
### 17. lift_df()

def lift_df(grupo_control, grupo_tratamiento):

    media_control = grupo_control.mean()
    media_treatment = grupo_tratamiento.mean()

    lift = round(((media_treatment-media_control)/media_treatment)*100, 2)

    print("- Grupo de control: {:.2f}%".format(media_control*100))
    print("- Grupo de tratamiento: {:.2f}%".format(media_treatment*100))

    if lift>0:
        print(f"El grupo de tratamiento ha mostrado un mayor nivel de impacto que el de control.")
        print(f"El tratamiento ha resultado en un rendimiento un {abs(lift)}% más que el grupo de control.")
    elif lift < 0:
        print("El grupo de tratamiento ha mostrado un menor nivel de impacto que el de control.")
        print(f"El tratamiento ha resultado en un rendimiento un {abs(lift)}% menos que el grupo de control.")
    else:
        print("No hay diferencia significativa entre el grupo de tratamiento y el de control.")


### 18. calcular_t_student()

def calcular_t_student(grupo_control, grupo_tratamiento):
    """
    Calcula el valor t de Student para dos muestras independientes.
    Retorna:
    - El valor t de Student.
    """
    media_control = grupo_control.mean()
    media_treatment = grupo_tratamiento.mean()

    std_control = grupo_control.mean()
    std_treatment = grupo_tratamiento.mean()

    var_control = grupo_control.var()
    var_treatment = grupo_tratamiento.var()

    n_control = len(grupo_control)
    n_treatment = len(grupo_tratamiento)

    numerador = media_control - media_treatment
    denominador = np.sqrt((var_control / n_control) + (var_treatment / n_treatment))
    #denominador = np.sqrt((std_control**2 / n_control) + (std_treatment**2 / n_treatment))
    t = numerador / denominador
    return t


### 19. evaluar_p_valor()

def evaluar_p_valor(p_valor, umbral = None):
  if umbral is None:
        umbral = 0.05

  print("- Hipótesis nula (H₀): No hay diferencia entre las medias de los dos grupos.")
  print("- Hipótesis alternativa (H₁): Hay una diferencia entre las medias de los dos grupos.")

  print('\n##########################################################################\n')

  print("El p valor es {:.2f}.\n".format(p_valor))

  print('\n##########################################################################\n')

  if p_valor < umbral:
      print("Se rechaza la hipótesis nula.\n")
      print("El valor p ({}) es menor que el umbral ({})".format(p_valor, umbral))
      print("Por lo tanto, la diferencia es estadísticamente significativa.")
      print("\t- Hay evidencia suficiente para afirmar que la diferencia entre los dos grupos no es simplemente aleatoria")

  else:
      print("No se rechaza la hipótesis nula.\n")
      print("El valor p ({}) es mayor o igual que el umbral ({})".format(p_valor, umbral))
      print("Por lo tanto, la diferencia no es estadísticamente significativa.")
      print("\t- Lo que observamos podría haber ocurrido solo por casualidad y no necesariamente debido a un efecto real.")
