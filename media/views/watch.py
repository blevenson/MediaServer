"""
Rangervid watch view.

URLs include:
/watch/
"""
import flask
import media
from media.views import webcrawler


@media.app.route('/watch/<show_params>/', methods=['GET'])
def watch_show(show_params):
    # Grab data from url
    params = show_params.split('-')
    season = params[-2]
    episode = params[-1]

    show_name = '-'.join(params[:-2])

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
        'season': season,
        'episode': episode,
        'source': webcrawler.get_episode_counts(show_name, season, episode),
    }

    return flask.render_template("watch.html", **context)
