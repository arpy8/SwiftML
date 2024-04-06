import pickle

path = "models/dumped_LogisticRegression.pkl"
model = pickle.load(open(path, "rb"))

params = model.get_params()

for param, values in params.items():
    print(param + ":", values)