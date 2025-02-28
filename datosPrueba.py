import plotly.express as px
from taipy.gui import Gui, html

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

iris = html("""
<taipy:chart figure="{fig}"/>""")

Gui(iris).run(port=5500)