from flask import Flask, render_template, request, redirect, url_for

# Создание экземпляра Flask
app = Flask(__name__, template_folder="templates")

# Маршрут для перенаправления на главную страницу
@app.route("/")
def index():
    return redirect(url_for('home'))

# Маршрут для отображения главной страницы
@app.route("/home")
def home():
    return render_template("home.html")

# Маршрут для ввода имени пользователя
@app.route("/name", methods=["GET", "POST"])
def name():
    if request.method == "POST":
        username = request.form["username"]  #
        return redirect(url_for("hello", username=username))
    return render_template("name.html")  #
# c помощью метода POST получаем имя пользователя из формы и перенаправляем
# если метод GET, отображаем страницу для ввода имени

# Маршрут для отображения страницы приветствия с именем пользователя на страницу приветствия
@app.route("/hello/<username>")
def hello(username):
    return render_template("hello.html", username=username)

# Маршрут для отображения страницы "О нас"
@app.route("/about")
def about():
    return render_template("about.html")

# Запуск приложения Flask
if __name__ == "__main__":
    app.run(debug=True)

