from bottle import Bottle, run 
app = Bottle() 
@app.route('/') 
def home_page(): 
    return '23b01a12g0' 
if __name__ == '__main__': 
    run(app, host='localhost', port=8081)