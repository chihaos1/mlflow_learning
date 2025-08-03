import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")

client = MlflowClient()

client.create_registered_model(
    name="linear-regression-model",
    tags={
        "framework": "sklearn",
        "model": "ElasticNet"
    },
    description="Elastic Net model trained on red wine quality dataset"
)

