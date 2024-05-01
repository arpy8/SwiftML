LOGO_URL = "assets/banner.png"
PAGE_ICON = "assets/img/logo-sq.png"
BACKGROUND = "assets/img/bg.png"

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

MODEL_NAME_INFO = {
    "RandomForestClassifier": ["A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. Trees in the forest use the best split strategy, i.e. equivalent to passing splitter='best' to the underlying DecisionTreeRegressor. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.", 
                               "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html"],
    "ExtraTreesClassifier": ["An extra-trees classifier is a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.", 
                             "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html"],
    "KNeighborsRegressor": ["KNN regression predicts using nearest neighbors, lacking distribution assumptions. Linear regression assumes a linear relationship and estimates coefficients through OLS. KNN is non-parametric and computationally demanding due to distance computations. Linear regression, parametric and interpretable, requires data to adhere to assumptions like homoscedasticity. KNN is suitable for non-linear data, but choosing K is critical. Linear regression's efficiency and interpretability make it favorable for large datasets with linear relationships, provided assumptions are met.", 
                             "https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html"],
    "ExtraTreesRegressor": ["An extra-trees regressor is a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.",
                            "https://scikit-l   earn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html"]
}

MODEL_DETAILS_TEMPLATE = """
##### **Best model:** 
#### {model_name}

###### **Parameters:** <br>
```
{final_model}
```

##### **Description:** <br>
{model_definition}

For more details, check out the following link: <br>
{model_info_link}
"""