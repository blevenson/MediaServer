"""REST API for services."""
import flask
import media


@media.app.route('/api/v1/', methods=["GET"])
def get_services():
    """Return list of services.

    Example:
    {
      "videos": "/api/v1/videos/",
      "url": "/api/v1/"
    }
    """

    context = {
        "videos": "/api/v1/videos/",
        "url": "/api/v1/"
    }

    return flask.jsonify(**context)
