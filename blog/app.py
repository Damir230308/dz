from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.models.database import db
from blog.views.auth import auth_app, login_manager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Flask_GB/blog/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "abcdefg123456"
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")
login_manager.init_app(app)
db.init_app(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.cli.command("init-db")
def init_db():
    db.create_all
    print("done!")

@app.cli.command("create-users")
def create_users():
    from blog.models import User
    admin = User(user_name="addd", is_staff=True)
    james = User(user_name="genius")
    
    db.session.commit()
    db.session.add_all([admin, james])
    db.session.commit()
    
    print("done! created users:", admin, james)
