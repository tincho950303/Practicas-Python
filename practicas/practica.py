duracion = 299

hora = 60
dia = hora * 24

hora_actual = 19.5
horas_dia = 24

restante_dia = horas_dia - hora_actual

def calcular_horas_trabajo(horaEntrada,horaSalida):
    calculo =  horaEntrada / horaSalida
    resta = calculo % 24
    print(round(calculo))



horas,minutos  = duracion / hora, duracion % hora

resultado = f"{round(horas)} hs con {minutos} minutos."


calcular_horas_trabajo(7,14)