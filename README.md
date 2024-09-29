# Predicción de Precios de Casas usando Deep Learning

Este proyecto predice los precios de casas utilizando un modelo de Deep Learning. Los datos de entrada provienen del dataset de Kaggle ["House Prices - Advanced Regression Techniques"](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques). El proyecto se ha dockerizado para su fácil despliegue y automatización usando GitHub Actions.

## Estructura del Proyecto

- **Feature Pipeline**: Procesa los datos crudos y genera características para el modelo.
- **Training Pipeline**: Entrena un modelo de Deep Learning con las características generadas.
- **Batch Inference Pipeline**: Usa el modelo entrenado para generar predicciones por lotes.
- **Streamlit App**: Permite a los usuarios cargar datos y obtener predicciones de precios de casas en tiempo real.

## Requisitos



#################
Se realizarán 1 proyecto de ML/DL:
Proyecto de regresión con Deep Learning, con los siguientes criterios
•	Deep learning (pronóstico/regresión para palabras o series de tiempo).
•	Puntos extra si se crean contenedores para cada modelo y se suben a dockerhub. Puntos extra si se tiene una app completa en ploomber o streamlit o chainlit (LLM).

Cada proyecto debe incluir los 3 notebooks o scripts que se usan tomando en cuenta el post de Pau Labarta: https://www.linkedin.com/posts/pau-labarta-bajo-4432074b_machinelearning-mlops-realworldml-activity-7137003082403442688-sD8x/
Cada proyecto debe tener documentación en un readme, también incluir un requeriments.txt (donde están las bibliotecas indispensables). Tener un repo en github por cada proyecto.
Pueden usar chatGPT.
Puntos extra si se crean contenedores para cada modelo y se suben a dockerhub. Puntos extra si se tiene una app completa en ploomber o streamlit o chainlit (LLM).
