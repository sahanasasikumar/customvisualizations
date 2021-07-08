import flask
import plotly.express as px
import plotly.io as pio

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def visualization():
    gapminder = px.data.gapminder()
    fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
    fig.show()

    #pio.write_html(fig, file='index.html', auto_open=True)


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
    