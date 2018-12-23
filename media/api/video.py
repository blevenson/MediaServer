"""REST API for grabing/deleteing a video."""
import flask
import media
import os


@media.app.route('/api/v1/video/<int:video_id>/', methods=["GET", "DELETE"])
def get_video(video_id):
    """Return metadata on videoid.

    Example:
    {
      "description": "Ranger next to kitchen table looking up.", 
      "file": "56694509373__7DAD3424-4D27-4B9F-B489-4F419F52FF2B.MOV", 
      "title": "Ranger Looking", 
      "url": "/api/v1/video/1/", 
      "videoid": 1, 
      "watched": 1
    }
    """

    # User
    context = {}

    # Database
    connection = media.model.get_db()

    cur = connection.execute(
        "  SELECT * FROM videos WHERE videoid = ? ",
        (video_id, )
    )
    context = cur.fetchone()

    if flask.request.method == 'DELETE':
        # Delete post

        # Remove from db
        connection.execute('DELETE FROM videos WHERE videoid = %s' % (
            str(video_id)))

        # Delete file from file system
        hash_filename = os.path.join(
            media.app.config["UPLOAD_FOLDER"],
            context['file']
        )
        os.remove(hash_filename)

        return flask.jsonify(), 204

    # url
    if not context:
        context = {}
        context["Error"] = "Video id not in database"

    context["url"] = flask.request.path

    return flask.jsonify(**context)
