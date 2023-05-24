from flask import Flask, render_template, request, jsonify
import csv
import socket
import time
import decipher


def obter_endereco_ip():
    hostname = socket.gethostname()
    endereco_ip = socket.gethostbyname(hostname)
    return endereco_ip


print("Endereço IP:", obter_endereco_ip())
app = Flask(__name__)


with open('templates/index.html', 'r') as file:
    html_content = file.read()

with open('templates/test.html', 'r') as file:
    test = file.read()

with open('templates/login.html', 'r') as file:
    login = file.read()


ip_list = []


def set_ip_id(ip):
    ip_list.append(ip)


@app.route('/')
def login_():

    return f"{login}"


@app.route('/validation', methods=['POST'])
def validation():
    valor_input = request.form['password-input']
    current_time = time.gmtime()
    print(valor_input)
    return f"{login}"


@app.route('/receive-login', methods=['POST'])
def receive_info():
    data = request.get_json()  # Retrieve JSON data from the request
    # Process the received data as needed
    data = data
    print("Received data:", data)

    return "Data received successfully"


@app.route('/index', methods=['POST'])
def index():

    client_ip = request.remote_addr
    set_ip_id(client_ip)
    return f"{html_content}"


@app.route('/processar', methods=['POST'])
def processar():
    valor_input = request.form['campo_input']
    print("request")
    with open("recent_submissions.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        client_ip = request.remote_addr
        print(client_ip)
        # Write the data to the CSV file
        current_time = time.gmtime()
        writer.writerow([f"{client_ip}", f"{valor_input}", [current_time.tm_year, current_time.tm_mon,
                                                            current_time.tm_mday, current_time.tm_hour,
                                                            current_time.tm_min, current_time.tm_sec,
                                                            current_time.tm_wday, current_time.tm_yday,
                                                            current_time.tm_isdst]])
    file.close()
    print("Valor do input:", valor_input)

    return "Valor do input: " + valor_input + f"{html_content}"


@app.route('/test', methods=['POST'])
def testing():
    return f"{test}"


@app.route('/screen-size')
def screen_size():
    data = request.get_json()
    width = data['width']
    height = data['height']
    print(width, height)
    # Perform any desired processing with the screen size data

    return jsonify({'message': 'Screen size received successfully'})


if __name__ == '__main__':
    app.run(host='2804:5da8:bb20:e066:5493:7f49:2ee2:a033', port=80)

