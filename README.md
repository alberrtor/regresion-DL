# Predicción de Precios de Casas usando Deep Learning

Este proyecto predice los precios de casas utilizando un modelo de Deep Learning. Los datos de entrada provienen del dataset de Kaggle ["USA House Prices"](https://www.kaggle.com/datasets/fratzcan/usa-house-prices). El proyecto se ha dockerizado para su fácil despliegue.

### Instalación y ejecución en local.
1. Descargar el dataset de kaggle "USA Housing Dataset.csv"" dentro del directorio del proyecto
3. Instalar python 3.9
4. Crear el entorno virtual de Python
    ```sh
    python3.9 -m venv venv
    ```
4. Activar el entorno virtual de Python
    ```sh
    source venv/bin/activate
    ```
5. Instalar las dependencias
    ```sh
    pip install -r requirements.txt
    ```
6. Instalar Jupyter Notebook
    ```sh
    pip install notebook
    ```
7. Abrir jupyter
    ```sh
    jupyter notebook
    ```
8. Ejecutar los 3 Notebooks en orden.
9. Generar la imagen de docker
    ```sh
    docker build -t regresion-dl-image .  
    ```
10. Crear el contenedor de docker
    ```sh
    docker run -p 8501:8501 regresion-dl-image
    ```
11. Abrir la aplicación en chrome y cargar el archivo "new_house_data.csv" para predecir los precios de las casas que se encuentran dentro del archivo.

    [http://localhost:8501](http://localhost:8501)


### Crear la imagen directamente de Docker Hub.
```sh
docker run -p 8501:8501 alberrtor/regresion-dl-image:latest
```

