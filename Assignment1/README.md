# Assignment 1 
### Author: Zixin Jiang

### Requirements
Requirements can be found in requirements.txt


### RFAST API using Flask
To run this FAST API:

First run:
```bash
$ uvicorn api:app --reload
```
In a separate terminal, run the follow two commands for the GET and POST requests.
```bash
$ curl http://127.0.0.1:8000/
$ http://127.0.0.1:8000/list
$ http://127.0.0.1:8000/find?term=moon
$ http://127.0.0.1:8000/note/Wensleydale
```
To add note, use
```bash
curl -X POST "http://127.0.0.1:8000/add" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"name": "Wensleydale", "content": "Isn'\''t the moon made out of this?"}'
```
or upload the file
```bash
curl -X POST 'http://127.0.0.1:8000/add' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d @note.json
```

### Flask webserver
First run:
```bash
$ python app.py
```
To access the website, point a browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).


### Streamlit
First run:
```bash
 $ streamlit run stream.py
```
To access the website, point the browser at [http://localhost:8501/](http://localhost:8501/). 




