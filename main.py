from flask import Flask, render_template
app = Flask(__name__)

#@app.route('/')
#def index():
    #return render_template('timetable_content.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lecturers/schedules')
def lecturer_schedules():
    return render_template('lecturer_schedule.html')

@app.route('/timetable/day/kampala')
def day_kampala():
    # You'll need to implement this view
    return render_template('day_kampala.html') 

@app.route('/timetable/day/main')
def day_main():
    # You'll need to implement this view
    return render_template('day_main.html')

@app.route('/timetable/weekend/kampala')
def weekend_kampala():
    # You'll need to implement this view
    return render_template('weekend_kampala.html')
@app.route('/schedule/day/kampala')
def day_kampala_schedule():
    return render_template('day_kampala_schedule.html')

@app.route('/schedule/day/main')
def day_main_schedule():
    return render_template('day_main_schedule.html')

@app.route('/schedule/weekend/kampala')
def weekend_kampala_schedule():
    return render_template('weekend_kampala_schedule.html')

if __name__ == '__main__':
    app.run(debug=True)