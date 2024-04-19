import pkg_resources

    
def path_convertor(filename):
    return pkg_resources.resource_filename('SwiftML', f'{filename}')


PORT = 825
ART = r"""

_____/\\\\\\\\\\\_____________________________________/\\\\\__________________/\\\\____________/\\\\___/\\\_____________        
 ___/\\\/////////\\\_________________________________/\\\///__________________\/\\\\\\________/\\\\\\__\/\\\_____________       
  __\//\\\______\///_______________________/\\\______/\\\___________/\\\_______\/\\\//\\\____/\\\//\\\__\/\\\_____________      
   ___\////\\\___________/\\____/\\___/\\__\///____/\\\\\\\\\_____/\\\\\\\\\\\__\/\\\\///\\\/\\\/_\/\\\__\/\\\_____________     
    ______\////\\\_______\/\\\__/\\\\_/\\\___/\\\__\////\\\//_____\////\\\////___\/\\\__\///\\\/___\/\\\__\/\\\_____________    
     _________\////\\\____\//\\\/\\\\\/\\\___\/\\\_____\/\\\__________\/\\\_______\/\\\____\///_____\/\\\__\/\\\_____________   
      __/\\\______\//\\\____\//\\\\\/\\\\\____\/\\\_____\/\\\__________\/\\\_/\\___\/\\\_____________\/\\\__\/\\\_____________  
       _\///\\\\\\\\\\\/______\//\\\\//\\\_____\/\\\_____\/\\\__________\//\\\\\____\/\\\_____________\/\\\__\/\\\\\\\\\\\\\\\_ 
        ___\///////////_________\///__\///______\///______\///____________\/////_____\///______________\///___\///////////////__
                                                                  
"""

LOGO_URL = path_convertor("assets/banner.png")
PAGE_ICON = r"SwiftML\assets\img\logo-sq.png"

TEAM_MEMBERS = [
    {"name": "Arpit Sengar", "role": "Developer", "links":["https://www.linkedin.com/in/arpitsengar", "https://github.com/arpy8"]},
    {"name": "Aditya Bhardwaj", "role": "Developer", "links":["https://www.linkedin.com/in/aditya-bhardwaj-3a6437232/", "https://github.com/adityabhardwajjj"]},
    {"name": "Harshit Jain", "role": "Developer", "links":["https://www.linkedin.com/in/harshitjainnn/", "https://github.com/HarshitJainn"]},
    {"name": "Anushka Singh", "role": "Developer", "links":["https://www.linkedin.com/in/harshitjainnn/", "https://github.com/HarshitJainn"]},
    {"name": "Vijeta Srivastava", "role": "Developer", "links":["https://www.linkedin.com/in/vijeta-shrivastava-a8962a244/", ""]},
]


EXCLUDED_MODELS = ['lightgbm', 'catboost', 'xgboost']
MODELS_DICT = {
    ## regressors
    "LinearRegression":"lr",
    "Lasso":"lasso",
    "Ridge":"ridge",
    "ElasticNet":"en",
    "Lars":"lar",
    "LassoLars":"llar",
    "OrthogonalMatchingPursuit":"omp",
    "BayesianRidge":"br",
    "AutomaticRelevanceDetermination":"ard",
    "PassiveAggressiveRegressor":"par",
    "RandomSampleConsensus":"ransac",
    "TheilSenRegressor":"tr",
    "HuberRegressor":"huber",
    "KernelRidge":"kr",
    "SupportVectorRegressor":"svm",
    "KNeighborsRegressor":"knn",
    "DecisionTreeRegressor":"dt",
    "RandomForestRegressor":"rf",
    "ExtraTreesRegressor":"et",
    "AdaBoostRegressor":"ada",
    "GradientBoostingRegressor":"gbr",
    "MLPRegressor":"mlp",
    "DummyRegressor":"dr",
    
    ## classifiers
    "LogisticRegression":"lr",
    "KNeighborsClassifier":"knn",
    "NaiveBayes":"nb",
    "DecisionTreeClassifier":"dt",
    "SVMLinearKernel":"svm",
    "SVMRadialKernel":"rbfsvm",
    "GaussianProcessClassifier":"gpc",
    "MLPClassifier":"mlp",
    "RidgeClassifier":"ridge",
    "RandomForestClassifier":"rf",
    "QuadraticDiscriminantAnalysis":"qda",
    "AdaBoostClassifier":"ada",
    "GradientBoostingClassifier":"gbc",
    "LinearDiscriminantAnalysis":"lda",
    "ExtraTreesClassifier":"et",
    
    # exclusions    
    "ExtremeGradientBoosting":"xgboost",
    "LGBMRegressor":"lightgbm",
    "CatBoostRegressor":"catboost",
}

