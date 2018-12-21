"""
Media server index (main) view.

URLs include:
/
"""
import arrow
import flask
import media


@media.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Display / route."""
    context = {
    }
	
    return flask.render_template("index.html", **context)


@media.app.route('/uploads/<path:filename>')
def download_file(filename):
    """Download the file."""
    return flask.send_from_directory(media.app.config['UPLOAD_FOLDER'],
                                     filename, as_attachment=True)
