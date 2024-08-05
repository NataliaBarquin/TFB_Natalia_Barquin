# TFB_Natalia_Barquin
--------------------------------------

### Medical Query Category Classifier

This project utilizes natural language processing (NLP) techniques to classify medical queries into categories based on user questions. The solution includes machine learning models trained to facilitate more efficient responses to queries.
The used data is available [here].(https://github.com/abachaa/LiveQA_MedicalTask_TREC2017/tree/master)


Project Structure

The project is organized as follows:

-    data/: Contains the data needed for training and evaluating the model.
    -    dataset.csv: Data used to train the model.
    -    test_data.csv: Data for testing and evaluation.

-    notebooks/: Jupyter Notebooks for data analysis, model training, and evaluation.
    -    analysis.ipynb: Initial data exploration and analysis.
    -    classification.ipynb: Training and evaluation of the classification model.
    -    generative_model.ipynb: Preliminary test of a generative model. Under review.

-    src/: Contains the .py file for reading XML files.

-    web/: Code for deploying the web application.
    -    docker-compose.yml:
    -    label_encoder.pkl: File for encoding the response variable.
    -    tokenizer.pkl: File for tokenizing the text.
    -    main.py: Main file.
    -    my_classifier.py: File containing the function for classifying the category and inverting the encoder.
    -    my_generator.py: File containing the function to return the response to the user.