from flask import Flask, session, render_template, url_for, redirect, request,jsonify, make_response
from .utils import generateID, findUser

visitedCounter=0
users=[]

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
        print(session)
        print(users)
        if len(users) > 0:
            # username=findUser(session.get('session_id'),users)
            for user in users:
                if user['session_id'] == session.get('session_id'):
                 username=user['username']
        res = make_response(render_template('index.html', username=username, title='Session App'))
        res.set_cookie('Visited', str(visited) , max_age=3600, secure=True, httponly=True)
        return res

    @app.get('/about')
    def about():
        return render_template('about.html', title='About')

    @app.get('/login')
    def login():
        return render_template('form.html', title="Login")

    @app.post('/submit')
    def submit():
        data = request.json
        try:
            if data.get('username') != '' and data.get('password') != '':
                user_id = generateID(data.get('username'))
                session['session_id']=generateID(user_id)
                users.append({"username":data.get('username'), "password":data.get('password'), "user_id":user_id, "session_id":session.get('session_id')})
                return jsonify({"message":"OK"})
        except ValueError:
            return 'Something went wrong'

    @app.get('/submit')
    def after_submit():
        return redirect(url_for('index'))

    @app.get('/logout')
    def logout():
        data=''
        if session.get('session_id'):
            for user in users:
                if user['session_id'] == session.get('session_id'):
                    users.remove(user)
                    session.pop('session_id',default=None)
        return redirect(url_for('index'))

    if __name__ == "__main__":
        app.run()

    return app


