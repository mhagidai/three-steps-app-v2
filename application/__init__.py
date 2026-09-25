from flask import Flask


def create_app():
	"""Application factory to configure Flask instance."""
	app = Flask(__name__)
	app.config.from_object('config.Config')

	from .routes import main
	app.register_blueprint(main)

	return app