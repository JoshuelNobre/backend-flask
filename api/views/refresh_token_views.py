from os import access
from flask_restful import Resource
from api import api
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..entity import user
from ..services import user_service
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from datetime import timedelta


class RefreshTokenList(Resource):

    @jwt_required(refresh=True)
    def post(self):
        user_token = get_jwt_identity()
        access_token = create_access_token(
            identity=user_token,
            expires_delta=timedelta(seconds=200)
        )
        refresh_token = create_refresh_token(
                    identity=user_token
                )
        return make_response({
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200)


api.add_resource(RefreshTokenList, '/token/refresh')

