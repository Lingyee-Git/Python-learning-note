
```python
# 导入pandas
import pandas as pd
# 查看pandas版本
print(pd.__version__)

# series：一种一维

data = [100, 102, 104]
# 创建Series
series = pd.Series(data)
print(series)
# 0    100
# 1    102
# 2    104
# dtype: int64

# 指定索引
series = pd.Series(data, index = ["a", "b", "c"])
print(series)
# a    100
# b    102
# c    104
# dtype: int64

# loc():按索引标签定位
# iloc():按整数位置定位

# 读取
print(series.loc["a"])  # 100

# 修改
series.loc["c"] = 200
print(series.loc["c"])  # 200

# 根据位置读取
print(series.iloc[0])   # 100

data = [100, 102, 104, 200, 202]
series = pd.Series(data, index = ["a", "b", "c", "d", "e"])
# 规定读取规则
print(series[series > 200]) # e    202

# dictionary
# 字典一样可以转为Series

calories = {"Day 1": 1750, "Day 2":2100, "Day 3":1700}

series = pd.Series(calories)

print(series)
# Day 1    1750
# Day 2    2100
# Day 3    1700
# dtype: int64

print(series.loc["Day 1"])  # 1750

series.loc["Day 3"] += 500
print(series.loc["Day 3"])  # 2200

print(series[series > 2000])
# Day 2    2100
# Day 3    2200
# dtype: int64
```