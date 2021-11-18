from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_Class
from models.members import Members
from models.bookings import Bookings
import repositories.gym_class_repository as gym_class_repository
import repositories.members_repository as members_repository
import repositories.bookings_repository as bookings_repository




bookings_blueprint = Blueprint("bookings", __name__)


@bookings_blueprint.route("/bookings")
def bookings():
    bookings = bookings_repository.select_all() # NEW
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_class():
    class_list = gym_class_repository.select_all()
    members_list = members_repository.select_all()
    return render_template("bookings/new.html", class_list = class_list, members_list = members_list)


@bookings_blueprint.route("/bookings",  methods=['POST'])
def create_booking():
    member = request.form['member']
    gym_class = request.form['gym_class']
    member = members_repository.select(member)
    gym_class = gym_class_repository.select(gym_class)
    bookings = Bookings(member, gym_class)

    bookings_repository.save(bookings)
    return redirect("/bookings")