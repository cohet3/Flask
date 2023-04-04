from flask import (Blueprint, render_template)

bp = Blueprint('portfolio', __name__, url_prefix='/')
@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')