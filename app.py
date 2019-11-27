from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
import os
from flask_marshmallow import Marshmallow 


#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#inti db
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#init mashmallow
ma = Marshmallow(app)


#billioner model
class WorldCup(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	year = db.Column(db.Integer, unique=True)
	host = db.Column(db.String(100))
	champion = db.Column(db.String(100))
	runner_up = db.Column(db.String(100))
	third_place = db.Column(db.String(100)) 
	teams = db.Column(db.Integer)
	matches_played = db.Column(db.Integer)
	goal_scored = db.Column(db.Integer)
	avg_goals_per_game = db.Column(db.Float)

	def __init__(self, year, host, champion, runner_up, third_place, teams, matches_played, goal_scored, avg_goals_per_game):
    		self.year = year
    		self.host = host
    		self.champion = champion
    		self.runner_up = runner_up
    		self.third_place = third_place
    		self.teams = teams
    		self.matches_played = matches_played
    		self.goal_scored = goal_scored
    		self.avg_goals_per_game = avg_goals_per_game	

# schema
class WorldCupSchema(ma.Schema):
  class Meta:
    fields = ('id','year', 'host', 'champion', 'runner_up', 'third_place', 'teams', 'matches_played', 'goal_scored', 'avg_goals_per_game')

# Init schema
worldcup_schema = WorldCupSchema()
worldscup_schema = WorldCupSchema(many=True)
    	
@app.route('/world_cup', methods=['POST'])
def add_cup():
	year = request.json['year']
	host = request.json['host']
	champion = request.json['champion']
	runner_up = request.json['runner_up']
	third_place = request.json['thirds']
	teams = request.json['teams']
	matches_played = request.json['matches']
	goal_scored = request.json['goals']
	avg_goals_per_game = request.json['avg']

	newC = WorldCup(year, host, champion, runner_up, third_place, teams, matches_played, goal_scored, avg_goals_per_game)
	
	
	db.session.add(newC)
	db.session.commit()

	return worldcup_schema.jsonify(newC)



@app.route('/world_cup')
def get_all_cup():
	cup = WorldCup.query.all()
	result = worldscup_schema.dump(cup)

	#print(billionaires[0])
	return jsonify(result)

#methods get for id,rank,name

#get cup for year
@app.route('/world_cup/<int:year>')
def get_cut_year(year):
	cup = WorldCup.query.filter_by(year=year).first_or_404()
	r = worldcup_schema.dump(cup)
	if cup:
		return jsonify(r)
	else:
		return jsonify({"Error 404":"Not found"})

#method delete
@app.route('/world_cup/<int:id>', methods=['DELETE'])
def delete_cup(id):
	cup = WorldCup.query.get_or_404(id)
	db.session.delete(cup)
	db.session.commit()

	return worldcup_schema.jsonify(cup)













#run server
if  __name__ == '__main__':
	app.run(debug=True)