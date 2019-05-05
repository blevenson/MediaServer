"""
Rangervid show view.

URLs include:
/show/
"""
import flask
import media
from media.views import webcrawler


@media.app.route('/show/<show_name>/', methods=['GET'])
def display_show(show_name):

    # Convert string to nice title format
    # game-of-thrones -> Game Of Thrones
    title = ''
    title += show_name[0].upper()
    i = 1
    while i < len(show_name):
        if show_name[i] == '-' and i < len(show_name) - 1:
            title += ' ' + show_name[i + 1].upper()
            i += 2
        else:
            title += show_name[i]
            i += 1

    context = {
        'title': title,
        'show_name': show_name,
        'seasons': webcrawler.get_episode_counts(show_name),
    }

    return flask.render_template("show.html", **context)
