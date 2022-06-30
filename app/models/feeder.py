from app import db

class Feeder(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tanggal = db.Column(db.String(30), nullable=False)
    jam = db.Column(db.String(10), nullable=False)
    kota = db.Column(db.Integer, nullable=True, default=0)
    tona = db.Column(db.Integer, nullable=True, default=0)
    kolongan = db.Column(db.Integer, nullable=True, default=0)
    lesabe = db.Column(db.Integer, nullable=True, default=0)
    tamako = db.Column(db.Integer, nullable=True, default=0)
    mainlinepetta = db.Column(db.Integer, nullable=True, default=0)
    pettakota = db.Column(db.Integer, nullable=True, default=0)
    mainlinetahuna = db.Column(db.Integer, nullable=True, default=0)
    kendahe = db.Column(db.Integer, nullable=True, default=0)
    bowongkulu = db.Column(db.Integer, nullable=True, default=0)
    kotatamako = db.Column(db.Integer, nullable=True, default=0)
    lapango = db.Column(db.Integer, nullable=True, default=0)
    tahuna = db.Column(db.Integer, nullable=True, default=0)
    salurang = db.Column(db.Integer, nullable=True, default=0)
    pintareng = db.Column(db.Integer, nullable=True, default=0)
    tahunaincome = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<{}. {}>'.format(self.id, self.tanggal)

    

    