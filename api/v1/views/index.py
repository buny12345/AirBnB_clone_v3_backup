from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "ok"})


@app_views.route('/stats', methods=['GET'])
def status():
    return jsonify({"status": "ok"})
