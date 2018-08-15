# sectionsextractor


TODO: UNDER CONSTRUCTION!!!
TODO: If behind proxy, set your proxy inside config.py

==================================================

A kind of REAME.first file
... but in reality the content are my notes

==================================================

This is the very first version of a
Sections Extractor application
wrapped into a Web Framework.
Used for Recommendation Engine
Knowledge Base.

Materials were used from http://inventwithpython.com/

The application is web based using Flask.

You can run the application
(after installing it
as intended with the below section notes)

Linux
(venv) $ export FLASK_APP=sectionsextractor.py
MS
(venv) $ set FLASK_APP=sectionsextractor.py

(venv) $ flask run

..register your user...
..test introducing file name "01.txt" ...for Document Extractor
...test introducing url "https://en.wikibooks.org/wiki/GNU_Health/Families" ... for HTML Extractor

The below initial project notes are from my exercises based on
The Flask Mega-Tutorial
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

Enjoy it and please, let me know any comments to make it better/useful.
Thank you.


==================================================

TO DO: app sources download
$ git config --global http.proxy http://proxy.mycompany:80
$ git clone https://github.com/daniel-julio-iglesias/sectionsextractor
(...)
==================================================

Install these packages after app sources download


(venv) $ pip install flask
(venv) $ pip install --proxy http://user:pass@proxyAddress:proxyPort flask

(venv) $ pip install flask-wtf
(venv) $ pip install flask-sqlalchemy
(venv) $ pip install flask-migrate
(venv) $ pip install flask-login
(venv) $ pip install bs4
(venv) $ pip install beautifulsoap4
(venv) $ pip install lxml

===================================================

Apply the next db steps after downloading your app sources


Linux
(venv) $ export FLASK_APP=sectionsextractor.py
MS
(venv) $ set FLASK_APP=sectionsextractor.py

(venv) $ flask db upgrade


===================================================

Run the application

Linux
(venv) $ export FLASK_APP=sectionsextractor.py
MS
(venv) $ set FLASK_APP=sectionsextractor.py

(venv) $ flask run


URL: http://localhost:5000/
URL: http://localhost:5000/index

===================================================

See notes_sectionsextractor.txt file inside docs directory.


TODO: See notes_sectionsextractor.txt file inside docs directory.

TODO: Make a form to introduce URL from where to extract sections
TODO: Implement the logic for HTML section text extraction process
TODO: Implememt functionality for text extraction from MS Word / or compatible document
TODO: Implememt functionality for text extraction from PDF document
TODO: Implememt functionality for text extraction from MS Excel / or compatible document


===================================================

