from quart import Blueprint, request, jsonify
from quart_cors import cors


audio_blueprint = Blueprint('audio', __name__)
audio_blueprint = cors(audio_blueprint, allow_origin="*", allow_methods=['GET', 'POST', 'OPTIONS'])

@audio_blueprint.route('/upload', methods=['POST'])
async def upload_chunk():
    return {'success': 'true'}, 200
    
@audio_blueprint.route('/complete-upload', methods=['POST'])
async def complete_file_upload():
    return {'success': 'true'}, 200


@audio_blueprint.route('/under-conversion', methods=['GET'])
def get_under_conversion():
    return {'success': 'true'}, 200


@audio_blueprint.route('/files-info', methods=['GET'])
def get_files_info():
    return {'success': 'true'}, 200
