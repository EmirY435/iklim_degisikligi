# İçe Aktarma
from flask import Flask, render_template, request


app = Flask(__name__)

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')
# İkinci sayfa
@app.route('/1')
def canlilar():
    return render_template(
                            'canlilar.html', 
                           )

# Üçüncü sayfa
@app.route('/2')
def ayak_izi():
    return render_template(
                            'ayak_izi.html',                                                   
                           )

# Hesaplama
@app.route('/3')
def tedbirler():
    return render_template(
                            'tedbirler.html', 
                           )


@app.route('/4')
def evde_su():
    return render_template(
                            'evde_su.html', 
                           )



app.run(debug=True)
