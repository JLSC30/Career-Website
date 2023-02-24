from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    'id': 1,
    'title': 'Job 1',
    'location': 'Job 1 location',
    'salary': '1000$',
  },{
    'id': 2,
    'title': 'Job 2',
    'location': 'Job 2 location',
    'salary': '2000$',
  },{
    'id': 3,
    'title': 'Job 3',
    'location': 'Job 3 location',
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
