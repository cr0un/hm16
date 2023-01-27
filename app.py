import json
from flask import request
from db_init import app
from models import *
from utils import init_database


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        result = []
        for u in User.query.all():
            result.append(u.to_dict())
        return json.dumps(result), 200, {'Content-Type': 'application/json; '
                                                    'charset=utf-8'}
    if request.method == "POST":
        user_data = json.loads(request.data)

        db.session.add(
            User(
                id=user_data.get("id"),
                first_name=user_data.get("first_name"),
                last_name=user_data.get("last_name"),
                age=user_data.get("age"),
                email=user_data.get("email"),
                role=user_data.get("role"),
                phone=user_data.get("phone"),
            )
        )
        db.session.commit()
        return "", 201


@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def user(uid: int):
    if request.method == "GET":
        return json.dumps(User.query.get(uid).to_dict()), 200, {'Content-Type':
                                                 'application/json; '
                                                    'charset=utf-8'}
    if request.method == "PUT":
        user_data = json.loads(request.data)
        u = User.query.get(uid)
        u.first_name = user_data["first_name"]
        u.last_name = user_data["last_name"]
        u.age = user_data["age"]
        u.email = user_data["email"]
        u.role = user_data["role"]
        u.phone = user_data["phone"]

        db.session.add(u)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        u = User.query.get(uid)

        db.session.delete(u)
        db.session.commit()

        return "", 204


@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        result = []
        for o in Order.query.all():
            result.append(o.to_dict())
        return json.dumps(result), 200, {'Content-Type': 'application/json; '
                                                    'charset=utf-8'}
    if request.method == "POST":
        order_data = json.loads(request.data)

        db.session.add(
            Order(
                id=order_data.get("id"),
                name=order_data.get("name"),
                description=order_data.get("description"),
                start_date=order_data.get("start_date"),
                end_date=order_data.get("end_date"),
                address=order_data.get("address"),
                price=order_data.get("price"),
                customer_id=order_data.get("customer_id"),
                executor_id=order_data.get("executor_id")
            )
        )
        db.session.commit()
        return "", 201


@app.route("/orders/<int:uid>", methods=["GET", "PUT", "DELETE"])
def order(uid: int):
    if request.method == "GET":
        return json.dumps(Order.query.get(uid).to_dict()), 200, {'Content-Type':
                                                 'application/json; '
                                                    'charset=utf-8'}
    if request.method == "PUT":
        order_data = json.loads(request.data)
        u = Order.query.get(uid)

        u.name = order_data["name"]
        u.description = order_data["description"]
        u.start_date = order_data["start_date"]
        u.end_date = order_data["end_date"]
        u.address = order_data["address"]
        u.price = order_data["price"]
        u.customer_id = order_data["customer_id"]
        u.executor_id = order_data["executor_id"]

        db.session.add(u)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        u = Order.query.get(uid)

        db.session.delete(u)
        db.session.commit()

        return "", 204


@app.route("/offers", methods=["GET", "POST"])
def offers():
    if request.method == "GET":
        result = []
        for ofs in Offer.query.all():
            result.append(ofs.to_dict())
        return json.dumps(result), 200, {'Content-Type': 'application/json; '
                                                    'charset=utf-8'}

    if request.method == "POST":
        offer_data = json.loads(request.data)

        db.session.add(
            Offer(
                id=offer_data.get("id"),
                order_id=offer_data.get("order_id"),
                executor_id=offer_data.get("executor_id"),
            )
        )
        db.session.commit()
        return "", 201


@app.route("/offers/<int:uid>", methods=["GET", "PUT", "DELETE"])
def offer(uid: int):
    if request.method == "GET":
        return json.dumps(Offer.query.get(uid).to_dict()), 200, {'Content-Type':
                                                              'application/json; '
                                                    'charset=utf-8'}

    if request.method == "PUT":
        Offer_data = json.loads(request.data)
        u = Offer.query.get(uid)

        u.order_id = Offer_data["order_id"]
        u.executor_id = Offer_data["executor_id"]

        db.session.add(u)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        u = Offer.query.get(uid)

        db.session.delete(u)
        db.session.commit()

        return "", 204


if __name__ == '__main__':
    init_database()
    app.run(debug=True)