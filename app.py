from flask import Flask, render_template, redirect, request
import predict as p

# __name__ == __main__
app = Flask(__name__)


@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')
   
    
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def marks():
    if request.method == 'POST':

        f = request.files['userfile']
        path = "./static/{}".format(f.filename)  # ./static/images.jpg
        f.save(path)
        print(f.filename)
        caption = p.caption_this_image(path)

        result_dic = {
            'image': path,
            'caption': caption
        }

    return render_template("result.html", your_result=result_dic)


if __name__ == '__main__':
    app.run(debug=True ,threaded=False)
