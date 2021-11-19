from db.run_sql import run_sql
from models.members import Members

def save(member):
    sql = "INSERT INTO members (name, age, id) VALUES (%s, %s, %s) RETURNING *"
    values = [member.name, member.age, member.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member


def select_all():
    members_list = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        gym_member = Members(row['name'], row['age'], row['id'] )
        members_list.append(gym_member)
    return members_list


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = Members(result['name'], result['age'], result['id'] )
    return member



def update(members):
    sql = "UPDATE members SET (name, age) = (%s, %s) WHERE id = %s"
    values = [members.name, members.age, members.id]
    run_sql(sql, values)


