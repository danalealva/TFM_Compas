# 🧠 Análisis de Sesgos en el Sistema COMPAS — TFM

## 📘 Introducción

Este repositorio contiene los materiales del Trabajo Final de Máster (TFM) titulado **“Análisis de Sesgos en el Sistema COMPAS”**, cuyo objetivo es:

- Evaluar los sesgos presentes por raza, edad y género en el sistema de evaluación de riesgo de reincidencia penal COMPAS.  
- Desarrollar un modelo predictivo alternativo menos sesgado (regresión logística explicable y auditada).  
- Construir un dashboard para monitorizar métricas éticas y de rendimiento de forma continua.

---

## ⚖️ ¿Qué es COMPAS?

COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) es un sistema utilizado en el ámbito judicial de Estados Unidos para estimar la probabilidad de reincidencia de personas acusadas o condenadas.  
El TFM analiza los sesgos algorítmicos que pueden surgir en su funcionamiento —principalmente por raza, edad y género— y propone un enfoque alternativo más transparente y auditable.

---

## 📁 Estructura del repositorio

```
├── .github/
│   └── workflows/                     # Automatizaciones de integración continua (CI)
├── dashboards/                        # Materiales del dashboard (exportación, enlaces, explicación)
│   ├── dashboards_evaluacion_comparacion_compas.pdf  
│   ├── readme_dashboards             
│   └── dashboards_compas_logistica_link.txt  
├── data/
│   ├── raw_propublica/                # Datos originales sin procesar
│   │   ├── compas_scores_raw.csv     
│   │   └── compas-scores-two-years.csv  
│   ├── processed/                     # Datos limpios, transformados y métricas finales
│   │   ├── compas_twoyears.csv        
│   │   └── metricas_looker_v2.csv      # Métricas consolidadas usadas en el dashboard
├── docs/                              # Documentación final del proyecto
│   └── MEMORIA DEL PROYECTO.pdf       # Versión definitiva de la memoria del TFM
├── lib/                               # Funciones propias y utilidades reutilizables
│   └── lib_propias.py                 
├── notebooks/                         # Notebooks del análisis y modelado
│   ├── 1_eda_sesgos_twoyears_propublica.ipynb
│   ├── 2_evaluacion_y_regresion_logisitca.ipynb
│   ├── 3_analisis_controversia_propublica.ipynb
│   └── lib_propias.py                 
├── README.md                          # Este documento
├── environment.yml                    # Entorno Conda (opcional)
└── requirements_tfm.txt               # Dependencias Pip del proyecto
```

---

## ⚙️ Cómo reproducir el entorno

### 1️⃣ Clonado del repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
git checkout release/defensa
```

### 2️⃣ Instalación del entorno

#### Opción A — pip / venv
```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements_tfm.txt
```

#### Opción B — Conda
```bash
conda env create -f environment.yml
conda activate <nombre_entorno>
```

### 3️⃣ Colocar los datos requeridos
Asegúrese de que los siguientes archivos estén disponibles en `data/raw_propublica/`:
- `compas_scores_raw.csv`  
- `compas-scores-two-years.csv`

### 4️⃣ Ejecutar los notebooks
```bash
export PYTHONPATH=$PWD:$PWD/lib      # Windows PowerShell: $env:PYTHONPATH="$PWD;$PWD\lib"
jupyter nbconvert --execute --inplace --to notebook notebooks/1_eda_sesgos_twoyears_propublica.ipynb
jupyter nbconvert --execute --inplace --to notebook notebooks/2_evaluacion_y_regresion_logisitca.ipynb
jupyter nbconvert --execute --inplace --to notebook notebooks/3_analisis_controversia_propublica.ipynb
```

---

## 📊 Dashboard / Visualización
El dashboard comparativo fue realizado en **Looker Studio**, usando como fuente principal de datos el archivo:  
**`data/processed/metricas_looker_v2.csv`**, que consolida métricas globales y segmentadas por grupo demográfico para ambos modelos (COMPAS vs regresión logística).

En la carpeta `dashboards/` se incluye una guía de uso (`readme_dashboards`) y un enlace al panel en línea (`dashboards_compas_logistica_link.txt`). También se proporciona una exportación en PDF (`dashboards_evaluacion_comparacion_compas.pdf`) para una revisión estática.

---

## 🧩 Tecnologías utilizadas

- **Lenguaje**: Python  
- **Bibliotecas de análisis y modelado**: pandas, numpy, matplotlib, seaborn, plotly, scikit-learn, scipy, statsmodels  
- **Otras utilidades**: missingno, fuzzywuzzy + python-Levenshtein, pyyaml, python-dotenv, openpyxl, pyarrow  
- **Ejecución**: Jupyter Notebook  
- **Visualización**: Looker Studio  
- **Control de versiones e integración continua**: Git & GitHub, GitHub Actions (pipeline CI configurado para Python 3.x)

---

## 🛠️ Troubleshooting / Errores comunes

| Error                        | Posible causa                          | Solución                                    |
|-----------------------------|----------------------------------------|---------------------------------------------|
| `FileNotFoundError`         | Uno o más CSV faltan en la carpeta `data/raw_propublica/` | Verificar que los nombres y rutas coincidan. |
| `ModuleNotFoundError`       | Faltan librerías                       | Ejecutar `pip install -r requirements_tfm.txt` o activar conda correctamente. |
| Importación en `lib_propias.py` falla | Rutas de módulos no reconocidas     | Asegurarse de que `PYTHONPATH` esté bien configurado (como se describe arriba). |

---

## 👥 Autores

- Azahara Bravo  
- Daniel Álvarez  
- María Loza  

**TFM – Máster en Data Analytics – Nuclio Digital School**

---

## 🏷️ Versionado de la entrega

- **Tag principal de entrega:** `v1.0-defensa`  
- **Rama asociada:** `release/defensa`  
- Esta versión corresponde a la entrega final utilizada para la defensa del TFM.
---

## 🛡️ Licencia

Este repositorio se publica con fines académicos. Prohibido uso comercial sin consentimiento explícito de los autores.
démicos. **Prohibido el uso comercial sin autorización.**
