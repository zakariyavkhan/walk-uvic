import networkx, osmnx
from . import db
from flask import (
    render_template,
    flash,
    request,
    Blueprint,
)
from .forms import NodeForm

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def home_page():
    # draw, save map to map.html

    form = NodeForm(nodes=db.Query.all())
    if request.method == 'POST' and form.validate_on_submit():
        origin_node = db.Query.get(form.origin.data)
        destination_node = db.Query.get(form.destination.data)

        # .save('templates/map.html')
        # redirect
        #pass node ids to osmnx
        #draw route and add to map.html

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'error {err_msg}', category='danger')

    return render_template('home.html', form=form)