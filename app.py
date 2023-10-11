from flask import Flask, request, render_template
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "whysoserious"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/form')
def form_page():
    return render_template('form.html', words=stories.story.prompts)

@app.route('/story', methods=["POST"])
def render_story():
    my_keys = stories.story.prompts
    prompt_ans = {}
    
    for idx in range(len(my_keys)):
        prompt_ans[my_keys[idx]] = request.form[my_keys[idx]]
    compstory = stories.story.generate(prompt_ans)
    return render_template('story.html', compstory=compstory)
    



