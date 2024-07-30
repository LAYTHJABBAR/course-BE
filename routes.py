from flask import Blueprint, request, jsonify, current_app
from pymongo import MongoClient
from bson.objectid import ObjectId
from models import normalize_data
from utils import check_and_refresh_data

main = Blueprint('main', __name__)

@main.before_app_request
def before_first_request():
    url = "https://api.mockaroo.com/api/501b2790?count=1000&key=8683a1c0"
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client[current_app.config['MONGO_DBNAME']]
    check_and_refresh_data(url, db)

@main.route('/get_courses', methods=['GET'])
def get_courses():
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client[current_app.config['MONGO_DBNAME']]
    collection = db['courses']
    search_query = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    query = {"$or": [
        {"University": {"$regex": search_query, "$options": "i"}},
        {"City": {"$regex": search_query, "$options": "i"}},
        {"Country": {"$regex": search_query, "$options": "i"}},
        {"Course Name": {"$regex": search_query, "$options": "i"}},
        {"Course Description": {"$regex": search_query, "$options": "i"}}
    ]}
    skip = (page - 1) * page_size
    cursor = collection.find(query).skip(skip).limit(page_size)
    courses = list(cursor)
    
    for course in courses:
        course['_id'] = str(course['_id'])
    
    return jsonify(courses)

@main.route('/create_course', methods=['POST'])
def create_course():
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client[current_app.config['MONGO_DBNAME']]
    collection = db['courses']
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"id": str(result.inserted_id)})

@main.route('/update_course/<course_id>', methods=['PUT'])
def update_course(course_id):
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client[current_app.config['MONGO_DBNAME']]
    collection = db['courses']
    data = request.json
    result = collection.update_one({"_id": ObjectId(course_id)}, {"$set": data})
    return jsonify({"matched_count": result.matched_count})

@main.route('/delete_course/<course_id>', methods=['DELETE'])
def delete_course(course_id):
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client[current_app.config['MONGO_DBNAME']]
    collection = db['courses']
    result = collection.delete_one({"_id": ObjectId(course_id)})
    return jsonify({"deleted_count": result.deleted_count})
