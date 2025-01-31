from flask import Flask, render_template, request

app = Flask(__name__)

subscribed_emails = []  # Temporary email storage

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email')
    if email and email not in subscribed_emails:
        subscribed_emails.append(email)
        message = "Thank you for subscribing!"
    else:
        message = "You are already subscribed!"
    return render_template('contact.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
