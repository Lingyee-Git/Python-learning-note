```python
# DataFrame

import pandas as pd

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]
        }

# 也可以写为：
# data = [{"Name": "Spongebob", "Age": 30},
#         {"Name": "Patrick", "Age": 35},
#         {"Name": "Squidward", "Age": 50}]

df = pd.DataFrame(data)
print(df)
#         Name  Age
# 0  Spongebob   30
# 1    Patrick   35
# 2  Squidward   50

df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])
print(df)
#                  Name  Age
# Employee 1  Spongebob   30
# Employee 2    Patrick   35
# Employee 3  Squidward   50

print(df.loc["Employee 1"])
# Name    Spongebob
# Age            30
# Name: Employee 1, dtype: object

print(df.iloc[0])
# Name    Spongebob
# Age            30
# Name: Employee 1, dtype: object

# 添加新列
df["Job"] = ["Cook", "N/A", "Cashier"]
print(df)

# 添加新行
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}],
                       index = ["Employee 4"])
df = pd.concat([df, new_row])   # 由于concat()函数接收的参数是一个包含数据框的列表，因此要用[]框起来
print(df)
#                  Name  Age       Job
# Employee 1  Spongebob   30      Cook
# Employee 2    Patrick   35       N/A
# Employee 3  Squidward   50   Cashier
# Employee 4      Sandy   28  Engineer
```