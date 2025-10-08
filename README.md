# 🧠 Análisis de Sesgos en el Sistema COMPAS

## 📘 Introducción

Este repositorio contiene los materiales del **Trabajo Final de Máster (TFM)** titulado **“Análisis de Sesgos en el Sistema COMPAS”**, cuyo objetivo es evaluar los **sesgos presentes por raza, edad y género** en el sistema de evaluación de riesgo de reincidencia penal **COMPAS**, desarrollar un **modelo predictivo alternativo menos sesgado** y construir un **dashboard** para **monitorizar métricas éticas** y de rendimiento de forma continua.

---

## ⚖️ ¿Qué es COMPAS?

**COMPAS (Correctional Offender Management Profiling for Alternative Sanctions)** es un sistema utilizado en el ámbito judicial de Estados Unidos para estimar la probabilidad de reincidencia de personas acusadas o condenadas.  
El TFM analiza los **sesgos algorítmicos** que pueden surgir en su funcionamiento —principalmente por **raza**, **edad** y **género**— y propone un enfoque alternativo más **transparente y auditable**, acompañado de un dashboard para **visualizar y seguir métricas de equidad**.

---

## 📁 Estructura del repositorio

```text
├── .github/
│   └── workflows/                     
├── dashboards/
│   ├── dashboards_evaluacion_comparacion_compas.pdf  
│   ├── readme_dashboards             
│   └── dashboards_compas_logistica_link.txt  
├── data/
│   ├── raw_propublica/              
│   │   ├── compas_scores_raw.csv     
│   │   └── compas-scores-two-years.csv  
│   ├── processed/                     
│   │   ├── compas_twoyears.csv        
│   │   └── metricas_looker_v2.csv     
├── docs/                              
│   └── MEMORIA DEL PROYECTO.pdf       
├── lib/                               
│   └── lib_propias.py                 
├── notebooks/                         
│   ├── 1_eda_sesgos_twoyears_propublica.ipynb
│   ├── 2_evaluacion_y_regresion_logisitca.ipynb
│   ├── 3_analisis_controversia_propublica.ipynb
│   └── lib_propias.py                 
├── README.md                          
├── environment.yml                    
└── requirements_tfm.txt               

```

---

## ⚙️ Cómo reproducir el entorno

### 1️⃣ Clonado del repositorio
```bash
git clone <URL_DEL_REPO>
cd TFM_Compas
git checkout release/defensa
```

### 2️⃣ Instalación del entorno

**Opción A – pip/venv**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements_tfm.txt
```

**Opción B – Conda**
```bash
conda env create -f environment.yml
conda activate tfm-compas
```

### 3️⃣ Colocar los datos requeridos
```
data/raw_propublica/compas-scores-raw.csv
data/raw_propublica/compas-scores-two-years.csv
```

### 4️⃣ Ejecutar notebooks desde la terminal
```bash
export PYTHONPATH=$PWD:$PWD/lib   # Windows PowerShell: $env:PYTHONPATH="$PWD;$PWD\lib"
jupyter nbconvert --execute --to notebook --inplace notebooks/1_.ipynb
jupyter nbconvert --execute --to notebook --inplace notebooks/2_.ipynb
jupyter nbconvert --execute --to notebook --inplace notebooks/3_*.ipynb
```

📋 **Nota:** El repositorio incluye **integración continua (CI)** en GitHub Actions.  
Si el pipeline aparece 🟢, la ejecución es **reproducible**.  
Si falla en local, revisa los **logs de Actions** para identificar dependencias o rutas incorrectas.

---

## 📊 Dashboard (Streamlit)

El dashboard utiliza los archivos generados en:
```
export_dashboard/metricas_globales.csv
export_dashboard/metricas_por_grupo.csv
```

Para lanzarlo:

```bash
pip install -r requirements_tfm.txt
export PYTHONPATH=$PWD:$PWD/lib
streamlit run dashboard/app.py
```

---

## 🧩 Tecnologías utilizadas

- **Python**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `scikit-learn`, `scipy`, `statsmodels`  
- **Auxiliares**: `missingno`, `fuzzywuzzy` (+ `python-Levenshtein`), `pyyaml`, `python-dotenv`, `openpyxl`, `pyarrow`  
- **Jupyter Notebook**  
- **Streamlit**  
- **Git & GitHub + GitHub Actions** (CI con Python 3.12.9)

---

## 🏷️ Versionado de la entrega

- **Tag principal:** `v1.0-defensa` *(o el más reciente)*  
- **Rama de referencia:** `release/defensa`

---

## 🛠️ Troubleshooting

| Error | Posible causa | Solución |
|-------|----------------|-----------|
| `FileNotFoundError` | Falta un CSV en `data/raw_propublica/` | Verifica la ubicación de los archivos originales |
| `ModuleNotFoundError` | Falta una librería | Ejecuta `pip install -r requirements_tfm.txt` |
| `ImportError` en `lib_propias.py` | No se reconoce la ruta local | Exporta `PYTHONPATH` como se indica arriba |

---

## 👥 Autores

- **Azahara Bravo**  
- **Daniel Álvarez**  
- **María Loza**

📚 *TFM – Máster en Data Analytics – Nuclio Digital School*

---

## ⚖️ Licencia

Repositorio con fines académicos. **Prohibido el uso comercial sin autorización.**
