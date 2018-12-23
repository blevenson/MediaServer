"""
Media server index (main) view.

URLs include:
/
"""
import arrow
import flask
import media
import os
import shutil
import tempfile
import uuid
import hashlib
import flask


@media.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Display / route."""
    context = {
    }

    return flask.render_template("index.html", **context)


@media.app.route('/upload/', methods=['GET', 'POST'])
def show_upload():
    """Display upload dir."""
    context = {
    }

    if flask.request.method == 'POST':

        # Get Database
        cursor = media.model.get_db().cursor()

        # Save POST request file object to temp file
        dummy, temp_filename = tempfile.mkstemp()
        file = flask.request.files["file"]
        file.save(temp_filename)

        # Compute the file name
        dummy, suffix = os.path.splitext(file.filename)
        hash_filename_basename = sha256sum(temp_filename) + suffix
        hash_filename = os.path.join(
            media.app.config["UPLOAD_FOLDER"], hash_filename_basename)

        # Move temp file to permanent location
        shutil.move(temp_filename, hash_filename)

        # Store all data in db
        cursor.execute(('INSERT INTO videos (title, description, file, watched) ' +
                        'VALUES (\'%s\', \'%s\', \'%s\', 0)')
                       % (flask.request.form['title'],
                          flask.request.form['description'],
                          hash_filename_basename))

    context = {}

    return flask.render_template("upload.html", **context)


@media.app.route('/uploads/<path:filename>')
def download_file(filename):
    """Download the file."""
    return flask.send_from_directory(media.app.config['UPLOAD_FOLDER'],
                                     filename, as_attachment=True)


def sha256sum(filename):
    """Return sha256 hash of file content, similar to UNIX sha256sum."""
    content = open(filename, 'rb').read()
    sha256_obj = hashlib.sha256(content)
    return sha256_obj.hexdigest()
