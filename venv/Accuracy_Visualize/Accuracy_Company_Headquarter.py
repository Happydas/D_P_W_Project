
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('Happy_Das', 'gqFHrnV4u2yQkUdckBtD')
X, Y = [], []
for line in open('../Results/Company_Headquarter/Company_headquarter_Average_Accuracy.txt', 'r'):
  values = [str(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

data1 = {
  "x": X,
  "y": Y,

  "name": "Average accuracy for Company_Headquarter",
  "type": "scatter"
}


data = Data([data1])
layout = {
  "title": "Average accuracy against testing data set",
  "xaxis": {"title": "Number of Vectors"},
  "yaxis": {"title": "Average accuracy"}
}

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)




