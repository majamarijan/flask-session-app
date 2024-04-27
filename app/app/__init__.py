from flask import Flask, session, render_template, url_for, redirect, request,jsonify

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    @app.get('/')
    def index():
        username=''
        if session.get('username'):
            username=session['username']
        print(session.get('username'))
        return render_template('index.html', username=username, title='Session App')

    @app.get('/about')
    def about():
        print(session.get('username'))
        return render_template('about.html', title='About')

    @app.get('/login')
    def login():
        return render_template('form.html', title="Login")

    @app.post('/submit')
    def submit():
        data = request.json
        if data.get('username') != '' and data.get('password') != '':
            checked = True
            if checked:
                session['username'] = data.get('username')
                print(request.json)
                return jsonify({"message":"OK"})

    @app.get('/submit')
    def after_submit():
        return redirect(url_for('index'))

    @app.get('/logout')
    def logout():
        data=''
        if session.get('username'):
            session.pop('username',default=None)
        return redirect(url_for('index'))

    if __name__ == "__main__":
        app.run()

    return app


