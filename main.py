from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		users = ['Kassem_m31', 'Adham', 'Seif', 'Ahmed Eid']
		passwords = ['313546', '123456']
		if username in users and password in passwords:
			return redirect(url_for('main'))
	return render_template('Chat-Room Login.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		msg = request.form['message']
		with open('messages.txt', 'a+') as file:
			file.write(f"{msg}\n")
			file.close()
		with open('messages.txt', 'r') as file:
			saved_msg = file.read()
			file.close()

		return render_template('Chat-Room.html', message=saved_msg)
	with open('messages.txt', 'r') as file:
		saved_msg = file.read()
	return render_template('Chat-Room.html', message=saved_msg)

if __name__ == '__main__':
	app.run(debug=True, port=8000)