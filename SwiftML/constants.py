try:
    from SwiftML.utils import path_converter
except ModuleNotFoundError:
    from utils import path_converter
    

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

LOGO_URL = "assets/banner.png" if ModuleNotFoundError else path_converter("assets/banner.png")
# LOGO_URL = "assets/banner.png"

PAGE_ICON = r"SwiftML\assets\img\logo-sq.png"

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

if __name__=="__main__":
    print(ART)