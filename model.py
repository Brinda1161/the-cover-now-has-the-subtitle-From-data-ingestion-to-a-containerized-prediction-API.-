import os
MODEL_DIR = "models"
TEST_DIR = os.path.join("models", "test")

def get_dir(test=False):
    d = TEST_DIR if test else MODEL_DIR
    os.makedirs(d, exist_ok=True)
    return d

def model_train(df, test=False):
    # ... fit model ...
    path = os.path.join(get_dir(test), f"model-{MODEL_VERSION}.joblib")
    joblib.dump(model, path)
