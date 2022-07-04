from app import db
import enum

class HarEnum(enum.Enum):
    Standby = 'Standby'
    P0 = 'PO'
    P1 = 'P1'
    P2 = 'P2'
    P3 = 'P3'
    P4 = 'P4'
    P5 = 'P5'
    TO = 'TO'
    SO = 'SO'
    MO = 'MO'
    PdM = 'PdM'
    CM = 'CM'



class Har(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tanggal_jumat = db.Column(db.String(30), nullable=False)
    jumat = db.Column(db.Enum(HarEnum), nullable=False)
    sabtu = db.Column(db.Enum(HarEnum), nullable=False)
    minggu = db.Column(db.Enum(HarEnum), nullable=False)
    senin = db.Column(db.Enum(HarEnum), nullable=False)
    selasa = db.Column(db.Enum(HarEnum), nullable=False)
    rabu = db.Column(db.Enum(HarEnum), nullable=False)
    kamis = db.Column(db.Enum(HarEnum), nullable=False)
    mesin_id = db.Column(db.Integer, db.ForeignKey('mesin.id'))

    def __repr__(self):
        return '<{}. {}>'.format(self.id, self.tanggal_jumat)