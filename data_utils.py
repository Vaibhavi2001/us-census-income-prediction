import pandas as pd

def load_dataset(file_path):
    #Load Dataset from the CSV file
    return pd.read_csv(file_path)

def clean_dataset(df):
    #Handle missing Values
    return df.fillna(0)

def split_features_target(df, target_column):
    #Split features adn target
    x = df.drop(target_column, axis=1)
    y = df[targert_column]
    return x, y
    
    