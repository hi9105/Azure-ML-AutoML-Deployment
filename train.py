from sklearn.ensemble import RandomForestClassifier
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error, confusion_matrix
import joblib
from sklearn.model_selection import train_test_split
from azureml.core import Dataset, Run

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_estimators', type=int, default=100)
    parser.add_argument('--min_samples_leaf', type=int, default=1)
    parser.add_argument('--max_features', default='auto')
    parser.add_argument('--oob_score', type=bool, default='True')
    parser.add_argument("--input-data", type=str)

    args = parser.parse_args()

    run = Run.get_context()

    #run.log("Number of trees in the forest : ", np.int(args.n_estimator))
    #run.log("Minimum number of samples required to be at a leaf node : ", np.int(args.min_samples_leaf))
    #run.log("Number of features to consider when looking for the best split : ", np.int(args.max_features))
    #run.log("Whether to use out-of-bag samples to estimate the generalization score : ", np.bool(args.oob_score))
    
    ws = run.experiment.workspace
    # get the input dataset by ID
    dataset = Dataset.get_by_id(ws, id=args.input_data)
	#dataset = Dataset.get_by_name(ws, name='heart_failure_clinical_records')
    
    # load the TabularDataset to pandas DataFrame
    df = dataset.to_pandas_dataframe()
    y_df = df.pop("DEATH_EVENT")

    # Split data into train and test sets.
    x_train, x_test, y_train, y_test = train_test_split(df, y_df, test_size=0.1, random_state=42)
    
    # training
    model = RandomForestClassifier(n_estimators=args.n_estimators, min_samples_leaf=args.min_samples_leaf, max_features=args.max_features, oob_score=args.oob_score).fit(x_train, y_train)
    #model_predictions = model.predict(x_test)
    
    # model accuracy
    accuracy = model.score(x_test, y_test)
    print('Accuracy on test set: {:.2f}'.format(accuracy))
    
    # metric logged by the training script.
    run.log("accuracy", np.float(accuracy))
    
    # creating a confusion matrix
    #cm = confusion_matrix(y_test, model_predictions)
    #print(cm)
    
    # files saved in the "output" folder are automatically uploaded into run history
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/HyperDriveModel.pkl')

if __name__ == '__main__':
    main()