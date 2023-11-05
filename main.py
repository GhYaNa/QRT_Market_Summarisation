# Example: reuse your existing OpenAI setup
import os
import openai
from flask import Flask, render_template 
from flask import request 

app = Flask(__name__)

#sets up the Flask Sever
@app.route('/',method=['POST','GET'])#use POST to the folder and send data to a data base
def index():
    return render_template('index.html')

openai.api_base = "http://localhost:1234/v1" # point to the local server
openai.api_key = "" # no need for an API key

completion = openai.ChatCompletion.create(
  model="local-model" # this field is currently unused
  @app.route('/api/data')
  def api_data():
    data = {'message': 'Data from Python'}
    return jsonify(data)


  messages=[
    {"role": "user", "content": input}
  ] 
)

print(completion.choices[0].message)

if __name__ == '__main__':
  app.run(debug=True)