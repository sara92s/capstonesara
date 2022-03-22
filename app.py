import os
from flask import (
  Flask,
  request,
  abort,
  jsonify
)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from models import setup_db, Movies, Actors
from flask_migrate import Migrate
from auth import requires_auth, AuthError

def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    CORS(app)

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization, true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS'
        )
        response.headers.add('Access-Control-Allow-origins', '*')
        return response

    @app.route('/', methods=['GET'])
    def start():
        return "<h1> This is the main page </h1>"

    @app.route("/movies")
    @requires_auth('get:movies')
    def retrieve_movies(jwt):
        movies = Movies.query.order_by(Movies.id).all()

        if len(movies) == 0:
            abort(404)

        return jsonify(
            {
                "success": True,
                "movies": movies,
                "total_movies": len(Movies.query.all()),
            }
        )

    @app.route("/movies/<int:movie_id>")
    @requires_auth('get:movies')
    def retrieve_movie(jwt, movie_id):
        current_movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        if current_movie is None:
            abort(404)
        
        return jsonify(
            {
                "success": True,
                "current_movie": current_movie,
            }
        )

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        try:
            movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

            if movie is None:
                abort(404)

            movie.delete()
            return jsonify(
                {
                    "success": True,
                    "deleted": movie_id,
                }
            )
        except:
            abort(422)

    @app.route("/movies", methods=["POST"])
    @requires_auth('post:movies')
    def create_movie(jwt):
        body = request.get_json()

        new_title = body.get("title", None)
        new_release_date = body.get("release_date", None)

        try:
            movie1 = Movies(title=new_title, release_date=new_release_date)
            movie1.insert()

            return jsonify({
                    "success": True,
                    "created": movie1
            }), 200
        except:
            abort(422)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def edit_movie(jwt, id):

        movie = Movies.query.get(id)

        if movie is None:
            abort(404)

        body = request.get_json()

        title = body.get("title")
        release_date = body.get("release_date")

        if (title is None) or (release_date is None):
            abort(422)

        try:
            if title is not None:
                movie.title = title

            if release_date is not None:
                movie.relaese_date = release_date

            movie.update()

            return jsonify({
                "success": True,
                "patched_movie": movie
            }), 200

        except:
            abort(422)

    @app.route("/actors")
    @requires_auth('get:actors')
    def retrieve_actors(jwt):
        actors = Actors.query.order_by(Actors.id).all()

        if len(actors) == 0:
            abort(404)

        return jsonify(
            {
                "success": True,
                "actors": actors,
                "total_actors": len(Actors.query.all()),
            }
        )

    @app.route("/actors/<int:actor_id>")
    @requires_auth('get:actors')
    def retrieve_actor(jwt, actor_id):
        current_actor = Actors.query.filter(Actors.id == actor_id).one_or_none()
        if current_actor is None:
            abort(404)
        
        return jsonify(
            {
                "success": True,
                "current_actor": current_actor,
            }
        )

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        try:
            actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()
            return jsonify(
                {
                    "success": True,
                    "deleted": actor_id,
                }
            )
        except:
            abort(422)

    @app.route("/actors", methods=["POST"])
    @requires_auth('post:actors')
    def create_actor(jwt):
        body = request.get_json()

        new_name = body.get("name", None)
        new_age = body.get("age", None)
        new_gender = body.get("gender", None)

        try:
            actor1 = Actors(name=new_name, age=new_age, gender=new_gender)
            actor1.insert()

            return jsonify(
                {
                    "success": True,
                    "created": actor1,
                }
            )

        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def edit_actor(jwt, actor_id):
        body = request.get_json()

        actor = Actors.query.get(actor_id)

        if actor is None:
            abort(404)

        new_name = body.get('name')
        new_age = body.get('age')
        new_gender = body.get('gender')

        if (new_name is None) or (new_age is None) or (new_gender is None):
            abort(422)

        try:
            if new_name is not None:
                actor.name = new_name
            if new_age is not None:
                actor.age = new_age
            if new_gender is not None:
                actor.gender = new_gender

            actor.update()
        except:
            abort(422)

        return jsonify({
            "success": True,
            "patched_actor": actor
        }), 200

    # errorhandlers

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}),
            405,
        )

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)