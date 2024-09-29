FROM python:3.9

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV STREAMLIT_WATCH_FILE=false
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
