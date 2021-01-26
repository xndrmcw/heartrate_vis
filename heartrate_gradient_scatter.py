import plotly.express as px
import pandas as pd



data = pd.read_csv(r"C:\Users\Alexander\Desktop\Fun Programming\catherine_birthday_HR.csv")

x_axis = list(data.iloc[:, 0])
y_axis = list(data.iloc[:, 1])

pd.set_option('display.max_columns', None)
print(data.head())

figure = px.scatter(data_frame=data, x = x_axis, y = y_axis,
                    title="BIRTHDAY HR DATA",
                    color = 'Heart Rate', color_continuous_scale='Agsunset')


figure.update_layout(
    title={
        'x':0.5,
        'xanchor': 'center',},
    font=dict(size=20),
    xaxis=dict(
        title='',
        ticktext=['7 P.M.', '8 P.M.', '9 P.M.', '10 P.M.', '11 P.M.','12 A.M.','1 A.M.', '2 A.M.'],
        tickvals=[0, 426, 800, 1176, 1535, 1894, 2348, 2834],
        tickangle=0,
        tickmode="array",
        titlefont=dict(size=30)),
    yaxis=dict(
        title='',
        showticklabels=False)
)
figure.update_xaxes(automargin=True)
figure.update_traces(mode='markers', marker_size=6)
figure.show()

import chart_studio.plotly as py
py.plot(figure, filename = 'heartrate_gradient_scatter.py', auto_open=True)