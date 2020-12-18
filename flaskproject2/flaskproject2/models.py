from flaskproject2 import db

class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(50), nullable=False)
	user_password = db.Column(db.String(50), nullable=False)
	user_age = db.Column(db.Integer, nullable=False)
	user_mobile_no = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"User(user_id={user_id},user_name = {user_name},user_password = {user_password}, user_age = {user_age}, user_mobile_no = {user_mobile_no})"


class Bus(db.Model):
	bus_id = db.Column(db.Integer, primary_key=True)
	bus_name = db.Column(db.String(50), nullable=False)
	bus_from = db.Column(db.String, nullable=False)
	bus_to = db.Column(db.String, nullable=False)
	bus_cost = db.Column(db.Integer, nullable=False)
	bus_seats = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Bus(bus_id={bus_id},bus_name = {bus_name},bus_from = {bus_from}, bus_to = {bus_to}, bus_cost = {bus_cost}, bus_seats={bus_seats})"

class Book(db.Model):
	booking_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String(50), nullable=False)
	bus_id = db.Column(db.String(50), nullable=False)
	book_tickets = db.Column(db.Integer, nullable=False)
	book_costs = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"User(booking_id={booking_id},user_id = {user_id},bus_id = {bus_id}, book_tickets = {book_tickets}, book_costs = {book_costs})"
