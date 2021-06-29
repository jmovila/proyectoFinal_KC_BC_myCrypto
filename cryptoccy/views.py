from cryptoccy import app
from flask import render_template, url_for, request, redirect, flash
from cryptoccy.forms import MovimientosForm
from cryptoccy.dataaccess import *
import datetime

now =datetime.datetime.now()
horaActual=now.time()




dbManager = DBmanager()

listCryptos =['EUR', 'BTC', 
'ETH', 'XRP', 
'LTC', 'BCH', 
'BNB', 'USDT', 
'EOS', 'BSV', 
'XLM', 'ADA', 
'TRX']

@app.route('/', methods=['GET', 'POST'])
def index():
   formulario= MovimientosForm()

   conexion = sqlite3.connect("movEx.db")#conecta a la BBDD
   cur = conexion.cursor()#activa la conexion ¿?
   cur.execute("SELECT * FROM movEx")
   claves = cur.description #me saca las cabeceras de la tabla
   filas= cur.fetchall()#me saca las filas
   movements=[]
   for fila in filas:
      d ={}
      for tclave, valor in zip(claves, fila):
         d[tclave[0]]=valor
         print(d)
      movements.append(d)

   return render_template('inicio.html', datos=movements)

@app.route('/purchase', methods=['GET', 'POST'])
def purchase():
   
   formulario= MovimientosForm()
   if request.method == 'GET':
      return render_template('compra.html', form = formulario)
   
   else:
      if formulario.validate():

         query = "INSERT INTO movEx (Fecha, Hora, FromCcy, FromQty, ToCcy, ToQty, PrecioU) VALUES (?, ?, ?, ?, ?, ?, ?)"
         print(query)
         dbManager.modificaTablaSQL(query, [formulario.fecha.data, formulario.hora.data,
                                          formulario.fromCcy.data, formulario.fromQty.data,
                                             formulario.toCcy.data, formulario.toQty.data, formulario.fromQty.data *formulario.toQty.data])
      
         return redirect(url_for("index"))
      else:
         return render_template('compra.html', form = formulario)
   
         
            
 

      
      
   

     
  



  

      