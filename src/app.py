#!/usr/bin/env python
# coding: utf-8

# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle


app = Flask(__name__)
api = Api(app)


model = pickle.load( open( "../data/trained_model.p", "rb" ) )

class Predict(Resource):
    def post(self):
        json_data = request.get_json()
        print(json_data)
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # it is much simpler because we used pipelines during development
        res = model.predict(df)
        # we cannot send numpt array as a result
        return res.tolist()


api.add_resource(Predict, '/predict')

app.run(debug=True, host='0.0.0.0', port=5002)








