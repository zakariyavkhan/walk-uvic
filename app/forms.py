from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class NodeForm(FlaskForm):
    # searchfield?
    origin = SelectField('Origin')
    destination = SelectField('Destination')
    submit = SubmitField(label='Go')

    def __init__(self, nodes=None):
        super().__init__()
        if nodes:
            self.origin.choices = [node.name for node in nodes]
            self.destination.choices = [node.name for node in nodes]