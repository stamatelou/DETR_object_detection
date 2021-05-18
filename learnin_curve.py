import pandas as pd
df = pd.read_csv("all_losses.csv")

import plotly.graph_objects as go
# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df.train_losses,
                    mode='lines+markers',
                    name='train loss'))
fig.add_trace(go.Scatter(x=df.index, y=df.valid_losses,
                    mode='lines+markers',
                    name='valid loss'))

fig.update_layout(
    xaxis_title="epochs",
    yaxis_title="loss",
     legend=dict(
        x=0.81,
        y=1,
        traceorder='normal',
        font=dict(
            size=12,),
    )
)
fig.show()

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df.mean_ap,
                    mode='lines+markers',
                    name='train_losses',))
fig.update_layout(
    xaxis_title="epochs",
    yaxis_title="mAP",
)

fig.show()

