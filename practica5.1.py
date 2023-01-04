from bs4 import BeautifulSoup
import requests
import pandas as pd
from fpdf import FPDF
import seaborn as sns
import matplotlib.pyplot as plt

def extract():
    web = 'https://api.sportsdata.io/v3/nba/projections/json/PlayerSeasonProjectionStatsByTeam/2022/MIA'
    headers = '?key=74f54d2e7e0540a992f1df67a336d7af'

    resultado = requests.get(web + headers)
    json_por = resultado.json()
    df = pd.DataFrame(json_por)
    df = df[['Name', 'Points', 'Assists', 'Steals', 'Rebounds', 'Minutes', 'Games', 'BlockedShots']]
    df.to_csv('csv_stats')
    return(df)

def transform(df):
    TITLE = '\n\n\n\nNBA MIAMI HEAT STATS'
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('helvetica', 'B',35)
    pdf.set_margins(30,25,25)
    pdf.set_auto_page_break(True, 25)
    pdf.multi_cell(0, 10, txt=TITLE, align="C")
    pdf.ln()
    pdf.ln()
    pdf.set_font('helvetica','', 15)
    pdf.multi_cell(0, 10, txt = 'Emma Rey Sánchez\nUniversidad Pontificia Comillas ICAI', align = 'C')
    pdf.image('miami_heat.png', x = 8, w = 190)
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 12)
    pdf.multi_cell(0, 10, txt = 'PRINCIPALES ESTADÍSTICAS DE LOS JUGADORES POR CATEGORÍAS')
    pdf.ln()
    pdf.set_font('helvetica', 'B', 8)
    pdf.multi_cell(0, 10, txt = 'A continuación se muestran las estadísticas de los jugadores del equipo Miami Heat por categorías. Dichas categorías son: Puntos, asistencias, rebotes, robos, minutos y partidos.')
    pdf.ln()
    pdf.set_font('helvetica', 'B', 12)
    pdf.multi_cell(0, 10, txt = 'PUNTOS POR JUGADOR')
    y = df['Points']
    x = df['Name']
    plt.figure(figsize=(15,10))
    sns.barplot(x=x, y=y)
    plt.xticks(rotation = -90)
    plt.savefig('grafico1.png', bbox_inches = 'tight')
    pdf.image('grafico1.png', x = 8, w = 190)
    pdf.ln()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 12)
    pdf.multi_cell(0, 10, txt = 'ASISTENCIA POR JUGADOR')
    y = df['Assists']
    x = df['Name']
    plt.figure(figsize=(15,10))
    sns.barplot(x=x, y=y)
    plt.xticks(rotation = -90)
    plt.savefig('grafico2.png', bbox_inches = 'tight')
    pdf.image('grafico2.png', x = 8, w = 190)
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 12)
    pdf.multi_cell(0, 10, txt = 'REBOTES POR JUGADOR')
    y = df['Rebounds']
    x = df['Name']
    plt.figure(figsize=(15,10))
    sns.barplot(x=x, y=y)
    plt.xticks(rotation = -90)
    plt.savefig('grafico3.png', bbox_inches = 'tight')
    pdf.image('grafico3.png', x = 8, w = 190)
    pdf.ln()
    pdf.add_page()
    pdf.multi_cell(0, 10, txt = 'ROBOS POR JUGADOR')
    y = df['Steals']
    x = df['Name']
    plt.figure(figsize=(15,10))
    sns.barplot(x=x, y=y)
    plt.xticks(rotation = -90)
    plt.savefig('grafico4.png', bbox_inches = 'tight')
    pdf.image('grafico4.png', x = 8, w = 190)
    pdf.ln()
    pdf.add_page()
    pdf.multi_cell(0, 10, txt = 'MINUTOS POR JUGADOR')
    y = df['Minutes']
    x = df['Name']
    plt.figure(figsize=(15,10))
    sns.barplot(x=x, y=y)
    plt.xticks(rotation = -90)
    plt.savefig('grafico5.png', bbox_inches = 'tight')
    pdf.image('grafico5.png', x = 8, w = 190)
    pdf.ln()
    pdf.add_page()
    pdf.multi_cell(0, 10, txt = 'PARTIDOS POR JUGADOR')
    y = df['Games']
    x = df['Name']
    plt.figure(figsize=(15,10))
    sns.barplot(x=x, y=y)
    plt.xticks(rotation = -90)
    plt.savefig('grafico6.png', bbox_inches = 'tight')
    pdf.image('grafico6.png', x = 8, w = 190)
    pdf.ln()
    return pdf


def load(pdf):
    pdf.output('pdfnba.pdf')

if __name__ == '__main__':
    dataf = extract()
    pdf = transform(dataf)
    load(pdf)
