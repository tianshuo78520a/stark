from flask import Blueprint, render_template, request
from chun import db
from chun import models
from chun.utils.page import Pagination


ac = Blueprint('ac', __name__)


@ac.route('/info', methods=['GET', 'POST'])
def index():
    pubishing = db.session.query(models.New).all()

    # 分页
    data_count = len(pubishing)
    current_page = request.args.get('page', 1)
    pager = Pagination(data_count, current_page, '/info')
    user_list = pubishing[pager.start:pager.end]
    page_html = pager.page_html()

    db.session.remove()
    print(page_html)
    # return render_template('info.html', user_list=user_list, page_html=page_html)
    return render_template('info.html', data=user_list, page_html=page_html)







