from flask import url_for

from app import db

class Record(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  team = db.Column(db.String, nullable=False)
  pos = db.Column(db.String, nullable=False)
  age = db.Column(db.Float, nullable=False)
  gp = db.Column(db.Integer, nullable=False)
  mpg = db.Column(db.Float, nullable=False)
  fta = db.Column(db.String, nullable=False)
  ftp = db.Column(db.Float, nullable=False)
  twpa = db.Column(db.String, nullable=False)
  twpp = db.Column(db.Float, nullable=False)
  thpa = db.Column(db.String, nullable=False)
  thpp = db.Column(db.Float, nullable=False)
  ppg = db.Column(db.Float, nullable=False)
  rpg = db.Column(db.Float, nullable=False)
  apg = db.Column(db.Float, nullable=False)
  spg = db.Column(db.Float, nullable=False)
  bpg = db.Column(db.Float, nullable=False)
  topg = db.Column(db.Float, nullable=False)

  def __repr__(self):
    return f"<Record: {self.name} ({self.team}) | {self.pos}>"

  def to_dict(self):
    data = dict(
      id=self.id,
      name=self.name,
      team=self.team,
      pos=self.pos,
      age=self.age,
      gp=self.gp,
      mpg=self.mpg,
      fta=self.fta,
      ftp=self.ftp,
      twpa=self.twpa,
      twpp=self.twpp,
      thpa=self.thpa,
      thpp=self.thpp,
      ppg=self.ppg,
      rpg=self.rpg,
      apg=self.apg,
      spg=self.spg,
      bpg=self.bpg,
      topg=self.topg,
      _links=dict(
        self=url_for('get_record', id=self.id)
      )
    )
    return data