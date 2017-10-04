#encoding:utf8
from flask import Flask,render_template
from faker import Faker

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ajax_test")
def ajax_test():
    return "修改后：dsa~~~~~~"

@app.route("/ajax_test1/<str>")
def ajax_test1(str):
    L = ['Rebecca Mccormick MD', 'Robin Kennedy', 'Derek Alvarez', 'Heidi Combs', \
    'Elizabeth Rivas', 'Danielle Neal', 'Scott Brooks', 'Jennifer King', 'Tyler Lopez',\
     'Richard Garcia', 'Luke Hoffman', 'Amber Wheeler', 'Melanie Hart', 'Anthony Wilkerson',\
      'Chad Oconnor', 'Jodi Gonzalez', 'Audrey Potter', 'SethHampton', 'Nicole Carter', \
      'Tricia Cisneros']
    res = [i for i in L if i.lower().startswith(str.lower())]
    if len(res) != 0:
        return ",".join(res)
    return "没有！"

if __name__ == '__main__':
    app.run(debug=True)