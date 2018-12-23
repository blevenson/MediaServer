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
      "videos": [{
          "description": "Ranger next to kitchen table looking up.", 
          "file": "56694509373__7DAD3424-4D27-4B9F-B489-4F419F52FF2B.MOV", 
          "title": "Ranger Looking", 
          "videoid": 1, 
          "watched": 0
        }, 
        ],
      "url": "/api/v1/videos/"
    }
    """

    context = {}

    # url
    context["url"] = flask.request.path
    # context["videos"] = listdir(media.app.config['UPLOAD_FOLDER'])

    # Database
    db = media.model.get_db()

    cur = db.execute("SELECT * FROM videos",)
    output = cur.fetchall()

    context["videos"] = output

    return flask.jsonify(**context)
