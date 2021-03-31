import pandas as pd
import matplotlib.pyplot as plt
from numpy import asarray
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
download_url = (
"https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
)
df = pd.read_csv(download_url)
type(df)

pd.set_option("display.max.columns", None)

uk = df[(df["country"] == 'United Kingdom')]
thailand = df[(df["country"] == 'Thailand')]

%matplotlib
uk.plot(x="year", y="co2", label='UK', title='CO2 emissions in the UK between 1750 and 2019')
thailand.plot(x="year", y="co2", label='Thailand', title='CO2 emissions in Thailand between 1931 and 2019')

fig, ax = plt.subplots()
fig.suptitle("Comparing CO2 emissions between the UK and Thailand")
ax.set_xlabel("Year")
ax.set_ylabel("CO2")
uk.plot(x="year", y="co2", ax=ax, label='UK')
thailand.plot(x="year", y="co2", ax=ax, label='Thailand')

scaler = MinMaxScaler()
uk[['gdp','co2']] = scaler.fit_transform(uk[['gdp','co2']])

fig1, ax = plt.subplots()
fig1.suptitle("Comparing CO2 emissions and GDP growth in the UK")
ax.set_xlabel("Year")
ax.set_ylabel("Value")
uk.plot(x="year", y="gdp", ax=ax, label='GDP')
uk.plot(x="year", y="co2", ax=ax, label='CO2')

thailand[['gdp','co2']] = scaler.fit_transform(thailand[['gdp','co2']])

fig2, ax = plt.subplots()
fig2.suptitle("Comparing CO2 emissions and GDP growth in Thailand")
ax.set_xlabel("Year")
ax.set_ylabel("Value")
thailand.plot(x="year", y="gdp", ax=ax, label='GDP')
thailand.plot(x="year", y="co2", ax=ax, label='CO2')
