from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SelectField, SubmitField, FloatField, BooleanField, HiddenField, TimeField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date

currencies=[('EUR', 'EUR'), ('BTC', 'BTC'),
     ('ETH', 'ETH'), ('XRP', 'XRP'), ('LTC', 'LTC'), 
     ('BCH', 'BCH'), ('BNB', 'BNB'), ('USDT', 'USDT'), 
     ('EOS', 'EOS'), ('BSV', 'BSV'), ('XLM', 'XLM'),
     ('ADA', 'ADA'), ('TRX', 'TRX')]

class MovimientosForm(FlaskForm):
    id = HiddenField()
    fecha = DateField('Fecha', validators=[DataRequired()])
    hora=TimeField('Hora', validators = [DataRequired()])
    fromCcy = SelectField('FromCcy', choices=currencies)

    
    fromQty=FloatField('FromQty', validators = [DataRequired()])
   
    toCcy = SelectField('ToCcy', choices= currencies)
    
    toQty=FloatField('ToQty', validators = [DataRequired()])
    p_u = FloatField('P_U', validators = [DataRequired()])
    
    submit = SubmitField('Purchase') 