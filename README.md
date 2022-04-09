# Azure Machine Learning - Heart Failure Prediction

Cardiovascular disease are the number one cause of the death around the world, taking an estimation of around 20 million lives each year, which accounts for around 45% of all deaths worldwide. Somehow, most of the cardiovascular disease could be prevented by addressing behavioral risk factors to population-wide strategies. This project is aiming to utilize Azure Machine Learning to detect the most crucial features to predict the heart failure event.

## Dataset

### Overview
*TODO*: Explain about the data you are using.

The dataset can be downloaded from Kaggle : https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.
Suppose a bank has to approve a small loan amount for a customer and the bank needs to make a decision quickly. The bank checks the person’s credit history and their financial condition and finds that they haven’t re-paid the older loan yet. Hence, the bank rejects the application.

### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

Algorithm name
MaxAbsScaler, LogisticRegression

Hyperparameters : 

Data transformation:
{
    "class_name": "MaxAbsScaler",
    "module": "sklearn.preprocessing",
    "param_args": [],
    "param_kwargs": {},
    "prepared_kwargs": {},
    "spec_class": "preproc"
}

Training algorithm: :
{
    "class_name": "LogisticRegression",
    "module": "sklearn.linear_model",
    "param_args": [],
    "param_kwargs": {
        "C": 1.7575106248547894,
        "class_weight": null,
        "multi_class": "multinomial",
        "penalty": "l2",
        "solver": "lbfgs"
    },
    "prepared_kwargs": {},
    "spec_class": "sklearn"
}

Accuracy
0.85333

In the following image, we can see the `RunDetails` widget.

![Automl_RunDetails](screenshot/Automl_RunDetails.JPG)

In the following image, we can see the best model trained with it's parameters.

![Automl_Best_Model_Details_Run_Id](screenshot/Automl_Best_Model_Details_Run_Id.JPG)

## Hyperparameter Tuning

Model chosen for this experiment : `RandomForestClassifier`. It combines the output of multiple (randomly created) Decision Trees to generate the final output. It leverages the power of multiple decision trees. It does not rely on the feature importance given by a single decision tree.

An overview of the types of parameters used for the hyperparameter search :

- n_estimatorsint : The number of trees in the forest.
- min_samples_leaf : The minimum number of samples required to be at a leaf node.
- max_features : The number of features to consider when looking for the best split.
- oob_score : Whether to use out-of-bag samples to estimate the generalization score.

Parameters ranges used for the hyperparameter search :

- `--n_estimators`: range(10, 500).
- `--min_samples_leaf`: range(10, 500).
- `--max_features`: sqrt, log2.
- `--oob_score`: True, False.

### Results

Maximum accuracy : 76.7 %

Best parameters of the model : 

- n_estimators : 295.
- min_samples_leaf : 31.
- max_features : sqrt.
- oob_score : False.

Improvements : 

- may be more parameters could have been used so that it may increase accuracy.
- may be the parameters range could be increased or decreased or extend so that it may increase accuracy.

In the following image, we can see the `RunDetails` widget.

![HyperDrive_RunDetails](screenshot/HyperDrive_RunDetails.JPG)

In the following image, we can see the `Best model` trained with it's parameters.

![HyperDrive_Best_Model](screenshot/HyperDrive_Best_Model.JPG)

In the following image, we can see that the `HyperDrive` experiment has been completed.

![HyperDrive_Experiment_Completed](screenshot/HyperDrive_Experiment_Completed.JPG)

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording

https://youtu.be/upywb52hH5E

*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
