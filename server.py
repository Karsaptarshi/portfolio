from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)



@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/templates/index.html')
def my_home2():
    return render_template('index.html')

@app.route('/templates/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)    

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message = data["message"]
        file =database.write(str({'Email':email,'Subject':subject,'Message':message}))
        file =database.write('\n')

@app.route('/templates/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data =request.form.to_dict()
        write_to_file(data)
        print(data)
        return redirect('./thankyou.html')
    else:
        return 'Something went wrong'

# @app.route('/templates/work.html')
# def work():
#     return render_template('work.html')  

# @app.route('/templates/components.html')
# def component():
#     return render_template('components.html')    

# @app.route('/templates/about.html')
# def about():
#     return render_template('about.html')      

# @app.route('/templates/works.html')
# def works():
#     return render_template('works.html')   

# @app.route('/templates/contact.html')
# def contact():
#     return render_template('contact.html')       