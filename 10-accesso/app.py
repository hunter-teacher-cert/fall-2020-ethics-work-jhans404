from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
app.config['SQLALCHEMY_BINDS'] = {'clues' : 'sqlite:///clues.db'}

# Initialize the database
db = SQLAlchemy(app)

# Create db model for Players
class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Integer, default=0)
    # Create a function to return a string when we add someone
    #def __repr__(self):
        #return '<Name %r>' % self.id

# Create db model for the clues
class Clues(db.Model):
    __bind_key__ = 'clues'
    id = db.Column(db.Integer, primary_key=True)
    clue = db.Column(db.String(100), nullable=False)
    question = db.Column(db.String(100), nullable=False)
    # Create a function to return a string when we add someone
    #def __repr__(self):
        #return '<Name %r>' % self.id

# Set up variables for looks accessibility
color_mode = 'static/css/light.css'
text_size = 'static/css/size30.css'

#players = []

@app.route('/')
def index():
    return render_template("index.html", color_mode=color_mode, text_size=text_size)

@app.route('/about')
def about():
    return render_template("about.html", color_mode=color_mode, text_size=text_size)

@app.route('/start', methods=["GET", "POST"])
def start():
    if request.method == "POST":
        #username = request.form.get("username")
        #players.append(username)
        player_name = request.form['name']
        new_player = Players(name=player_name)

        # Push to database
        try:
            db.session.add(new_player)
            db.session.commit()
            return redirect('/start')
        except:
            return "Doh! Player database add error."
    else:
        players = Players.query.order_by(Players.id)
        return render_template("start.html", players=players, color_mode=color_mode, text_size=text_size)

@app.route('/delete/<int:id>')
def delete(id):
    player_to_delete = Players.query.get_or_404(id)
    try:
        db.session.delete(player_to_delete)
        db.session.commit()
        return redirect('/start')
    except:
        return "Problem deleting that player from the database =("

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    player_to_update = Players.query.get_or_404(id)
    if request.method == "POST":
        player_to_update.name = request.form['name']
        try:
            db.session.commit()
            return redirect('/start')
        except:
            return "Problem updating that player in the database =("
    else:
        return render_template("update.html", player_to_update=player_to_update)

@app.route('/incScore/<int:id>')
def incScore(id):
    player_to_increase = Players.query.get_or_404(id)
    player_to_increase.score += 1
    try:
        db.session.commit()
        return redirect('/jeopardy')
    except:
        return "Problem incrementing that player's score in the database =("

@app.route('/decScore/<int:id>')
def decScore(id):
    player_to_decrease = Players.query.get_or_404(id)
    player_to_decrease.score -= 1
    try:
        db.session.commit()
        return redirect('/jeopardy')
    except:
        return "Problem decrementing that player's score in the database =("

@app.route('/clues', methods=["GET", "POST"])
def clues():
    if request.method == "POST":
        #username = request.form.get("username")
        #players.append(username)
        clue = request.form['clue']
        question = request.form['question']
        new_clue = Clues(clue=clue, question=question)

        # Push to database
        try:
            db.session.add(new_clue)
            db.session.commit()
            return redirect('/clues')
        except:
            return "Doh! Clue database add error."
    else:
        clues = Clues.query.order_by(Clues.id)
        return render_template("clues.html", clues=clues, color_mode=color_mode, text_size=text_size)

@app.route('/deleteClue/<int:id>')
def deleteClue(id):
    clue_to_delete = Clues.query.get_or_404(id)
    try:
        db.session.delete(clue_to_delete)
        db.session.commit()
        return redirect('/clues')
    except:
        return "Problem deleting that clue from the database =("

@app.route('/updateClue/<int:id>', methods=['POST', 'GET'])
def updateClue(id):
    clue_to_update = Clues.query.get_or_404(id)
    if request.method == "POST":
        clue_to_update.clue = request.form['clue']
        clue_to_update.question = request.form['question']
        try:
            db.session.commit()
            return redirect('/clues')
        except:
            return "Problem updating that clue in the database =("
    else:
        return render_template("updateClue.html", clue_to_update=clue_to_update, text_size=text_size)


@app.route('/jeopardy')
def jeopardy():
    players = Players.query.order_by(Players.id)
    clues = Clues.query.order_by(Clues.id)
    return render_template("jeopardy.html", players=players, clues=clues, color_mode=color_mode, text_size=text_size)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
