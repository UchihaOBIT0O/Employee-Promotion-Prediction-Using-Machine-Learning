import pickle
from flask import Flask, render_template, request

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/home')
def home1():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/pred', methods=['POST'])
def pred():
    department = request.form['department']
    education = request.form['education']
    if education == '1':
        education = 1
    elif education == '2':
        education = 2
    else:
        education = 3
    no_of_trainings = request.form['no_of_trainings']
    age = request.form['age']
    previous_year_rating = request.form['previous_year_rating']
    length_of_service = request.form['length_of_service']
    KPIs = request.form['KPIs']
    if KPIs == '0':
        KPIs = 0
    else:
        KPIs = 1
    awards_won = request.form['awards_won']
    if awards_won == '0':
        awards_won = 0
    else:
        awards_won = 1
    avg_training_score = request.form['avg_training_score']
    total = [[department, education, no_of_trainings, age, float(previous_year_rating), float(length_of_service),
              KPIs, awards_won, avg_training_score]]
    prediction = model.predict(total)
    if prediction == 0:
        text = 'Sorry, you are not eligible for promotion'
    else:
        text = 'Great, you are eligible for promotion'
    return render_template('submit.html', predictionText=text)


if __name__ == '__main__':
    app.run(debug=True)





