from quart import Blueprint, request, jsonify
from quart_cors import cors
from ..openais.gpt import start_game, select_option

audio_blueprint = Blueprint('game', __name__)
audio_blueprint = cors(audio_blueprint, allow_origin="*", allow_methods=['GET', 'POST', 'OPTIONS'])

@audio_blueprint.route('/select-option', methods=['POST'])
async def option():
    form = await request.form
    thread_id = form['thread_id']
    option = form['option']

    return jsonify(select_option(option, thread_id)), 200

@audio_blueprint.route('/start-game', methods=['POST'])
def start():
    return jsonify(start_game()), 200
