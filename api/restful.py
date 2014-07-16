import json, pdb, re
from flask import jsonify, request, Response, make_response
from google.appengine.ext import ndb

from flask.ext.restful import  Resource

def debug():
    debug =True
    if debug:
        pdb.set_trace()


def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class ModelIdAPI(Resource):
    mode = None
    def get(self, id_val):
        return jsonify(get_entity(self.mode,id_val).to_dict())

    def put(self, id_val):
        entity = get_entity(self.mode,id_val)
        save_entity(model,request, entity)
        return jsonify({'success':True})

    def delete(self, id_val):
        entity = get_entity(self.mode,id_val)
        entity.key.delete()
        return jsonify({'success':True})


class ModelAPI(Resource):
    mode = None
    def get(self):
        resp = Response(json.dumps([c.to_dict() for c in self.mode.query()]), mimetype='application/json')
        resp.status_code = 200

        print resp
        return make_response(resp)

    def post(self):
        model = self.mode
        entity = model()
        save_entity(model,request, entity)
        return jsonify({'success': True})

def get_entity(model,id):
    key = ndb.Key(model,int(id) ^ 0xBADAD)
    return key.get()
def save_entity(model,request, entity):
        data = request.form
        if not data:
            data= request.json
        props = model._properties
        attrs = [ k for k in props.keys() ]
        for attr in attrs:
            val = None
            if data[attr]:
                if type(props[attr]) is ndb.StringProperty:
                    print "attr %s "%data[attr]
                    val = data[attr]
                elif type(props[attr]) is ndb.IntegerProperty:
                    val = int(data[attr])
            setattr(entity, attr, val)
        entity.put()
def restify(api,model,base_url):
    model_api= ModelAPI
    model_id_api = ModelIdAPI
    model_api.mode = model
    model_id_api.mode = model

    api.add_resource(model_id_api, base_url+'/<int:id_val>', endpoint = convert(model.__name__))
    api.add_resource(model_api, base_url, endpoint = convert(model.__name__)+'_list')
    api.add_resource(model_api, base_url+"/", endpoint = convert(model.__name__)+'_list_')
