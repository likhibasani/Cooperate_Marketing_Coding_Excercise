from flask import Flask, render_template, request, redirect, url_for
from reimbursement import Reimbursement

app = Flask(__name__)
reimbursement = Reimbursement()

@app.route('/')
def index():
    ads = reimbursement.get_ads()
    total_reimbursement = reimbursement.total_reimbursement()
    return render_template('index.html', ads=ads, total_reimbursement=total_reimbursement, reimbursement=reimbursement)

@app.route('/add_ad', methods=['POST'])
def add_ad():
    ad_type = request.form['ad_type']
    count = int(request.form['count'])
    spend = float(request.form['spend'])
    reimbursement.add_ad(ad_type, count, spend)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
