import plotly.graph_objs as go

import numpy as np
import math


print("Basic Sine Wave graph_objs")
x_points = np.arange(0, math.pi*2, 0.05)
y_points = np.sin(x_points)

trace0 = go.Scatter(x=x_points, y=y_points)

fig = go.Figure()
fig.add_trace(trace0)
fig.update_layout(title = 'Sine Wave')
fig.show()