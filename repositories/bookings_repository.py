from db.run_sql import run_sql
from models.bookings import Bookings
from repositories import gym_class_repository
from repositories import members_repository

def save(booking):
    sql = "INSERT INTO bookings (members_id, classes_id) VALUES (%s, %s) RETURNING *"
    values = [booking.member.id, booking.gym_class.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id
    return booking

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = members_repository.select(row['members_id'])
        gym_class = gym_class_repository.select(row['classes_id'])
        booking = Bookings(member, gym_class, row['id'])
        bookings.append(booking)
    return bookings
# def create_booking(bookings):