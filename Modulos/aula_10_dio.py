from datetime import date, time, datetime, timedelta

def trabalhando_date():
    data_atual= date.today()
    data_atual_str =(data_atual.strftime('%A/%B/%Y'))
    #print(type(data_atual))
    print(data_atual_str)
    #print(type(data_atual_str))
def trabalhando_time():
        horario= time(hour=12,minute=18, second=30)
        print(horario)

def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    dias=('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado','Domingo' )
    print(dias[data_atual.weekday()])
    data_criada= datetime(2018,5,20,15,30,20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_str='01/01/2023 12:20:22'
    data_cvt= datetime.strptime(data_str, '%d/%m/%Y %H:%M:%S')
    print(data_cvt)
    nova_data = data_cvt - timedelta(days=365, hours=2)
    print(nova_data)
    nova_data = data_cvt + timedelta(days=365, hours=2)
    print(nova_data)
if __name__ == '__main__':
    #trabalhando_date()
    trabalhando_time()
    trabalhando_datetime()
