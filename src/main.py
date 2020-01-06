import pandas as pd
import datetime
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

df_train = pd.read_csv('./assets/train.csv')
df_test = pd.read_csv('./assets/test.csv')

revenue = df_train["revenue"]
del df_train["revenue"]

df_whole = pd.concat([df_train, df_test], axis=0)
df_whole["Open Date"] = pd.to_datetime(df_whole["Open Date"])
df_whole["Year"] = df_whole["Open Date"].apply(lambda x:x.year)
df_whole["Month"] = df_whole["Open Date"].apply(lambda x:x.month)
df_whole["Day"] = df_whole["Open Date"].apply(lambda x:x.day)

le = LabelEncoder()
df_whole["City"] = le.fit_transform(df_whole["City"])
df_whole["City Group"] = df_whole["City Group"].map({"Other":0, "Big Cities":1})
df_whole["Type"] = df_whole["Type"].map({"FC":0, "IL":1, "DT":2, "MB":3})

df_train = df_whole.iloc[:df_train.shape[0]]
df_test = df_whole.iloc[df_train.shape[0]:]

df_train_columns = [col for col in df_train.columns if col not in ["Id", "Open Date"]]

rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=5,
    max_features=0.5,
    random_state=449,
    n_jobs=-1
)
rf.fit(df_train[df_train_columns], revenue)
prediction = rf.predict(df_test[df_train_columns])

submission = pd.DataFrame({"Id":df_test.Id, "Prediction":prediction})
submission.to_csv("./output/submission.csv", index=False)
