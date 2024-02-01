from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, cohen_kappa_score
import pandas as pd

def knn_resampling(X, y, resampling='oversampling'):
    # Drop 'Travel_Rarely' column
    X = X.drop(columns=['businesstravel', 'Travel_Rarely'])

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    if resampling == 'oversampling':
        resampler = RandomOverSampler()
    elif resampling == 'undersampling':
        resampler = RandomUnderSampler()
    else:
        raise ValueError("Invalid resampling strategy. Choose 'oversampling' or 'undersampling'.")

    X_train_resampled, y_train_resampled = resampler.fit_resample(X_train, y_train)

    # Training KNN Model
    knn_model = KNeighborsClassifier(n_neighbors=5) 
    knn_model.fit(X_train_resampled, y_train_resampled)
    
    knn_predictions_train = knn_model.predict(X_train_resampled)
    knn_predictions_test = knn_model.predict(X_test)
    
    print(f"Result after {resampling}")
    print()
    
    print("KNN Classifier - TRAIN Resampled Data:")
    print(classification_report(y_train_resampled, knn_predictions_train))
    
    print("KNN Classifier - TEST Resampled Data:")
    print(classification_report(y_test, knn_predictions_test))

    kappa_score_train = cohen_kappa_score(y_train_resampled, knn_predictions_train)
    print(f"Kappa Score in TRAIN set: {kappa_score_train:.2f}")  # Corrected closing parenthesis

