
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('Happy_Das', 'gqFHrnV4u2yQkUdckBtD')
X, Y = [], []
for line in open('../Results/Capital_Country/Main_Capital_Country_Average_Accuracy.txt', 'r'):
  values = [str(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

data1 = {
  "x": X,
  "y": Y,

  "name": "Accuracy for Country-Capital",
  "type": "scatter"
}

X, Y = [], []
for line in open('../Results/Currency_Country/Main_Currency_Country_Average_Accuracy.txt', 'r'):
  values = [str(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

data2 = {
  "x": X,
  "y": Y,
  "name": "Accuracy for Country-Currency",
  "type": "scatter"
}

X, Y = [], []
for line in open('../Results/Company_Headquarter/Company_headquarter_Average_Accuracy.txt', 'r'):
  values = [str(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

data3 = {
  "x": X,
  "y": Y,

  "name": "Accuracy for Company_Headquarter",
  "type": "scatter"
}

X, Y = [], []
for line in open('../Results/Person_Party/Main_Person_Party_Average_Accuracy.txt', 'r'):
  values = [str(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

data4 = {
  "x": X,
  "y": Y,
  "name": "Accuracy for Person-Party",
  "type": "scatter"
}

data = Data([data1, data2, data3, data4])
#data = Data([trace1])
layout = {
  #"title": "Accuracy against testing data set",
  "xaxis": {"title": "Number of Vectors"},
  "yaxis": {"title": "Average Accuracy"}
}

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)



