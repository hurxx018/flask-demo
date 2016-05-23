from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.vars = {}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET', 'POST'])
def index():
  return render_template('index.html', question='Ticker symbol: ')

if __name__ == '__main__':
  app.run(port=33507, debug=True)
  # debug is disabled.
  # app.run(host='0.0.0.0') # The operating system listens on all public IPs.
