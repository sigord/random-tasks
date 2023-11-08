FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

# model alredy in the image
# COPY ["model1.bin", "dv.bin", "predict_service_q4.py", "./"]
COPY ["predict_service_q6.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict_service_q6:app"]