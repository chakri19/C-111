import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("C-111HW.csv")
data = df["reading_time"].tolist()

meanPopNumber = statistics.mean(data)
stdevPopNumber = statistics.stdev(data)
print("Mean number is", meanPopNumber)
print("Standard number is", stdevPopNumber)

def random_set_of_mean():
    dataset = []
    for i in range(0,30):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def plot_graph(mean_list):
    dataFrame = mean_list
    fig = ff.create_distplot([dataFrame], ["reading_time"], show_hist = False)
    fig.show()  

stdSampleList = []
meanSampleList = []

mean_list = []
for i in range(0,100):
    set_of_means = random_set_of_mean()
    mean_list.append(set_of_means)
stdSampleList = statistics.stdev(mean_list)
meanSampleList = statistics.mean(mean_list)
print("The standard deviation of the sample data reading time is ", stdSampleList)
print("The mean of the sample data reading time is ", meanSampleList)
plot_graph(mean_list)


first_std_deviation_start, first_std_deviation_end = meanPopNumber - stdevPopNumber, meanPopNumber + stdevPopNumber
second_std_deviation_start, second_std_deviation_end = meanPopNumber - (2 * stdevPopNumber), meanPopNumber + (2 * stdevPopNumber)
third_std_deviation_start, third_std_deviation_end = meanPopNumber - (3 * stdevPopNumber), meanPopNumber + (3 * stdevPopNumber)

# finding the mean of the first data
df1 = pd.read_csv("Intervention1.csv")
data1 = df1["Math_score"].tolist()
meanSampleData1 = statistics.mean(data1)

# finding the mean of the second
df2 = pd.read_csv("Intervention2.csv")
data2 = df2["Math_score"].tolist()
meanSampleData2 = statistics.mean(data2)

# finding the mean of the third
df3 = pd.read_csv("Intervention3.csv")
data3 = df3["Math_score"].tolist()
meanSampleData3 = statistics.mean(data3)

fig1 = ff.create_distplot([meanSampleList],["Student Marks"], show_hist = False)
fig1.add_trace(go.Scatter(x =[meanSampleList, meanSampleList], y=[0,0.20], mode = "lines", name = "Mean"))
fig1.add_trace(go.Scatter(x =[first_std_deviation_start, first_std_deviation_start], y=[0,0.17], mode = "lines", name = "StdFirstStart"))
fig1.add_trace(go.Scatter(x =[first_std_deviation_end, first_std_deviation_end], y=[0,0.17], mode = "lines", name = "StdFirstEnd"))
fig1.add_trace(go.Scatter(x =[second_std_deviation_start, second_std_deviation_start], y=[0,0.17], mode = "lines", name = "StdSecondStart"))
fig1.add_trace(go.Scatter(x =[second_std_deviation_end, second_std_deviation_end], y=[0,0.17], mode = "lines", name = "StdSecondEnd"))
fig1.add_trace(go.Scatter(x =[third_std_deviation_start, third_std_deviation_start], y=[0,0.17], mode = "lines", name = "StdThirdStart"))
fig1.add_trace(go.Scatter(x =[third_std_deviation_end, third_std_deviation_end], y=[0,0.17], mode = "lines", name = "StdThirdEnd"))
fig1.add_trace(go.Scatter(x = [meanSampleData1, meanSampleData1], y = [0.017], mode = "lines", name = "Intervention 1"))
fig1.add_trace(go.Scatter(x = [meanSampleData2, meanSampleData2], y = [0.017], mode = "lines", name = "Intervention 2"))
fig1.add_trace(go.Scatter(x = [meanSampleData3, meanSampleData3], y = [0.017], mode = "lines", name = "Intervention 3"))
fig1.show()
print("Mean of Intervention 1:", meanSampleData1)
print("Mean of Intervention 2:", meanSampleData2)
print("Mean of Intervention 3:", meanSampleData3)

zScore1 = (meanSampleData1 - meanSampleList) / stdSampleList
zScore2 = (meanSampleData2 - meanSampleList) / stdSampleList
zScore3 = (meanSampleData3 - meanSampleList) / stdSampleList
print("Z Score 1:", zScore1)
print("Z Score 2:", zScore2)
print("Z Score 3:", zScore3)