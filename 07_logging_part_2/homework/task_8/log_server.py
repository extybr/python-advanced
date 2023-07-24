from flask import Flask, request

app = Flask(__name__)


@app.route('/log', methods=['POST'])
def log_post():
    msg = (f"{request.form['name']} | {request.form['levelname']} | "
           f"{request.form['asctime']} | {request.form['levelno']} | "
           f"{request.form['message']}")

    ip = request.remote_addr
    with open(f'{ip}_calc.log', 'a') as text:
        text.write(msg + '\n')

    print(msg)

    return 'OK', 200


@app.route('/log', methods=['GET'])
def log_get():
    ip = request.remote_addr
    with open(f'{ip}_calc.log', 'r') as text:
        html = '<html><h3><ul>'
        for line in text.readlines():
            if line.find('ERROR') != -1:
                html += f"<li><font color='red'>{line}</font></li>"
            else:
                html += f"<li>{line}</li>"
        return html + '</ul></h3></html>'


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(host='127.0.0.1', port=5000, debug=True)