BACKGROUND = r"SwiftML\assets\img\bg.png"

GEMINI_INSTRUCTIONS = """
I am going to pass you a string. Your job is to write a single line pandas script to perform the task mentioned in the string. You can only use the pandas library. You have 2 minutes to complete the task.

"""

YDATA_PROFILE_REPORT_TEXT = """
Profile report generated successfully for the given dataset.

---

#### About Profile Reports

A profile report is a concise document summarizing key information about an individual, group, or entity. It typically includes details such as background, demographics, interests, accomplishments, and other relevant data. Profile reports are commonly used in various fields such as journalism, marketing, and research to provide a comprehensive overview for decision-making purposes. They aim to offer insights into the subject's characteristics, preferences, and behaviors, aiding in understanding and engaging with them effectively.

<br>
"""


README_TEXT_CONTENT = """Model ID: {sha256_string}
PARAMS: {params}


Your model has been successfully trained and saved. Below are the details of the files generated:

1. .pkl file - This pickle file is the serialized version of the model you trained using SwiftML.
You can use this pickle file to load your model in the future. Make sure to keep this file safe and secure.
2. predict.py - Contains a simple script showing how to predict values from the .pkl file.
3. profile-report.html - Contains the profile report of the dataset you used to train the model.
4. api/ - this folder contains the necessary files to run the FastAPI server for making predictions.


For any queries, mail me at arpitsengar99@gmail.com
"""

PREDICTION_SCRIPT = """
import pickle 
import pandas as pd

X_test = {values}
pickle_path = r"{model_path}"

with open(pickle_path, 'rb') as file:
    params, model = pickle.load(file)
    
try:
    # data = pd.DataFrame(X_test, columns=params)
    print(model.predict({values}))
    
except AssertionError and ValueError:
    print("Please check the input data")
"""

ENCODING_IMPORTANT = """
### Important Note

We've detected that your dataset contains categorical columns, it's advisable to convert these columns into numerical values before making predictions. One way to achieve this is by using the `pandas.get_dummies` method, which performs one hot encoding.

Here's an example of how to do this:

```python
import pandas as pd

# Example DataFrame
data = {'Color': ['Red', 'Green', 'Blue', 'Red']}
df = pd.DataFrame(data)

# Perform one hot encoding
one_hot_encoded = pd.get_dummies(df['Color'], prefix='Color')

# Concatenate the one hot encoded columns with the original DataFrame
df_encoded = pd.concat([df, one_hot_encoded], axis=1)

print(df_encoded)
```

This will produce the following output:

```
   Color  Color_Blue  Color_Green  Color_Red
0    Red           0            0          1
1  Green           0            1          0
2   Blue           1            0          0
3    Red           0            0          1
```

By converting categorical columns to numerical values, you prepare your dataset for predictive modeling and ensure compatibility with machine learning algorithms.


For any queries, mail me at arpitsengar99@gmail.com

SwiftML
"""

MODEL_NAME_INFO = {
    "RandomForestClassifier": ["A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. Trees in the forest use the best split strategy, i.e. equivalent to passing splitter='best' to the underlying DecisionTreeRegressor. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.", 
                               "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html"],
    "ExtraTreesClassifier": ["An extra-trees classifier is a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.", 
                             "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html"]
}


PREDICT_FASTAPI_SCRIPT = """import pickle
import uvicorn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

class Predict(BaseModel):
    model_id: str
    values: list

pickle_path = '{model_path}'

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to the SwiftML API!"

@app.post("/predict")
async def predict(values: Predict):
    
    with open(pickle_path, 'rb') as file:
        params, model = pickle.load(file)
    
    values = values.values
    data = pd.DataFrame([values], columns=params)
    
    prediction = model.predict(data)
    prediction = prediction.tolist()    
    
    return {result_dict}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
"""

API_REQUIREMENTS = """fastapi==0.110.1
uvicorn==0.29.0
pydantic==2.6.4
"""

API_README = """This folder contains the necessary files to run the FastAPI server for making predictions using the model you trained with SwiftML.
To make predictions, follow the steps below:
1. Install the required packages by running the following command:
2. Run the FastAPI server by executing the following command:
3. Make a POST request to the '/predict' endpoint with the following JSON payload:
4. The server will return the prediction made by the model.

Make sure to pass the correct values in the JSON payload to get accurate predictions.
Convert the categorical columns in the dataset to numerical values before making predictions.


For any queries, mail me at arpitsengar99@gmail.com

Thanks for using SwiftML!
"""