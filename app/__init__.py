from flask import Flask, session, render_template, url_for, redirect, request,jsonify, make_response

visitedCounter=0

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    
    @app.get('/')
    def index():
        if 'Visited' in request.cookies:
            visited = int(request.cookies.get('Visited'))+1
        else:
            visited=visitedCounter+1
        username=''
        # if 'username' in session
        if session.get('username'):
            username=session['username']
        # print(session.get('username'))
        res = make_response(render_template('index.html', username=username, title='Session App'))
        res.set_cookie('Visited', str(visited) , max_age=3600, secure=True, httponly=True)
        return res

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
        try:
            if data.get('username') != '' and data.get('password') != '':
                session['username'] = data.get('username')
                print(request.json)
                return jsonify({"message":"OK"})
        except ValueError:
            return 'Something went wrong'

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


