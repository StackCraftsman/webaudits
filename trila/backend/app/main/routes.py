from flask import session, redirect, url_for, render_template, request, jsonify
from . import main
from .forms import LoginForm
from datetime import datetime
from flask_socketio import SocketIO, emit
import base64
from .. import socketio
from .ai_audit import ux_audit

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('message', 'Hello client!', namespace='/')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    emit('message', 'bye client!', namespace='/')

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    emit('message', message, namespace='/')

@main.route('/snapshot', methods=['POST'])
def register_new():
    try:
        if 'user_photo' in request.files:
            photo = request.files['user_photo'].read()
        elif 'user_photo' in request.json:
            photo = base64.b64decode(request.json['user_photo'])
        else:
            return jsonify({'error': 'user_photo key not found in request'}), 400

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"snapshot/{timestamp}_compare.jpg"
        with open(filename, "wb") as file:
            file.write(photo)

        response = server_response(filename)
        socketio.emit('message', response, namespace='/')

        return jsonify({'message': 'done '})
    except Exception as e:
        return jsonify({'error': 'Failed to process request', 'details': str(e)}), 400

def server_response(image_path):
    response_generator = ux_audit(image_path)
    response = ''.join(response_generator)  # Consume the generator and join its contents into a single string
    return response
