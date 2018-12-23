"""REST API for services."""
import flask
import media


@media.app.route('/api/v1/', methods=["GET"])
def get_services():
    """Return list of services.

    Example:
    {
        "videos": "/api/v1/videos/",
        "watched": "/api/v1/watched/",
        "upload": "/api/v1/upload/",
        "video": "/api/v1/video/",
        "url": "/api/v1/"
    }
    """

    context = {
        "videos": "/api/v1/videos/",
        "watched": "/api/v1/watched/",
        "upload": "/api/v1/upload/",
        "video": "/api/v1/video/",
        "url": "/api/v1/"
    }

    return flask.jsonify(**context)
