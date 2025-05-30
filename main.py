from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('timetable_content.html')

@app.route('/teachers')
def about():
    return render_template('teachers.html')


if __name__ == '__main__':
    app.run()