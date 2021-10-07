from flask import Flask
from flask import render_template
from datetime import datetime, time
import glob
import csv

from flask.helpers import total_seconds

app = Flask(__name__)

@app.route("/")
def main():
    total_token_data = []
    date_data = []
    for csv_files in [file for file in glob.glob("./data/*") if file.endswith(".csv")]:
        opener = open(csv_files, 'r', encoding='utf-8')
        reader = csv.reader(opener)
        for line in reader:
            total_token_data.append(line[2])
            date_data.append(line[0]+' '+line[1])
        opener.close()
    print(date_data[-1].split(" ")[0]+" "+date_data[-1].split(" ")[1])
    AHSH = datetime.strptime(date_data[-1].split(" ")[0]+" "+date_data[-1].split(" ")[1],"%Y/%m/%d %H:%M:%S")
    BHSH = datetime.strptime(date_data[-5].split(" ")[0]+" "+date_data[-5].split(" ")[1],"%Y/%m/%d %H:%M:%S")
    print(int(total_token_data[-1]), int(total_token_data[-5]), AHSH, BHSH, int(((AHSH- BHSH).seconds)))
    xvc = (int(total_token_data[-1]) - int(total_token_data[-5])) / int(((AHSH- BHSH).seconds))
    print(xvc * int(((AHSH- BHSH).seconds)))
    return render_template(
        'index.html', 
        values=total_token_data, 
        labels=date_data, 
        legend='패스토큰',
        current_token=total_token_data[-1],
        hash=xvc * int(((AHSH- BHSH).seconds))
        )


if __name__ == "__main__":
    app.run(debug=True)
