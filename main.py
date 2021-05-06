from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, SelectField
from wtforms.validators import DataRequired
import requests
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
Bootstrap(app)
api_endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en_US"

language_codes = {
    "English (US)": "en_US",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "Japanese": "ja",
    "Russian": "ru",
    "English (UK)": "en_GB",
    "German": "de",
    "Italian": "it",
    "Korean": "ko",
    "Brazilian Portuguese": "pt-BR",
    "Arabic": "ar",
    "Turkish": "tr"
}


class NewWordForm(FlaskForm):
    style = {"class": "OurClasses", "style": "margin-bottom: 3%; font-size:20px;"}
    word = StringField(label="Search for a word:", validators=[DataRequired()], render_kw=style)
    language = SelectField(label="Language", choices=[x for x in language_codes.keys()],
                           validators=[DataRequired()], render_kw=style)
    submit = SubmitField("search", render_kw=style)


@app.route("/", methods=["POST", "GET"])
def homepage():
    form = NewWordForm()
    meanings = None
    if form.validate_on_submit():
        word = form.word.data
        lan = form.language.data
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/{language_codes[lan]}/{word}")
        try:
            data = response.json()[0]
        except KeyError:
            meanings = 0
        else:
            meanings = data["meanings"]

    return render_template("index.html", word_data=meanings, form=form)


if __name__ == "__main__":
    app.run(debug=True)
