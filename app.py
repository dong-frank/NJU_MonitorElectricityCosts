from flask import Flask, request, jsonify
from power_monitor import query_power

app = Flask(__name__)

@app.route('/power', methods=['GET'])
def get_power():
    bui_id = request.args.get('bui_id', 'gl11')
    bui_name = request.args.get('bui_name', '11舍')
    floor_id = request.args.get('floor_id', '002')
    floor_name = request.args.get('floor_name', '第2层')
    room_name = request.args.get('room_name', '204房间')
    room_id = request.args.get('room_id', '1111')
    remain = query_power(bui_id, bui_name, floor_id, floor_name, room_name, room_id)
    return jsonify({"remain": remain})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)