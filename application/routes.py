from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
  return {
    'name':character.name,
    'age':character.age,
    'catch_phrase':character.catch_phrase
  }

@app.route('/')
def hello_world():
  return '<p>Hello World!!</p>'

@app.route('/characters', methods=['POST'])
def create_character():
  data = request.json
  character = FriendsCharacter(data['name'],data['age'],data['catch_phrase'])
  db.session.add(character)
  db.session.commit()
  return jsonify( id=character.id , name=character.name , age=character.age , catch_phrase=character.catch_phrase )
  return jsonify(error='Character couldn\'t be created'), 400


@app.route('/characters', methods=['GET'])
def get_characters():
  characters = FriendsCharacter.query.all()
  character_list = []
  for character in characters:
    character_list.append(format_character(character))
  return {'characters': character_list}

@app.route('/characters/<id>', methods=['GET'])
def get_character(id):
  character = FriendsCharacter.query.filter_by(id=id).first()
  return jsonify(id=character.id,name=character.name,age=character.age,catch_phrase=character.catch_phrase)

@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
  character = FriendsCharacter.query.filter_by(id=id).first()
  db.session.delete(character)
  db.session.commit()
  return 'Character deleted'

@app.route('/characters/<id>', methods=['PATCH'])
def update_character(id):
  character = FriendsCharacter.query.filter_by(id=id).first()
  data = request.json
  character.name = data['name']
  character.age = data['age']
  character.catch_phrase = data['catch_phrase']
  db.session.commit()
  updatedCharacter = character
  return jsonify(id=updatedCharacter.id,name=updatedCharacter.name,age=updatedCharacter.age,catch_phrase=updatedCharacter.catch_phrase)