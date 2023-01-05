from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import InputRequired, ValidationError
from . import db

class NodeForm(FlaskForm):
    def validate_origin(self, origin_to_check):
        if not db.Query.filter_by(name=origin_to_check.data):
            raise ValidationError('Cannot find origin node: ' + origin_to_check.data)
        
    def validate_destination(self, destination_to_check):
        if not db.Query.filter_by(name=destination_to_check.data):
            raise ValidationError('Cannot find destination node: ' + destination_to_check.data)

    origin = SelectField('Origin',
                         coerce=int,
                         validators=InputRequired())
    destination = SelectField('Destination',
                              coerce=int,
                              validators=InputRequired())
    submit = SubmitField(label='Go')
    
    def __init__(self, nodes=None):
        super().__init__()
        if nodes:
            self.origin.choices, self.destination.choices = \
                [(node.id, node.name) for node in nodes]