#app.py 
from flask import Flask, render_template, session, redirect, url_for 
from flask_wtf import Form 
from wtforms import StringField, SubmitField
from flask_bootstrap import Bootstrap
from wtforms.validators import Required

from wiki_sentiment import * 
from search_wiki import * 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

bootstrap = Bootstrap(app)

class SearchForm(Form):
    searchterm = StringField('Search Wikipedia and find the sentiment of the first paragraph', validators=[Required()])
    submit = SubmitField('Submit')

@app.route("/resume")
def hello():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        session['searchterm'] = form.searchterm.data 
        session['sentiment'], session['titlearticle'], session['wikiurl'] = get_sentiment_from_url(get_one_url_from_wiki_search(session.get('searchterm')))
        return redirect(url_for('search'))
    return render_template('search.html', form=form, searchterm=session.get('searchterm'), number=session.get('sentiment'), titlearticle=session.get('titlearticle'), wikiUrl=session.get('wikiurl'))

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)