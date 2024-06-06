from django.shortcuts import render

from django_plotly import settings
from .data_processing import load_csv, select_columns
import plotly.express as px
import pandas as pd
import os


def plot_view(request):
    path = os.path.join(settings.BASE_DIR, 'data', 'data.csv')
    data = load_csv(path)
    c1 = "age"
    c2 = "experience"
    selected_data = select_columns(data, column1=c1, column2=c2)
    fig = px.scatter(selected_data, x=c1, y=c2, title="Our First Plot")

    plot_div = fig.to_html(full_html=False)

    context = {"plot_div": plot_div}
    return render(request, "plot.html", context)

def hello(request):
    return render(request, "hello.html", {"hello":"HI"})