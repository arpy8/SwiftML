import pickle
import numpy as np
import pandas as pd

path = "models/final_dumped_HuberRegressor.pkl"
params, model = pickle.load(open(path, "rb"))


path2 = "model/HuberRegressor.pkl"
print(type(path2))
# params = model.get_params()

# for param in params:
classes = ['setosa', 'versicolor', 'virginica']
ml_list = [1, 5.1, 3.5, 1.4, 0.2]
ml = [1,3,'alfa-romero giulia','gas','std','two','convertible','rwd','front',88.6,168.8,64.1,48.8,2548,'dohc','four',130,'mpfi',3.47,2.68,9,111,5000,21,27]

# print(classes[np.argmax(model.predict(pd.DataFrame([ml_list])))])
# print(model.predict(pd.DataFrame([ml])))
temp = pd.DataFrame([ml], columns=params)

# temp.to_csv("temp.csv", index=False)
print(model.predict(params))