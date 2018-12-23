"""REST API for marking videos as watched."""
import sqlite3
import flask
import media


@media.app.route('/api/v1/watched/', methods=["POST", "DELETE"])
def set_watched():
    """Mark video as watched or unwatched."""

    connection = media.model.get_db()

    context = {}

    # url
    context["url"] = flask.request.path

    # Check if post request
    if flask.request.method == 'POST':
        # Mark video as watched
        connection.execute(('UPDATE videos SET watched = 1 WHERE videoid = %s')
                           % (str(flask.request.json['videoid'])))

        return flask.jsonify(**context), 201

    if flask.request.method == 'DELETE':
        # Mark post as unwatched
        connection.execute(('UPDATE videos SET watched = 0 WHERE videoid = %s')
                           % (str(flask.request.json['videoid'])))
        return flask.jsonify(), 204

    return flask.jsonify(**context)
