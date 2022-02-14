from flask_sqlalchemy import SQLAlchemy
from src.python.app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://" \
                                        "omoglffn:ySoZGmy1jAxRdoNRAvKk-LZLOBcqFrGH@castor.db.elephantsql.com/omoglffn"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }


exampleData = Post(id=3, title="testTitle", description="testDescription", created_at="now")
db.session.add(exampleData)
db.session.commit()
