from flask import Flask, render_template

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return "<h1>Welcome to the Homepage!</h1>"

# Simulated error route for testing 500 error
@app.route('/cause500')
def cause_500():
    # This will cause a division by zero error, triggering a 500 error
    1 / 0
    return "This will never be returned."


# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
