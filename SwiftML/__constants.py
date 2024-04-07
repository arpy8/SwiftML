try:
    from SwiftML.__utils import path_convertor
except ModuleNotFoundError:
    from __utils import path_convertor
    

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

LOGO_URL = "assets/banner.png" if ModuleNotFoundError else path_convertor("assets/banner.png")
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
Profile report generated successfully for the given dataset successfully at 

##### **{report_path}**

---

#### About Profile Reports

A profile report is a concise document summarizing key information about an individual, group, or entity. It typically includes details such as background, demographics, interests, accomplishments, and other relevant data. Profile reports are commonly used in various fields such as journalism, marketing, and research to provide a comprehensive overview for decision-making purposes. They aim to offer insights into the subject's characteristics, preferences, and behaviors, aiding in understanding and engaging with them effectively.

<br>
"""

if __name__ == "__main__":
    import streamlit as st
    st.write(YDATA_PROFILE_REPORT_TEXT.format(report_path="test"), unsafe_allow_html=True)
    st.caption("Generated with the help of")
    st.image("https://assets.ydata.ai/oss/ydata-profiling_red.png", width=70, )