from .. import db

class VirtualMap(db.Model):
    """ Robot Model for storing robot related details """
    __tablename__ = "virtual_map"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(50), unique=True)
    latitude = db.Column(db.Float(Precision=64))
    longitude = db.Column(db.Float(Precision=64))
    farm_id = db.Column(db.String(100), unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)