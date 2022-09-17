import json

from flask import request
from flask_restx import Api, Resource
from werkzeug.datastructures import MultiDict


from apps.api import blueprint
from apps.api.forms import BookForm, CityForm
from apps.models import Book, City
from apps.authentication.decorators import token_required


api = Api(blueprint)


@api.route('/books/', methods=['POST', 'GET', 'DELETE', 'PUT'])
@api.route('/books/<int:model_id>/', methods=['GET', 'DELETE', 'PUT'])
class BookRoute(Resource):
    def get(self, model_id: int = None):
        if model_id is None:
            all_objects = Book.query.all()
            output = [{'id': obj.id, **BookForm(obj=obj).data} for obj in all_objects]
        else:
            obj = Book.query.get(model_id)
            if obj is None:
                return {
                           'message': 'matching record not found',
                           'success': False
                       }, 404
            output = {'id': obj.id, **BookForm(obj=obj).data}
        return {
                   'data': output,
                   'success': True
               }, 200

    @token_required
    def post(self):
        try:
            body_of_req = request.form
            if not body_of_req:
                raise Exception()
        except Exception:
            if len(request.data) > 0:
                body_of_req = json.loads(request.data)
            else:
                body_of_req = {}
        form = BookForm(MultiDict(body_of_req))
        if form.validate():
            try:
                obj = Book(**body_of_req)
                Book.query.session.add(obj)
                Book.query.session.commit()
            except Exception as e:
                return {
                           'message': str(e),
                           'success': False
                       }, 400
        else:
            return {
                       'message': form.errors,
                       'success': False
                   }, 400
        return {
                   'message': 'record saved!',
                   'success': True
               }, 200

    @token_required
    def put(self, model_id: int):
        try:
            body_of_req = request.form
            if not body_of_req:
                raise Exception()
        except Exception:
            if len(request.data) > 0:
                body_of_req = json.loads(request.data)
            else:
                body_of_req = {}

        to_edit_row = Book.query.filter_by(id=model_id)

        if not to_edit_row:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404

        obj = to_edit_row.first()

        if not obj:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404

        form = BookForm(MultiDict(body_of_req), obj=obj)
        if not form.validate():
            return {
                       'message': form.errors,
                       'success': False
                   }, 404

        table_cols = [attr.name for attr in to_edit_row.__dict__['_raw_columns'][0].columns._all_columns]

        for col in table_cols:
            value = body_of_req.get(col, None)
            if value:
                setattr(obj, col, value)
        Book.query.session.add(obj)
        Book.query.session.commit()
        return {
            'message': 'record updated',
            'success': True
        }

    @token_required
    def delete(self, model_id: int):
        to_delete = Book.query.filter_by(id=model_id)
        if to_delete.count() == 0:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404
        to_delete.delete()
        Book.query.session.commit()
        return {
                   'message': 'record deleted!',
                   'success': True
               }, 200


@api.route('/cities/', methods=['POST', 'GET', 'DELETE', 'PUT'])
@api.route('/cities/<int:model_id>/', methods=['GET', 'DELETE', 'PUT'])
class CityRoute(Resource):
    def get(self, model_id: int = None):
        if model_id is None:
            all_objects = City.query.all()
            output = [{'id': obj.id, **CityForm(obj=obj).data} for obj in all_objects]
        else:
            obj = City.query.get(model_id)
            if obj is None:
                return {
                           'message': 'matching record not found',
                           'success': False
                       }, 404
            output = {'id': obj.id, **CityForm(obj=obj).data}
        return {
                   'data': output,
                   'success': True
               }, 200

    @token_required
    def post(self):
        try:
            body_of_req = request.form
            if not body_of_req:
                raise Exception()
        except Exception:
            if len(request.data) > 0:
                body_of_req = json.loads(request.data)
            else:
                body_of_req = {}
        form = CityForm(MultiDict(body_of_req))
        if form.validate():
            try:
                obj = City(**body_of_req)
                City.query.session.add(obj)
                City.query.session.commit()
            except Exception as e:
                return {
                           'message': str(e),
                           'success': False
                       }, 400
        else:
            return {
                       'message': form.errors,
                       'success': False
                   }, 400
        return {
                   'message': 'record saved!',
                   'success': True
               }, 200

    @token_required
    def put(self, model_id: int):
        try:
            body_of_req = request.form
            if not body_of_req:
                raise Exception()
        except Exception:
            if len(request.data) > 0:
                body_of_req = json.loads(request.data)
            else:
                body_of_req = {}

        to_edit_row = City.query.filter_by(id=model_id)

        if not to_edit_row:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404

        obj = to_edit_row.first()

        if not obj:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404

        form = CityForm(MultiDict(body_of_req), obj=obj)
        if not form.validate():
            return {
                       'message': form.errors,
                       'success': False
                   }, 404

        table_cols = [attr.name for attr in to_edit_row.__dict__['_raw_columns'][0].columns._all_columns]

        for col in table_cols:
            value = body_of_req.get(col, None)
            if value:
                setattr(obj, col, value)
        City.query.session.add(obj)
        City.query.session.commit()
        return {
            'message': 'record updated',
            'success': True
        }

    @token_required
    def delete(self, model_id: int):
        to_delete = City.query.filter_by(id=model_id)
        if to_delete.count() == 0:
            return {
                       'message': 'matching record not found',
                       'success': False
                   }, 404
        to_delete.delete()
        City.query.session.commit()
        return {
                   'message': 'record deleted!',
                   'success': True
               }, 200

