# -*- coding:utf-8 -*-

import turbo.log

from models.blog.model import Blog

from . import base
from store import actions

BaseHandler = base.BaseHandler
logger = turbo.log.getLogger(__file__)


class HomeHandler(BaseHandler):

    def get(self):
        result = self.db.query(Blog).add_columns(
            Blog.id, Blog.text).all()
        self.render('index.html', result=result)


class IncHandler(BaseHandler):

    _get_params = {
        'option': [
            ('value', int, 0)
        ]
    }

    def get(self):
        self._data = actions.increase(self._params['value'])
        self.write(str(self._data))


class MinusHandler(BaseHandler):

    _get_params = {
        'option': [
            ('value', int, 0)
        ]
    }

    def get(self):
        self._data = actions.decrease(self._params['value'])
        self.write(str(self._data))
