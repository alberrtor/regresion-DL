import streamlit as st
import pandas as pd
import tensorflow as tf
import joblib

# Cargar el modelo entrenado
model = tf.keras.models.load_model('house_price_model.h5')

# Cargar el encoder y el scaler
encoder = joblib.load('encoder.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Predicción de Precios de Casas")

# Subir un archivo CSV con los datos de las casas
uploaded_file = st.file_uploader("Sube un archivo CSV con los datos de las propiedades", type=["csv"])

if uploaded_file is not None:
    # Leer los datos subidos
    input_data = pd.read_csv(uploaded_file)
    
    # Verificar si las columnas 'street' y 'country' existen antes de eliminarlas
    columns_to_drop = ['street', 'country']
    input_data = input_data.drop(columns=[col for col in columns_to_drop if col in input_data.columns])

    # Codificar y normalizar los datos
    categorical_cols = ['city', 'statezip']
    encoded_cats = pd.DataFrame(encoder.transform(input_data[categorical_cols]), columns=encoder.get_feature_names_out(categorical_cols))
    
    numerical_cols = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 
                      'condition', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated']
    scaled_nums = pd.DataFrame(scaler.transform(input_data[numerical_cols]), columns=numerical_cols)
    
    # Concatenar los datos codificados y normalizados
    processed_data = pd.concat([scaled_nums, encoded_cats], axis=1)
    
    # Generar predicciones
    predictions = model.predict(processed_data)
    
    # Mostrar las predicciones
    st.write("Predicciones de precios:")
    st.write(pd.DataFrame(predictions, columns=['PredictedPrice']))
