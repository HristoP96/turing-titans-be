from quart import Quart, send_from_directory
from .routes.controller import audio_blueprint
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os

def create_app():
    app = Quart(__name__, static_folder="../static", static_url_path="/static/static")

    app.register_blueprint(audio_blueprint)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    async def catch_all(path):
        file_path = os.path.join(app.static_folder, path)
        if path != "" and os.path.exists(file_path):
            return await send_from_directory(app.static_folder, path)
        else:
            return await send_from_directory(app.static_folder, "index.html")

    scheduler = AsyncIOScheduler()
    scheduler.start()

    return app
