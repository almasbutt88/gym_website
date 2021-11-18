from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.gym_class_repository as gym_class_repository
import repositories.members_repository as members_repository



gym_class_blueprint = Blueprint("gym_class", __name__)

@gym_class_blueprint.route('/classes')
def class_list():
    class_list = gym_class_repository.select_all()

    return render_template('classes/index.html', class_list = class_list)

# EDIT / 
# GET '/classes/<id>'
@gym_class_blueprint.route('/classes/<id>', methods = ['GET'])
def select(id):
    gym_class = gym_class_repository.select(id)
    member = members_repository.select(id)
    return render_template('/classes/show.html', gym_class = gym_class, member = member)

# @bookings_blueprint.route("/bookings",  methods=['POST'])
# def create_booking():
#     member = request.form['member']
#     gym_class = request.form['gym_class']
#     member = members_repository.select(member)
#     gym_class = gym_class_repository.select(gym_class)
#     bookings = Bookings(member, gym_class)




# # NEW
# # GET '/classes/new'

# # CREATE
# # POST '/'
# @gym_class_blueprint.route("/classes",  methods=['POST'])
# def create_booking():
  

#     return redirect('/')


# # SHOW
# # GET '/tasks/<id>'
# @tasks_blueprint.route("/tasks/<id>", methods=['GET'])
# def show_task(id):
#     task = task_repository.select(id)
#     return render_template('tasks/show.html', task = task)



# # DELETE
# # DELETE '/tasks/<id>'
# @tasks_blueprint.route("/tasks/<id>/delete", methods=['POST'])
# def delete_task(id):
#     task_repository.delete(id)
#     return redirect('/tasks')
