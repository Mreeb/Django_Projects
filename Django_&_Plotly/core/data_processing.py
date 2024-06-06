import pandas as pd


def load_csv(file):
    df = pd.read_csv(file)
    return df


def select_columns(df, column1, column2):
    selected_data = df[[column1, column2]]
    return selected_data
