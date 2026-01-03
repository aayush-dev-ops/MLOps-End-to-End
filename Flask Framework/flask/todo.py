## put, delete - http verbs
## wokring with api's -- json

from flask import Flask, jsonify, request

app = Flask(__name__)

##Initial data in my todo list
'''
this usually comes from sql, mongodb etc...
it is in the form of dict, means you can convert it into jsonify
'''
items = [
    {"id":1,"name":"Item 1","desc": "This is item 1"},
    {"id":2,"name":"Item 2","desc": "This is item 2"},
    {"id":3,"name":"Item 3","desc": "This is item 3"}
]

#home page 
@app.route('/')
def home():
    return "Create your ToDoS."

#get : retrieve all the todos
@app.route('/getitems',methods =['GET'])
def get_items():
    return jsonify(items)

#Get : retrieve todos based on some ID
@app.route('/getitems/<int:item_id>',methods =['GET'])
def get_by_id(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"Error":"item not found"})
    return jsonify(item)

#Post : New Task
@app.route('/crateitems',methods =['POST'])
def create_items():
    if not request.json or not 'name' in request.json:
        return jsonify({"Error":"item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name" : request.json['name'],
        "desc" : request.json['desc']
    }
    items.append(new_item)
    return jsonify(new_item)

#PUT : we update an existing item.not craete a new one.
@app.route('/getitems/<int:item_id>',methods =['PUT'])
def update_items(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"Error":"item not found"})
    item['name'] = request.json.get('name',item['name'])
    item['desc'] = request.json.get('desc',item['desc'])
    
    return jsonify(item)
    
#DELETE: delete an item
@app.route('/delitems/<int:item_id>',methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result" : "item deleted"})
'''
Loops through all items
Keeps only the items whose id is NOT equal to item_id
Effectively removes the item with the matching ID
'''

if __name__ =='__main__':
    app.run(debug = True)