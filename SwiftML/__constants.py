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

len(MODELS_DICT.keys())