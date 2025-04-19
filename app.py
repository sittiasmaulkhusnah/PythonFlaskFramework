from flask import Flask, render_template, send_file
import matplotlib
matplotlib.use('Agg')  
from matplotlib import pyplot as plt
from io import BytesIO

app = Flask(__name__)

app_name = "My Application Name is: Asmaul dan Khusna"

#1 App Route di flask "hello word"
@app.route("/")
def hello_world():
    return f"<p>Haloo, Apa Kabar! {app_name} </p>"


#2 App Route di flask
@app.route("/aplikasi/")
def aplikasi():
    return "<p>Selamat datang di Aplikasi Flask</p>"


#3 App Route dengan HTML 
@app.route("/about/")
def about():
    return render_template('about_without_bostrapp.html')

#4 App Route dengan HTML with bostrapp
@app.route("/about-bostrapp/")
def about_bostrapp():
    return render_template('about.html')

#5 App Route Dinamis
@app.route("/nama/<string:nama_mahasiswa>/")
def getnama(nama_mahasiswa):
    return "nama anda adalah {}".format(nama_mahasiswa)

#6 App Route ID
@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

#7 App Route Variabel Global
@app.route('/variabel-global/')
def variabel_global():
    return f"Welcome {app_name}"

#8 App Route Dictionary Variabel
@app.route('/data')
def data():
    user = {"name": "Usna", "age": 18, "city": "Makassar"}
    return render_template('data.html', user=user)

# app route plot dengan matplotlib (nilai mahasiswa)
@app.route('/plot/')
def plot():
    # Data 
    mahasiswa = ["Asmaul", "Khusna", "Usna"]
    nilai = [100, 90, 95]
    warna = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # Warna custom

    # Buat plot
    plt.figure(figsize=(8, 5))
    bars = plt.bar(mahasiswa, nilai, color=warna)
    
    # Tambahkan nilai di atas setiap bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height}',
                 ha='center', va='bottom', fontsize=12)

    # Styling plot
    plt.title("Perbandingan Nilai Mahasiswa", pad=20, fontsize=14)
    plt.xlabel("Nama Mahasiswa", labelpad=10)
    plt.ylabel("Nilai", labelpad=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.ylim(0, 100)  # Batas maksimum nilai

    # Simpan plot ke buffer
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
    img_buffer.seek(0)
    plt.close()

    return send_file(img_buffer, mimetype='image/png')

if __name__ == "__main__":
    app.run()