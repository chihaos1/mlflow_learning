import mlflow
from mlflow import MlflowClient

mlflow.set_tracking_uri("http://127.0.0.1:5000")

client = MlflowClient()

client.delete_registered_model(
    name="ElasticNet-regression-model"
)