from flask import Flask, jsonify, request
from src.datastructure import FamilyStructure

app = Flask(__name__)

jackson_family = FamilyStructure('Jackson')

@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data or 'first_name' not in data or 'age' not in data or 'lucky_numbers' not in data:
        return jsonify({"error": "Bad request"}), 400
    member = {
        "id": data.get("id"),
        "first_name": data["first_name"],
        "age": data["age"],
        "lucky_numbers": data["lucky_numbers"]
    }
    jackson_family.add_member(member)
    # Devuelve el miembro agregado (con id generado)
    return jsonify(jackson_family.get_member(member["id"])), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    deleted = jackson_family.delete_member(member_id)
    if deleted:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404