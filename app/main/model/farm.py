from .. import db

class Farm(db.Model):
    """ Robot Model for storing robot related details """
    __tablename__ = "farm"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    owner = db.Column(db.String(50))
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Farm '{}'>".format(self.public_id)