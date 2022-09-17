from cProfile import label
import requests as r
import datetime as dt
import csv 
from PIL import Image
from IPython.display import display
from urllib.parse import quote

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
print(resp.status_code)

raw_data = resp.json()
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

final_data.insert(0, ['Confirmados','obitos','Recuperados','ativos','Data'])

# Excluindo o time zone que é 0 e não agrega em nada no projeto:
CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]

print(final_data[0])
for i in final_data[1:]:
    print(i)
    

# DateTime: Data, hora, segundo e microsegundo:
import datetime as dt
print(dt.time(12, 6, 21, 7), 'Hora:minuto:segundo:microsegundo')
print('----')
print(dt.date(2021, 10, 30), 'Ano/mês/dia')
print('----')
print(dt.datetime(2021, 10, 30, 12, 6, 21, 7), 'Ano/mês/dia Hora:minuto:segundo:microsegundo')
print()     


natal = dt.date(2021, 12, 25)
reveillon = dt.date(2022, 1, 1)
print({reveillon - natal})
print(f'Faltam {(reveillon - natal).days} dias para o reveillon')
print(f'Faltam {(reveillon - natal).total_seconds()} segundos para o reveillon')
print(f'Faltam {(reveillon - natal).microseconds} microsegundos para o reveillon')
print()

with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

for i in range(1, len(final_data)):
    final_data[i][DATA] =  dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')


def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets= []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [
            {
                'label': labels[0],
                'data': y
            }
        ]


def set_title(title=''):
    if title != '':
        display = 'true'
    else:        
        display = 'false'
    return {
        'title': title,
        'display': display
    }

def create_chart(x,y, labels, kind ='bar', title=''):
    datasets = get_datasets(y, labels)
    options = set_title(title)

    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }

    return chart


def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp =  r.get(f'{url_base}?c={str(chart)}')
    return resp.content


def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)

def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)


y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])


y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])

labels = ['Confirmados', 'Recuperados']

x = []

for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))

chart = create_chart(x,[y_data_1, y_data_2], labels,  title='Gráfico confirmado vs recuperados')    
chart_content = get_api_chart(chart)
save_image('meu-primeiro-grafico.png', chart_content)
display_image('meu-primeiro-grafico.png')

# Gerar QR-CODE:
def get_api_qrcode(link):
    text = quote(link) # parsing do link para url
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content

# Recuperar o link
url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('qr-code.png', get_api_qrcode(link))
display_image('qr-code.png')