import time
import decipher
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
from urllib.parse import urlencode
import json


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 50]

        self.add_widget(Label(text='Login'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Senha'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.login_button = Button(text='Entrar')
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

        self.headers = {'Content-Type': 'application/json'}

    def login(self, instance):
        username = self.username.text
        password = self.password.text
        date = time.gmtime()
        server_number = 4
        message = [username, date]
        message1 = [password, date]
        d_message = decipher.encript(message, server_number)
        d_message1 = decipher.encript(message1, server_number)
        print(d_message[0])
        current_time = [d_message[1].tm_year, d_message[1].tm_mon, d_message[1].tm_mday, d_message[1].tm_hour,d_message[1].tm_min, d_message[1].tm_sec,d_message[1].tm_wday, d_message[1].tm_yday,d_message[1].tm_isdst]
        current_time_ = f"{current_time[0]} {current_time[1]} {current_time[2]} {current_time[3]} {current_time[4]} {current_time[5]} {current_time[6]} {current_time[7]} {current_time[8]}"

        url = 'http://[2804:5da8:bb20:e066:5493:7f49:2ee2:a033]:80/receive-login'  # URL do servidor
        data = {"n": format(d_message[0], ".30f"),
                "a": format(d_message1[0], ".30f"),
                "c": current_time}  # Dados a serem enviados para o servidor
        json_data = json.dumps(data)
        try:
            response = requests.post(url, data=json_data, headers=self.headers)
            if response.status_code == 200:
                print("Senha enviada com sucesso para o servidor!")
            else:
                print("Falha ao enviar senha para o servidor. Código de resposta:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Ocorreu um erro ao enviar a senha:", e)

        print("Usuário: ", username)
        print("Senha: ", password)


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()