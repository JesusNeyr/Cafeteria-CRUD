from flask import Flask,render_template
# from src.database.db_connection import connect
from src.routes.product_routes import product_bp
from flask_cors import CORS
import os
app = Flask(__name__, template_folder=os.path.join(os.getcwd(),'src/templates'),
            static_folder=os.path.join(os.getcwd(),'src/templates/static'))
#recien agregamos
CORS(app)
app.register_blueprint(product_bp)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)