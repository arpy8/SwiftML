from unityml.utils import path_converter


PORT = 825
ART = """
88        88               88                           88b           d88  88           
88        88               ""    ,d                     888b         d888  88           
88        88                     88                     88`8b       d8'88  88           
88        88  8b,dPPYba,   88  MM88MMM  8b       d8     88 `8b     d8' 88  88           
88        88  88P'   `"8a  88    88     `8b     d8'     88  `8b   d8'  88  88           
88        88  88       88  88    88      `8b   d8'      88   `8b d8'   88  88           
Y8a.    .a8P  88       88  88    88,      `8b,d8'       88    `888'    88  88           
 `"Y8888Y"'   88       88  88    "Y888      Y88'        88     `8'     88  88888888888  
                                            d8'                                         
                                           d8'                                          
"""

LOGO_URL = path_converter("assets/banner.png")

PAGE_ICON = ""

TEAM_MEMBERS = [
    {"name": "Arpit Sengar", "role": "Developer", "links":["https://www.linkedin.com/in/arpitsengar", "https://github.com/arpy8"]},
    {"name": "Aditya Bhardwaj", "role": "Developer", "links":["https://www.linkedin.com/in/aditya-bhardwaj-3a6437232/", "https://github.com/adityabhardwajjj"]},
    {"name": "Harshit Jain", "role": "Developer", "links":["https://www.linkedin.com/in/harshitjainnn/", "https://github.com/HarshitJainn"]},
    {"name": "Anushka Singh", "role": "Developer", "links":["https://www.linkedin.com/in/harshitjainnn/", "https://github.com/HarshitJainn"]},
]

MODELS_DICT = {
    'LGBMRegressor':'lightgbm', 
    'ExtraTreesRegressor':'et',
    'RandomForestRegressor':'rt',
    'GradientBoostingRegressor':'gbr',
    'LinearRegression':'lr',
    'Ridge':'ridge',
    'Lasso':'lasso',
    'ElasticNet':'en',
    'LassoLars':'llar',
    'BayesianRidge':'br',
    'KNeighborsRegressor':'knn',
    'HuberRegressor':'huber',
    'Lars':'lar',
    'AdaBoostRegressor':'ada',
    'DecisionTreeRegressor':'dt',
    'PassiveAggressiveRegressor':'par',
    'OrthogonalMatchingPursuit':'omp',
    'DummyRegressor':'dummy',
    'CatBoostRegressor': 'catboost'
}