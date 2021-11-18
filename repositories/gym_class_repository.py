from db.run_sql import run_sql
from models.gym_class import Gym_Class


def save(gym_class):
    sql = "INSERT INTO class_list (name, spaces, capacity, id) VALUES (%s. %s, %s, %s) RETURNING *"
    values = [gym_class.name, gym_class.spaces, gym_class.capacity, gym_class.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id
    return gym_class

def select_all():
    class_list = []
    sql = "SELECT * FROM gym_class"
    results = run_sql(sql)

    for row in results:
        gym_class = Gym_Class(row['name'], row['spaces'] ,row['capacity'], row['id'])
        class_list.append(gym_class)
    return class_list

def select(id):
    gym_class = None

    sql = "SELECT * FROM gym_class WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Gym_Class(result['name'], result['spaces'] ,result['capacity'], result['id'])
    return gym_class
