from app import db

class Mesin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unit = db.Column(db.String(5), nullable=False)
    nama_mesin = db.Column(db.String(20), nullable=False)
    daya_mampu = db.Column(db.Integer, nullable=False)
    is_sewa = db.Column(db.Boolean, nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'))

    def __repr__(self):
        return '<{}. {} Unit {}>'.format(self.id, self.nama_mesin, self.unit)