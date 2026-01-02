FLASK FRAMEWORK:
complete web framework that is created with the help of pytohn progg language. there are other frameworks as well apart from flask -> django, fast API, stringlit.

Things we will discuss here:
1. WSGI -> WEB SERVER GATEWAY INTERFACE
2. JINJA 2 : TEMPLATE ENGINE
-------------------------------------------------------------------
1. WSGI -> WEB SERVER GATEWAY INTERFACE

web server : where we deploy our entire application.
examples : AWS ec2, Azure app, apache, iis // used based on requirement

web server k andar web app hai. web app -> written in flask framework.
whenever a req comes from a user, i will be getting the request/s in web server. this web app will redirect this req to web app and get the response back.

for this comunication, we will use a protocol. this is called -> WSGI.
web server gateway interface.

so the entire req and response thing is based on WSGI.


2. JINJA 2 : TEMPLATE ENGINE

FLask  has this jinja 2 technique.

it is a web template engine: work?
it combines a web template (any page in a website) with the data source(csv sheet/ a sql db/mongo db/ a ml model from where we will be getting some kind of response/...), And after this the entire web page will get loaded.

example -> in a login page, the user name and pasword gets authenticated from the database.

HELPS TO CREATE DYNAMIC WEB PAGES
