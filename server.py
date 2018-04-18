from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_cors import CORS
from app.score_controller import ScoreController
from app.score_par_controller import ScoreParController

models = {
  'quickscore': ['untrained']
, 'feature_based': ['fb-college']
, 'bow': ['untrained', 'bow-college']
, 'bow, feature_based': ['bow_fb-sick', 'bow_fb-college']
, 'infersent': ['untrained', 'infersent-sick', 'infersent-college']
, 'infersent, feature_based': ['infersent_fb-college']
}

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/index')
def index():
	return redirect(url_for('score'))

@app.route('/score')
def score():
	return render_template('score.html', models=models)

@app.route('/score/csv')
def score_csv():
	return render_template('score-csv.html', models=models)

@app.route('/free-recall')
def recall():
	return render_template('free_recall.html', models=models)

score_controller = ScoreController(max_sentence_len=250)
score_par_controller = ScoreParController(max_par_len=2000, max_targets=30, max_responses=30)
app.add_url_rule('/api/score', 'api_score', score_controller.route, methods=['GET', 'POST'])
app.add_url_rule('/api/score-par', 'api_par_score', score_par_controller.route, methods=['GET', 'POST'])

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=5002, debug=False, threaded=False)
