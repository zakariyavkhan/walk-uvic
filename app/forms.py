from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class NodeForm(FlaskForm):
    origin = SelectField('Origin',
                         coerce=int)
    destination = SelectField('Destination',
                              coerce=int)
    submit = SubmitField(label='Go')

    def __init__(self, nodes=None):
        super().__init__()
        if nodes:
            self.origin.choices = nodes
            self.destination.choices = nodes