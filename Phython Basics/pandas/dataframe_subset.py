import pandas as pd

titanic = pd.read_csv("titanic.csv")
ages = titanic["Age"]
# print(ages.head())
# print(type(titanic["Age"]))
# print(titanic["Age"].shape)
# age_sex = titanic[["Age", "Sex"]]
# print(age_sex.head())
# print(type(titanic[["Age", "Sex"]]))
# print(titanic[["Age", "Sex"]].shape)
# above_35 = titanic[titanic["Age"] > 35] #to check the age above 35
# print(above_35.head())
# print(titanic["Age"] > 35)
# class_23 = titanic[titanic["Pclass"].isin([2, 3])]
# print(class_23.head())
class_30 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_30.head())