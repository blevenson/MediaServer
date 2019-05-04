"""
Rangervid show view.

URLs include:
/show/
"""
import flask
import media


@media.app.route('/show/<show_name>/', methods=['GET', 'POST'])
def display_show(show_name):

    # Check if post request to follow
    if flask.request.method == 'POST':
        # Insert them into database
        if 'like' in flask.request.form:
            # Like post
            data_base.execute(('INSERT INTO likes (owner, postid) ' +
                               'VALUES (\'%s\', %s)')
                              % (flask.session['username'],
                                 flask.request.form['postid']))
        elif 'unlike' in flask.request.form:
            # Unlike post
            data_base.execute(('DELETE FROM likes WHERE owner = \'%s\' ' +
                               'and postid = %s') %
                              (flask.session['username'],
                               flask.request.form['postid']))
        elif 'comment' in flask.request.form:
            # Add comment
            data_base.execute(('INSERT INTO comments (owner, postid, text) ' +
                               'VALUES (\'%s\', %s, \'%s\')') %
                              (flask.session['username'],
                               flask.request.form['postid'],
                               flask.request.form['text']))
        elif 'uncomment' in flask.request.form:
            # Delete comment
            data_base.execute(('DELETE FROM comments WHERE owner = \'%s\' ' +
                               'and commentid = %s') %
                              (flask.session['username'],
                               flask.request.form['commentid']))
        elif 'delete' in flask.request.form:
            # Delete post

            # Grab filename
            data_base.execute('SELECT * FROM posts WHERE postid = ' +
                              flask.request.form['postid'])
            delete_post = data_base.fetchone()

            # Check if they can delete the post
            if delete_post['owner'] == flask.session['username']:
                # Remove from db
                data_base.execute('DELETE FROM posts WHERE postid = %s' % (
                    flask.request.form['postid']))

                # Delete file from file system
                hash_filename = os.path.join(
                    insta485.app.config["UPLOAD_FOLDER"],
                    delete_post['filename']
                )
                os.remove(hash_filename)

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
    }

    return flask.render_template("show.html", **context)
