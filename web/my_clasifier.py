
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences



def category_clasification(model, tokenizer, label_encoder, summary, question):



    sequences_query = tokenizer.texts_to_sequences(np.array([summary + " "  + question ], dtype=str))
    X_query = pad_sequences(sequences_query, maxlen=100)

    prediction = model.predict(X_query)
    index_of_max = np.argmax(prediction)
    unencoded_prediction = label_encoder.inverse_transform(np.array([index_of_max]))[0]

    #categories = {8:"information" }

    #return categories.get(np.array([index_of_max])[0])
    return unencoded_prediction