import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Hari, Mr.Harish",
            "Dani, Ms. Dani Daniels",
            "Shivan, Mr. Theepori",
        ],
        "Age": [19, 22, 35],
        "Sex": ["Male", "Female", "Male"],
    }
)

# print(df)
# print(df["Age"])
ages = pd.Series([20,35,58], name="Age")
# print(ages)
# print(df["Age"].max())
# print(ages.max())
print(df.describe())