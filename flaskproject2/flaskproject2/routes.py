from flaskproject2 import api,db
from flaskproject2.models import User,Bus,Book
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with


user_put_args = reqparse.RequestParser()
user_put_args.add_argument("user_name", type=str, help="Username of user is required", required=True)
user_put_args.add_argument("user_password", type=str, help="Password of user is required", required=True)
user_put_args.add_argument("user_age", type=int, help="age of user is required", required=True)
user_put_args.add_argument("user_mobile_no", type=int, help="mobile number of user is required", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("user_name", type=str, help="Username of user is required")
user_update_args.add_argument("user_password", type=str, help="Password of user is required")
user_update_args.add_argument("user_age", type=int, help="age of user is required")
user_update_args.add_argument("user_mobile_no", type=int, help="mobile number of user is required")

resource_fields1 = {
	'user_id': fields.Integer,
	'user_name': fields.String,
	'user_password': fields.String,
	'user_age': fields.Integer,
	'user_mobile_no': fields.Integer
}

bus_put_args = reqparse.RequestParser()
bus_put_args.add_argument("bus_name", type=str, help="name of bus is required", required=True)
bus_put_args.add_argument("bus_from", type=str, help="from location is required", required=True)
bus_put_args.add_argument("bus_to", type=str, help="to location is required", required=True)
bus_put_args.add_argument("bus_cost", type=int, help="bus cost is required", required=True)
bus_put_args.add_argument("bus_seats", type=int, help="no of seats is required", required=True)

bus_update_args = reqparse.RequestParser()
bus_update_args.add_argument("bus_name", type=str, help="name of bus is required")
bus_update_args.add_argument("bus_from", type=str, help="from location is required")
bus_update_args.add_argument("bus_to", type=str, help="to location is required")
bus_update_args.add_argument("bus_cost", type=int, help="bus cost is required")
bus_update_args.add_argument("bus_seats", type=int, help="no of seats is required")

resource_fields2 = {
	'bus_id': fields.Integer,
	'bus_name': fields.String,
	'bus_from': fields.String,
	'bus_to': fields.String,
	'bus_cost': fields.Integer,
	'bus_seats': fields.Integer
}

book_put_args = reqparse.RequestParser()
book_put_args.add_argument("bus_id", type=int, help="id of bus is required", required=True)
book_put_args.add_argument("user_id", type=int, help="id of user is required", required=True)
book_put_args.add_argument("book_tickets", type=int, help="no of tickets is required", required=True)

resource_fields3 = {
	'booking_id': fields.Integer,
	'bus_id': fields.Integer,
	'user_id': fields.Integer,
	'book_tickets': fields.Integer,
	'book_costs': fields.Integer
}

class User_rest(Resource):
	@marshal_with(resource_fields1)
	def get(self, user_id):
		result = User.query.filter_by(user_id=user_id).first()
		if not result:
			abort(404, message="Could not find user with that id")
		return result

	@marshal_with(resource_fields1)
	def put(self, user_id):
		args = user_put_args.parse_args()
		result = User.query.filter_by(user_id=user_id).first()
		if result:
			abort(409, message="user id already exists...")
		users = User(user_id=user_id, user_name=args['user_name'], user_password=args['user_password'], user_age=args['user_age'], user_mobile_no=args['user_mobile_no'])
		db.session.add(users)
		db.session.commit()
		return users, 201

	@marshal_with(resource_fields1)
	def patch(self, user_id):
		args = user_update_args.parse_args()
		result = User.query.filter_by(user_id=user_id).first()
		if not result:
			abort(404, message="user doesn't exist. So, cannot update")
		if args['user_name']:
			result.user_name = args['user_name']
		if args['user_password']:
			result.user_password = args['user_password']
		if args['user_age']:
			result.user_age = args['user_age']
		if args['user_mobile_no']:
			result.user_mobile_no = args['user_mobile_no']
		db.session.commit()
		return result

	def delete(self, user_id):
		result = User.query.filter_by(user_id=user_id).first()
		if result is None:
			abort(404, message= "user doesn't exist")
		db.session.delete(result)
		db.session.commit()
		return "", 204

class Bus_rest(Resource):
	@marshal_with(resource_fields2)
	def get(self, bus_id):
		result = Bus.query.filter_by(bus_id=bus_id).first()
		if not result:
			abort(404, message="Could not find bus with that id")
		return result

	@marshal_with(resource_fields2)
	def put(self, bus_id):
		args = bus_put_args.parse_args()
		result = Bus.query.filter_by(bus_id=bus_id).first()
		if result:
			abort(409, message="bus id already exists...")
		busses = Bus(bus_id=bus_id, bus_name=args['bus_name'], bus_from=args['bus_from'], bus_to=args['bus_to'], bus_cost=args['bus_cost'], bus_seats=args['bus_seats'])
		db.session.add(busses)
		db.session.commit()
		return busses, 201

	@marshal_with(resource_fields2)
	def patch(self, bus_id):
		args = bus_update_args.parse_args()
		result = Bus.query.filter_by(bus_id=bus_id).first()
		if not result:
			abort(404, message="bus doesn't exist. So, cannot update")
		if args['bus_name']:
			result.bus_name = args['bus_name']
		if args['bus_from']:
			result.bus_from = args['bus_from']
		if args['bus_to']:
			result.bus_to = args['bus_to']
		if args['bus_cost']:
			result.bus_cost = args['bus_cost']
		if args['bus_seats']:
			result.bus_seats = args['bus_seats']
		db.session.commit()
		return result

	def delete(self, bus_id):
		result = Bus.query.filter_by(bus_id=bus_id).first()
		if result is None:
			abort(404, message= "bus doesn't exist")
		db.session.delete(result)
		db.session.commit()
		return "", 204

class Book_rest(Resource):
	@marshal_with(resource_fields3)
	def get(self, booking_id):
		result = Book.query.filter_by(booking_id=booking_id).first()
		if not result:
			abort(404, message="Could not find booking with that id")
		return result

	@marshal_with(resource_fields3)
	def put(self, booking_id):
		args = book_put_args.parse_args()
		result = Book.query.filter_by(booking_id=booking_id).first()
		if result:
			abort(409, message="booking id already exists...")
		users=User.query.filter_by(user_id=args['user_id']).first()
		busses=Bus.query.filter_by(bus_id=args['bus_id']).first()
		if not users:
			abort(404, message="Could not find user with that id")
		if not busses:
			abort(404, message="Could not find bus with that id")
		if busses.bus_seats<args['book_tickets']:
			abort(404, message="Tickets not available")
		busses.bus_seats-=args['book_tickets']
		bookings = Book(booking_id=booking_id, bus_id=args['bus_id'], user_id=args['user_id'], book_tickets=args['book_tickets'], book_costs=busses.bus_cost*args['book_tickets'])
		db.session.add(bookings)
		db.session.commit()
		return bookings, 201

	def delete(self, booking_id):
		result = Book.query.filter_by(booking_id=booking_id).first()
		if result is None:
			abort(404, message= "booking doesn't exist")
		tickets_booked=result.book_tickets
		busses=Bus.query.filter_by(bus_id=result.bus_id).first()
		busses.bus_seats+=tickets_booked
		db.session.delete(result)
		db.session.commit()
		return "", 204

api.add_resource(User_rest, "/user/<int:user_id>")
api.add_resource(Bus_rest, "/bus/<int:bus_id>")
api.add_resource(Book_rest, "/book/<int:booking_id>")