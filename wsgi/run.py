from app import app

@app.route('/')
@app.route('/a')
@app.route('/index')
def hello():
    return 'Hello World!!!!!!'

if __name__ == "__main__":
    app.run()
