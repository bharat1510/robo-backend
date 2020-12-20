from .. import db

class Robot(db.Model):
    """ Robot Model for storing robot related details """
    __tablename__ = "robot"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(50), unique=True)
    model = db.Column(db.String(50))
    registered_on = db.Column(db.DateTime, nullable=False)
    
    pi_type = db.Column(db.String(50))
    aurdino_type = db.Column(db.String(50))
    motor_type = db. Column(db.String(50))
    motor_driver_type = db.Column(db.String(50))
    battey_info = db.Column(db.String(50))
    public_url = db.Column(db.String(50), unique=True)
    public_pnumber = db.Column(db.String(5))
    is_solar = db.Column(db.Boolean)
    is_led = db.Column(db.Boolean)