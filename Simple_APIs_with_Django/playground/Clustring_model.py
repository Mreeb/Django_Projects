import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.compose import ColumnTransformer
import numpy as np


def find_optimal_clusters(df, clus):
    silhouette_scores = []

    for k in range(2, clus + 1):
        kmeans_model = KMeans(n_clusters=k, random_state=42)
        kmeans_labels = kmeans_model.fit_predict(df)
        silhouette_scores.append(silhouette_score(df, kmeans_labels))

    return silhouette_scores


def clustrng(file_path, max_clusters=5):
    data = pd.read_csv(file_path)
    df = data.drop(columns="Class", axis=1)

    numeric_features = df.select_dtypes(include=['float64', 'int64']).columns
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_features = df.select_dtypes(include=['object']).columns
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    processed_data = preprocessor.fit_transform(df)

    silhouette_scores = find_optimal_clusters(processed_data, max_clusters)

    optimal_num_clusters = np.argmax(silhouette_scores) + 2  # Adding 2 to get the actual number of clusters

    kmeans_model = KMeans(n_clusters=optimal_num_clusters, random_state=42)
    kmeans_labels = kmeans_model.fit_predict(processed_data)

    silhouette_kmeans = silhouette_score(processed_data, kmeans_labels)

    df['Cluster_Labels_KMeans'] = kmeans_labels
    return optimal_num_clusters, round(silhouette_kmeans, 3),kmeans_labels, df


if __name__ == "__main__":
    clusters, Score,labels, df = clustrng(file_path="apples_and_oranges.csv", max_clusters=10)
    print(df.head())

