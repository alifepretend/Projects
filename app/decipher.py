import math
import decimal


def encript(mensagem, server_number):
    frase = mensagem[0]
    data = mensagem[1]
    server_number = server_number
    translate_dict = {
        " ": "00",
        "a": "01",
        "b": "02",
        "c": "03",
        "d": "04",
        "e": "05",
        "f": "06",
        "g": "07",
        "h": "08",
        "i": "09",
        "j": "10",
        "k": "11",
        "l": "12",
        "m": "13",
        "n": "14",
        "o": "15",
        "p": "16",
        "q": "17",
        "r": "18",
        "s": "19",
        "t": "20",
        "u": "21",
        "v": "22",
        "w": "23",
        "x": "24",
        "y": "25",
        "z": "26",
        ".": "27",
        "...": "28",
        "?": "29",
        "!": "30",
        "1": "31",
        "2": "32",
        "3": "33",
        "4": "34",
        "5": "35",
        "6": "36",
        "7": "37",
        "8": "38",
        "9": "39",
        "0": "40"
    }

    inverted_dict = {v: k for k, v in translate_dict.items()}

    encript_frase = []
    for letter in frase:
        encript_letter = translate_dict[f"{letter}"]
        encript_frase.append(encript_letter)
    cript_frase = ""
    for i in encript_frase:
        cript_frase = cript_frase + i

    cript_frase = int(cript_frase)
    print(cript_frase)

    cript_frase = decimal.Decimal(cript_frase) / decimal.Decimal(data[0])

    cript_frase = pow(decimal.Decimal(cript_frase), decimal.Decimal(data[1]))

    cript_frase = decimal.Decimal(cript_frase) * decimal.Decimal(data[2]) * decimal.Decimal(
        math.log(data[2] * server_number))

    # frase encriptada

    print(f"Frase encriptada: {'{:.0f}'.format(cript_frase)}")
    return [cript_frase, data]


def decript(mensagem, server_number):
    frase = mensagem[0]
    data = mensagem[1]
    server_number = server_number
    translate_dict = {
        " ": "00",
        "a": "01",
        "b": "02",
        "c": "03",
        "d": "04",
        "e": "05",
        "f": "06",
        "g": "07",
        "h": "08",
        "i": "09",
        "j": "10",
        "k": "11",
        "l": "12",
        "m": "13",
        "n": "14",
        "o": "15",
        "p": "16",
        "q": "17",
        "r": "18",
        "s": "19",
        "t": "20",
        "u": "21",
        "v": "22",
        "w": "23",
        "x": "24",
        "y": "25",
        "z": "26",
        ".": "27",
        "...": "28",
        "?": "29",
        "!": "30",
        "1": "31",
        "2": "32",
        "3": "33",
        "4": "34",
        "5": "35",
        "6": "36",
        "7": "37",
        "8": "38",
        "9": "39",
        "0": "40"
    }
    inverted_dict = {v: k for k, v in translate_dict.items()}

    deciphered_frase = decimal.Decimal(frase) / decimal.Decimal(data[2]) / decimal.Decimal(
        math.log(data[2] * server_number))

    deciphered_frase = pow(decimal.Decimal(deciphered_frase), 1 / decimal.Decimal(data[1]))

    deciphered_frase = decimal.Decimal(deciphered_frase) * decimal.Decimal(data[0])

    numero_completo = '{:.0f}'.format(deciphered_frase)

    if len(numero_completo) == 23:
        numero_completo = "0" + numero_completo

    i = 0
    temp = []
    leters = []
    for digit in numero_completo:
        if i == 0:
            temp.append(digit)
            i += 1
        elif i == 1:
            temp.append(digit)
            digit_2 = temp[0] + temp[1]
            leters.append(digit_2)
            temp = []
            i = 0
    sentence = ""
    for letter in leters:
        sentence = sentence + inverted_dict[f"{letter}"]
    return sentence


if __name__ == "__main__":
    mensagem = ["lugu1873", "[2023, 5, 21, 20, 39, 35, 6, 141, 0]"]


    message = encript(mensagem, 3)
    print(message)

    decripted_frase = decript(message, 3)
    print(decripted_frase)





