import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv(r"C:\Users\Alexander\Desktop\Fun Programming\catherine_birthday_HR.csv")

#x_axis = list(range(data.shape[0] - 1))
x_axis = list(data.iloc[:, 0])
y_axis = list(data.iloc[1:, 1])

pd.set_option('display.max_columns', None)
print(data.head())


figure = go.Figure(
    data = [go.Scatter(x = x_axis, y = y_axis, mode = 'lines')], # list of traces
    layout = {"title":"Birthday HR Data"},
    color = 'y_axis'# dictionary of key value pairs
    #frames = [] # list of frames or list of figure
)

figure.update_layout(
    xaxis=dict(
        title_text="Time",
        ticktext=['7 P.M.', '8 P.M.', '9 P.M.', '10 P.M.', '11 P.M.','12 A.M.','1 A.M.', '2 A.M.'],
        tickvals=[0, 426, 800, 1176, 1535, 1894, 2348, 2834],
        tickangle=0,
        tickmode="array",
        titlefont=dict(size=30)),
    yaxis=dict(
        title_text="Heartrate\n(BPM)",
    ))
figure.update_xaxes(automargin=True)
figure.show()
