from flask import Blueprint, jsonify, request

from services import (
    get_price_data,
    get_events,
    get_change_points,
    get_dashboard_metrics,
    get_prices_between,
    get_event,
)

api = Blueprint("api", __name__)


@api.route("/prices", methods=["GET"])
def prices():
    return jsonify(get_price_data())


@api.route("/events", methods=["GET"])
def events():
    return jsonify(get_events())


@api.route("/change-points", methods=["GET"])
def change_points():
    return jsonify(get_change_points())



@api.route("/kpis")
def kpis():

    start = request.args.get("start")
    end = request.args.get("end")

    return jsonify(
        get_dashboard_metrics(start, end)
    )

@api.route("/price-range", methods=["GET"])
def price_range():
    start = request.args.get("start")
    end = request.args.get("end")

    if not start or not end:
        return jsonify(
            {"error": "Please provide start and end query parameters."}
        ), 400

    return jsonify(get_prices_between(start, end))


@api.route("/event/<int:event_id>", methods=["GET"])
def event(event_id):
    result = get_event(event_id)

    if result is None:
        return jsonify({"error": "Event not found"}), 404

    return jsonify(result)