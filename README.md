![](images/doge.png)

at the time of writing, <br>
torch 1.3.1 needs python 3.10 (not python 3.11) <br>
gensim 4.30 needs > python 3.7 <br>

inquire: <br>
ls -l /usr/local/bin/python*

change: <br>
ln -s -f /usr/local/bin/python3.10 /usr/local/bin/python3 <br>
ln -s -f /usr/local/bin/python3.10 /usr/local/bin/python <br>

then add: <br>
python -m pip install jupyterlab <br>
python -m pip install ipykernel <br>
python -m ipykernel install --name wine-chatbot-rec <br>
python -m ipykernel install --user <br>

install env: <br>
python -m pip install --user virtualenv <br>
python -m venv <name, like wine-chatbot-rec> <br>

activate env and install pkgs: <br>
source wine-chatbot-rec/bin/activate <br>
python -m pip install -r requirements.txt <br> 

then run locally: <br>
jupyter notebook 

reference: <br>
https://dev.to/malwarebo/how-to-set-python3-as-a-default-python-version-on-mac-4jjf
