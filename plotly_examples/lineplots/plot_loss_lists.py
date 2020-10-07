import os
from os.path import join
import plotly.graph_objs as go
import numpy as np


def plot_train_val_losses(training_loss: list, validation_loss: list,
                          save_dir: str = None, 
                          display: bool = False,
                          debug: bool = False,
                          interval: str = 'Epochs',
                          title: str = "Training Loss Curves") -> None:
    """
    Creates a one off train val plot.

    Args:
        training_loss (list): list of floats
        val_loss (list): list of floats
        save_dir (str): path to a location to save an exported image of the plot (or an interactive graph)
        debug (bool): default False
        ** kwargs (keyword arguments): checked for title, xlabel, ylabel, interval (epochs or batches)

    Returns:
        Nothing
    """
    x_values = list(np.arange(1, len(training_loss)+1))

    train_trace = go.Scatter(x=x_values, y=training_loss, mode='lines+markers', name='training_loss')
    val_trace = go.Scatter(x=x_values, y=validation_loss, mode='lines+markers', name='validation_loss')

    fig = go.Figure()
    fig.add_trace(train_trace)
    fig.add_trace(val_trace)
    fig.update_layout(title=title, xaxis_title=interval, yaxis_title='Loss')
    if display:
        fig.show()
    if save_dir is not None:
        fig.write_image(join(save_dir, "training_loss_curves.png"))
        fig.write_html(join(save_dir, "training_loss_curves.html"))
        fig.write_json(join(save_dir, "training_loss_curves.json"))
    return


train_loss = [0.9233, 0.9123, 0.8530, 0.7923, 0.6521, 0.5102, 0.4002, 0.3534, 0.3211, 0.2991, 0.2182]
val_loss = [0.9233, 0.9221, 0.8930, 0.8021, 0.6902, 0.6011, 0.5827, 0.5432, 0.5788, 0.5973, 0.6091]

save_path = './plot_loss_lists_out'
if not os.path.exists(save_path):
    os.mkdir(save_path)
plot_train_val_losses(training_loss=train_loss, validation_loss=val_loss, save_dir=save_path, display=True)
