from flask import Flask
from flask import render_template
from datetime import time
import glob
import csv

app = Flask(__name__)

@app.route("/")
def main():
    for csv_files in [file for file in glob.glob("./data/*") if file.endswith(".csv")]:
        opener = open(csv_files, 'r', encoding='utf-8')
        reader = csv.reader(opener)
        for line in reader:
            print(line)
        opener.close()
    return render_template('index.html')

@app.route("/time_chart")
def time_chart():
    legend = 'Temperatures'
    temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
                    61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
                    70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
    times = [time(hour=11, minute=14, second=15),
             time(hour=11, minute=14, second=30),
             time(hour=11, minute=14, second=45),
             time(hour=11, minute=15, second=00),
             time(hour=11, minute=15, second=15),
             time(hour=11, minute=15, second=30),
             time(hour=11, minute=15, second=45),
             time(hour=11, minute=16, second=00),
             time(hour=11, minute=16, second=15),
             time(hour=11, minute=16, second=30),
             time(hour=11, minute=16, second=45),
             time(hour=11, minute=17, second=00),
             time(hour=11, minute=17, second=15),
             time(hour=11, minute=17, second=30),
             time(hour=11, minute=17, second=45),
             time(hour=11, minute=18, second=00),
             time(hour=11, minute=18, second=15),
             time(hour=11, minute=18, second=30)]
    return render_template('index.html', values=temperatures, labels=times, legend=legend)


if __name__ == "__main__":
    app.run(debug=True)
