import json
import pandas as pd
import plotly.graph_objects as go

def to_json(data, filepath="block1_output.json"):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def table_output(matched):
    df = pd.DataFrame(matched, columns=["time", "fut_high", "spot_high"])
    return df

def plot_peaks(df, matched):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, y=df["high"], mode="lines", name="Futures"
    ))

    times = [x[0] for x in matched]
    fut_vals = [x[1] for x in matched]

    fig.add_trace(go.Scatter(
        x=times, y=fut_vals, mode="markers", name="Futures Peaks"
    ))

    fig.show()
