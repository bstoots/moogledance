from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.update(
  DEBUG=True,
  SEND_FILE_MAX_AGE_DEFAULT=0
)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=80)
