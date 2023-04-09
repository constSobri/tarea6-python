import time


def regresarACasa():
    hora = time.localtime().tm_hour
    minutos = time.localtime().tm_min
    horasRestantes = 18 - hora
    minutosRestantes = 60 - minutos

    def minutoCero():
        if minutosRestantes < 10:
            return '0' + str(minutosRestantes)
        else:
            return minutosRestantes

    minutosCero = minutoCero()

    if hora >= 19:
        print('Ya puedes irte a casa!')
    elif horasRestantes == 1:
        print('Oops, te faltan', horasRestantes, 'hora y', minutosCero, 'minutos para salir del trabajo.')
    else:
        print('Oops, te faltan', horasRestantes, 'horas y', minutosCero, 'minutos para salir del trabajo.')


regresarACasa()
