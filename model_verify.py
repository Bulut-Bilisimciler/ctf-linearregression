import os
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score
import json
import requests
import subprocess


def main():

    # Search for Pickle extensioned files in the home directory
    for file_name in os.listdir("/home"):
        if file_name.endswith('.pkl'):
            # Found the model file
            model_file_path = os.path.join("/home", file_name)
            # print(f"Found model file: {model_file_path}")

            # Load the model
            with open(model_file_path, 'rb') as f:
                model = pickle.load(f)

            # Load the test dataset
            test_df = pd.read_csv('maintest.csv')
            test_df.dropna(inplace=True)

            # Extract the target values
            y_true = test_df['target'].values

            # Extract the feature values
            X_test = test_df.drop('target', axis=1).values

            # Make predictions using the model
            y_pred = model.predict(X_test)

            # Calculate the performance metrics
            # mse = mean_squared_error(y_true, y_pred)
            # mae = mean_absolute_error(y_true, y_pred)
            r2 = r2_score(y_true, y_pred)
            # accuracy = np.sqrt(mean_squared_error(y_true, y_pred))

            # Print the results
            # print(f"Mean squared error: {mse}")
            # print(f"Mean absolute error: {mae}")
            print(f"R-squared: {r2}")
            # print(f"Accuracy: {accuracy}")

            # Log message to inform user that calculations are complete
            print("Model evaluation complete.")

    if (r2>0.5):
        return 0
    else:        
        return 1

if __name__ == "__main__":
    main()
