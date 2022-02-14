from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from src.python import tle
from src.python.app import app
from src.python.calculation import findHorizonTime
from skyfield.toposlib import wgs84

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://" \
                                        "omoglffn:ySoZGmy1jAxRdoNRAvKk-LZLOBcqFrGH@castor.db.elephantsql.com/omoglffn"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Passes(db.Model):
    timestamp = db.Column(db.String, primary_key=True)
    id = db.Column(db.String)
    rise_at = db.Column(db.Time)
    set_at = db.Column(db.Time)
    duration = db.Column(db.Integer)
    interval = db.Column(db.String)

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "id": self.id,
            "rise_at": str(self.rise_at_at.strftime('%d-%m-%Y')),
            "set_at": str(self.set_at.strftime('%d-%m-%Y')),
            "duration": str(self.duration),
            "interval": self.interval
        }


def db_pass_example():
    row = []
    calculationJSON, calculationData = findHorizonTime(tle.loadTLE()["S-NET A"], 3 * 24 * 3600,
                                                       wgs84.latlon(33.6405, -117.8443,
                                                                    elevation_m=17))

    for key in calculationData.keys():
        row.append(Passes(timestamp=key, id="S-NET A",
                          rise_at=datetime.strptime(calculationData[key]['rise'], '%Y %b %d %H:%M:%S'),
                          set_at=datetime.strptime(calculationData[key]['set'], '%Y %b %d %H:%M:%S'),
                          duration=calculationData[key]['duration'], interval=calculationData[key]['interval']))

    for r in row:
        db.session.add(r)
    db.session.commit()
    db.close_all_sessions()


if __name__ == "__main__":
    # clear and re-declare db model
    # db.drop_all()
    # db.create_all()
    db_pass_example()
