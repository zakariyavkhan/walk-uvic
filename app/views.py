import networkx, osmnx, folium
from . import db
from flask import (render_template, Blueprint, request, flash)
from .forms import NodeForm
from .models import Node
from sqlalchemy.sql import select

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def index():
    form = NodeForm(nodes = \
        db.session.scalars(select(Node)).all())

    if request.method == 'POST' and form.is_submitted():
        origin_node = db.get_or_404(Node, form.origin.data)
        destination_node = db.get_or_404(Node, form.destination.data)

        G = osmnx.graph_from_bbox(48.4661000,
                                  48.4602000,
                                  -123.3077000,
                                  -123.3165000,
                                  network_type='walk',
                                  retain_all=False)

        route = networkx.shortest_path(G, origin_node.id, 
                                       destination_node.id, 
                                       weight='length')

        osmnx.plot_route_folium(G, route=route, 
                                route_map = \
                                folium.Map(location=[48.463198, -123.311886], 
                                            zoom_start=18)).save('app/templates/map.html')

    return render_template('home.html', form=form)
