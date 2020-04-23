# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr

import pandas as pd

df = pd.read_csv("/Users/kilimetr/Desktop/python/pandas/data_pandas_demo/survey_results_public.csv")
schema_df = pd.read_csv("/Users/kilimetr/Desktop/python/pandas/data_pandas_demo/survey_results_schema.csv")

print(df)
print(df.shape)
print(df.info())
# print(pd.set_option("display.max_columns", 85)) # shows all 85 columns in jupyter
print(df.head(10))
print(df.tail(10))


print(df["Hobbyist"])
print(df["Hobbyist"].value_counts())


print(df.loc[0]) # show first row
print(df.loc[[0, 1, 2], "Hobbyist"])
print(df.loc[0:2, "Hobbyist":"Employment"])


print(df.set_index("Hobbyist"))


df.set_index("Hobbyist", inplace = True)
print(df)
print(df.index)
print(df.loc["Yes"]) # df.loc["CoreyMSchafer@gmail.com", "last"]; df.loc[0] does not work but df.iloc[0] works
df.reset_index(inplace = True)
print(df)


df = pd.read_csv("/Users/kilimetr/Desktop/python/pandas/data_pandas_demo/survey_results_public.csv", index_col = "Respondent")
schema_df = pd.read_csv("/Users/kilimetr/Desktop/python/pandas/data_pandas_demo/survey_results_schema.csv", index_col = "Column")
print(df.head())
print(schema_df)
print(schema_df.loc["MgrIdiot", "QuestionText"])
print(schema_df.sort_index(ascending = False)) # sort alphabeticaly staring at the end
print(schema_df.sort_index(inplace = True)) # pernamentaly sorted alphabeticaly


df = pd.read_csv("/Users/kilimetr/Desktop/python/pandas/data_pandas_demo/survey_results_public.csv")
schema_df = pd.read_csv("/Users/kilimetr/Desktop/python/pandas/data_pandas_demo/survey_results_schema.csv")
filt = (df["Hobbyist"] == "Yes")
print(df[filt]) # print childrens according to filter
print(df.loc[filt, "MgrIdiot"]) # same as above but print just mgridiot
filt = (df["Hobbyist"] == "Yes") & (df["SurveyEase"] == "Neither easy nor difficult")
print(df[filt])
print(df.loc[~filt]) # negate the filtering logic above
filt = (df["SurveyEase"] == "Easy") | (df["SurveyEase"] == "Neither easy nor difficult")
print(df[filt])
high_salary = (df["ConvertedComp"] > 70000)
print(df.loc[high_salary, ["Country", "LanguageWorkedWith", "ConvertedComp"]])
countries = ["United States", "India", "United Kingdom", "Germany", "Canada"]
filt = df["Country"].isin(countries)
print(df.loc[filt, "Country"])
filt = df["LanguageWorkedWith"].str.contains("Python", na = False)
print(df.loc[filt, "LanguageWorkedWith"])


# # print(df.SurveyEase)
# print(df[["Respondent", "SurveyEase"]])
# print(df.columns)

# print(df.iloc[[0, 1], 3])
# print(df.loc[[0, 1], ["Respondent","SurveyEase"]])

# # df = pd.DataFrame(people)
