import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x="year", y="lifeExp", color='country')
fig.show()


df = px.data.gapminder().query("continent != 'Asia'") # remove Asia for visibility

print("df type: {}".format(type(df)))
print(df)

fig = px.line(df, x="year", y="lifeExp", color="continent",
              line_group="country", hover_name="country")
fig.show()
