"""REST API for services."""
import flask
import media


@media.app.route('/api/v1/', methods=["GET"])
def get_services():
    """Return list of services.

    Example:
    {
      "posts": "/api/v1/p/",
      "url": "/api/v1/"
    }
    """
    if "username" not in flask.session:
        flask.abort(403)

    context = {
        "posts": "/api/v1/p/",
        "url": "/api/v1/"
    }

    return flask.jsonify(**context)
