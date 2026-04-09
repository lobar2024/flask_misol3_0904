from flask import Flask, render_template

app = Flask(__name__)

talabalar = ["Zafar", "Malika", "Ali", "Gulnora", "Bekzod"]

@app.route('/talabalar')
def talabalar_royxati():
    talabalar_saralangan = sorted(talabalar)  # alfavit bo‘yicha saralash
    umumiy_soni = len(talabalar_saralangan)   # umumiy son
    return render_template('talabalar.html', talabalar=talabalar_saralangan, soni=umumiy_soni)

if __name__ == '__main__':
    app.run(debug=True)
