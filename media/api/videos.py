"""REST API for videos."""
import flask
import media

from os import listdir

print("Running")


@media.app.route('/api/v1/videos/', methods=["GET"])
def get_video_list():
    """Return list of stored videos.

    Example:
    {
      "videos": ['vid.mov', 'anotherVideo.mov'],
      "url": "/api/v1/videos/"
    }
    """

    context = {}

    # url
    context["url"] = flask.request.path
    context["videos"] = listdir(media.app.config['UPLOAD_FOLDER'])

    return flask.jsonify(**context)
