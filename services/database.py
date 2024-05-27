import sqlite3

def input_data(forecast):

    con = sqlite3.connect('database/desafio_compras.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO forecast (SUPP_CODE,YEAR, MONTH, PRICE, VOL, USER) VALUES (?, ?, ?, ?, ?, ?)', (forecast.supp_code, forecast.year, forecast.month, forecast.price, forecast.vol, forecast.user))
    con.commit()
    con.close()

def read_data():

    con = sqlite3.connect('database/desafio_compras.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM forecast')
    data = cursor.fetchall()
    con.close()

    return data