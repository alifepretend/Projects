import csv
import time
import requests
from bs4 import BeautifulSoup
import decipher


def get_identity(ip):
    with open("ip_list.csv", mode='r', newline='') as identities:
        reader = csv.reader(identities)
        identity = None
        for line in reader:
            if ip == line[0]:
                identity = line
    identities.close()
    return identity


def get_html_info(word):
    # Fazer uma requisição GET para a página
    url = f'https://dicionario.priberam.org/{word}'  # Substitua com a URL da página que deseja buscar
    response = requests.get(url)
    classe = 0
    if response.status_code == 200:
        # Ler o conteúdo da página
        conteudo = response.text

        # Criar um objeto BeautifulSoup
        soup = BeautifulSoup(conteudo, 'html.parser')
        div = soup.find(id='resultados')
        # print(div)
        if div is not None:
            # Encontrar todas as tags que possuem a classe desejada
            defheader = div.find_all(class_='defheader')
            classes = div.find_all(class_='varpt')
            classe = div.find_all(style='color: #1483ff')
            verbeteh = div.find_all(class_="verbeteh1")


        # print(verbeteh)
        possibilidades = []
        if classe:
            for i in classe:
                possibilidades.append(i.text)
            print(possibilidades, word)
            return [word, possibilidades]
    else:
        print('Falha ao buscar a página:', response.status_code)


def analize_message(text):
    word_list = text.split(" ")
    info = []
    for word in word_list:
        info.append(get_html_info(word))
    print(info)
    return info


last_lines = None

while True:
    with open("recent_submissions.csv", mode='r', newline='') as file:
        writer = csv.reader(file)
        i = 0
        lines = []
        for line in writer:
            if i != 0:
                if len(lines) != 0:
                    if set(line[2]) != set(lines[0][2]):
                        # print(line[2])
                        # print(lines[-1][2])
                        lines.append(line)
                        # print(lines)
                        ip = line[0]
                        message = line[1]
                        time_ = line[2]

                        # print(f"IP remetente: {ip}")
                        # print(f"Mensagem: {message}")
                        # print(f"Data: {time_}")
                elif len(lines) == 0:
                    lines.append(line)

                    ip = line[0]
                    message = line[1]
                    time_ = line[2]

                    # print(f"IP remetente: {ip}")
                    # print(f"Mensagem: {message}")
                    # print(f"Data: {time_}")

            i += 1

    file.close()

    if lines != last_lines:
        print(lines[-1][2])

        identity = get_identity(lines[-1][0])

        if identity[1] == ' Luiz Gustavo':
            periodo = analize_message(lines[-1][1])

    last_lines = lines
