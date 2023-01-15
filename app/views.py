import networkx, osmnx, folium
from . import db
from flask import (render_template, flash, request, Blueprint)
from .forms import NodeForm
from .models import Node

index = Blueprint('index', __name__)

@index.route('/', methods=['GET', 'POST'])
def index():
    form = NodeForm(nodes=db.session.execute(db.select(Node).all()))

    if request.method == 'POST' and form.is_submitted():
        origin_node = db.get_or_404(Node, form.origin.data)
        destination_node = db.get_or_404(Node, form.destination.data)

        G = osmnx.graph_from_bbox(48.4661000,
                                  48.4602000,
                                  -123.3077000,
                                  -123.3165000,
                                  network_type="walk",
                                  retain_all=False)

        route = networkx.shortest_path(G, 
                                       origin_node.id, 
                                       destination_node.id, 
                                       weight='length')

        osmnx.plot_route_folium(G, 
                                route=route, 
                                route_map = \
                                    folium.Map(location=[48.463198, -123.311886], 
                                               zoom_start=17)
                                ).save('templates/map.html')

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'error {err_msg}', category='danger')

    return render_template('index.html', form=form)