from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import test_task2_1
import test_task1

# Скрипт админ-панели для работы с полученными записями

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'Data'
    id = db.Column(db.Integer, primary_key=True)
    uptime_text = db.Column(db.String(100), nullable=False)
    price_per_mn_text = db.Column(db.String(100), nullable=False)
    days_left_text = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<{}:{}:{}>".format(self.uptime_text, self.price_per_mn_text, self.days_left_text)


@app.route('/', methods=['POST', 'GET'])
def data():
    data = Data.query.order_by(Data.date.desc()).all()
    return render_template("data.html", data=data)


@app.route('/registration')
def registration():
    test_task1.main()
    return redirect('/')


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        uptime_text, price_per_mn_text, days_left_text = test_task2_1.main()
        date = Data(uptime_text=uptime_text, price_per_mn_text=price_per_mn_text, days_left_text=days_left_text)
        try:
            db.session.add(date)
            db.session.commit()
            return redirect('/')
        except:
            return "При добавлении новой записи произошла ошибка! "


@app.route('/<int:id>/update', methods=['POST', 'GET'])
def update(id):
    date = Data.query.get_or_404(id)
    if request.method == "POST":
        date.uptime_text = request.form['uptime_text']
        date.price_per_mn_text = request.form['price_per_mn_text']
        date.days_left_text = request.form['days_left_text']
    try:
        db.session.commit()
        return redirect('/')
    except:
        return "При обновлении записи произошла ошибка!"


@app.route('/<int:id>/delete')
def delete(id):
    data = Data.query.get_or_404(id)
    try:
        db.session.delete(data)
        db.session.commit()
        return redirect('/')
    except:
        return "При удалении записи произошла ошибка!"


if __name__ == "__main__":
    app.run(debug=True)