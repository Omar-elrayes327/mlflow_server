import mlflow
import mlflow.tensorflow
import tensorflow as tf
from pathlib import Path
import os


# ======================
# MLflow Config
# ======================

MLFLOW_URI = os.getenv(
    "MLFLOW_URI",
    "https://YOUR-MLFLOW-URL.up.railway.app"
)

mlflow.set_tracking_uri(MLFLOW_URI)

mlflow.set_experiment(
    "skin_cancer_experiment_v2"
)


# ======================
# Model Path
# ======================

model_path = Path(
    "../models/UNet_model.keras"
)


if not model_path.exists():
    raise FileNotFoundError(
        f"Model not found: {model_path}"
    )


model = tf.keras.models.load_model(
    model_path,
    compile=False
)


# ======================
# Register
# ======================

with mlflow.start_run():

    mlflow.tensorflow.log_model(
        model=model,
        name="model"
    )


    mlflow.register_model(
        f"runs:/{mlflow.active_run().info.run_id}/model",
        "skin_cancer_segmenter"
    )


print("Segmenter registered successfully")
