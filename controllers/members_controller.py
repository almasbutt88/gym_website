from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.members import Members
import repositories.gym_class_repository as gym_class_repository
import repositories.members_repository as members_repository
import repositories.bookings_repository as bookings_repository



members_blueprint = Blueprint("members", __name__)

@members_blueprint.route('/members')
def members_list():
    members_list = members_repository.select_all()

    return render_template('members/index.html', members_list = members_list)

# EDIT / 
# GET '/classes/<id>'
@members_blueprint.route('/members/<id>', methods = ['GET'])
def select(id):
    members_list = members_repository.select(id)
    gym_class = gym_class_repository.select(id)
    return render_template('/members/show.html', members_list = members_list, gym_class = gym_class)


@members_blueprint.route("/members/new",  methods=['POST'])
def create_member():
    name = request.form['name']
    age = request.form['age']
    member = Members(name, age)

    members_repository.save(member)
    return redirect("/members")
