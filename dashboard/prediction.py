from django.core.cache import cache
from tensorflow import keras
import numpy as np

# Used to 'set' and 'get' trained model from the cache
model_cache_key = 'model_cache'

# Get model from cache
model = cache.get(model_cache_key)

if model is None:
    # Model is not in the cache, so 'set' it
    model = keras.models.load_model('./dnn/model/dnn_cacao_ferm_classifier') # Load model
    cache.set(model_cache_key, model, None) # Save the model in cache
    # In the above line, None is the timeout parameter. It means cache forever.

def predict(data):
    preds = model.predict(data)
    return preds.astype(np.int32)