from flask import Flask, render_template, request
import gen

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    passwords = []
    if request.method == 'POST':
        count = int(request.form.get('count', 5))
        length = int(request.form.get('length', 12))
        use_digits = 'digits' in request.form
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        use_special = 'special' in request.form
        
        passwords = gen.generate_password(count, length, use_digits, use_uppercase, use_lowercase, use_special)
    
    return render_template('index.html', passwords=passwords)

if __name__ == '__main__':
    app.run(host='192.168.0.0', port=5000)