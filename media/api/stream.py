"""REST API for streaming videos."""
import sqlite3
import flask
import media
import requests


@media.app.route('/api/v1/search/', methods=["POST"])
def search_shows():
    """Search for the show online."""

    context = {}

    # url
    context["url"] = flask.request.path

    # Check if post request
    if flask.request.method == 'POST':
        # Grab show search from post request
        show_name = flask.request.json['title']

        search_url = 'http://www.watchepisodeseries.com/home/search?q=' + \
            show_name.replace(' ', '+')

        # Search for video
        response = requests.get(search_url)
        results = response.json()['series']

        context['series'] = results

        return flask.jsonify(**context)

    return flask.jsonify(**context)
