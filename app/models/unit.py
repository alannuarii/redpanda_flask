from app import db

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_unit = db.Column(db.String(20), nullable=False)
    mesins = db.relationship('Mesin', backref='kit', cascade="all, delete-orphan")

    def __repr__(self):
        return '<{}. {}>'.format(self.id, self.nama_unit)