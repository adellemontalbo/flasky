from flask import Blueprint, jsonify, abort, make_response

class Dog:
    def __init__(self, id, name, color, personality):
        self.id = id
        self.name = name
        self.color = color
        self.personality = personality

    def to_dog_dict(self):
        return dict(
            id=self.id, 
            name=self.name, 
            color=self.color,
            personality=self.personality
                    )



class Cat:
    def __init__(self, id, name, color, personality):
        self.id = id
        self.name = name
        self.color = color
        self.personality = personality

    def to_cat_dict(self):
        return dict(
            id=self.id, 
            name=self.name, 
            color=self.color,
            personality=self.personality
    )

cats = [
    Cat(1, "Luna", "grey", "naughty"), 
    Cat(2, "Orange Cat", "orange", "antagonistic"),
    Cat(3, "Big Ears", "grey and white", "sleepy")
]

dogs = [
    Dog(1, "Amigo", "brown", "playful"), 
    Dog(2, "Vigo", "black", "shy"),
]

bp_cats = Blueprint("cats", __name__, url_prefix="/cats")
bp_dogs = Blueprint("dogs", __name__, url_prefix="/dogs")

@bp_dogs.route("", methods=["GET"])
def handle_dogs():
    results_list = [dog.to_dog_dict() for dog in dogs]
    return jsonify(results_list)


@bp_cats.route("", methods=["GET"])
def handle_cats():
    results_list = []
    for cat in cats: 
        results_list.append(cat.to_cat_dict())
    return jsonify(results_list)

def validate_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except:
        abort(make_response({"message":f"cat {cat_id} invalid"}, 400))

    for cat in cats: 
        if cat.id == cat_id:
            return cat

    abort(make_response({"message":f"cat {cat_id} not found"}, 404))

@bp_cats.route("/<id>", methods=["GET"])
def handle_cat(id):
    cat = validate_cat(id)
    return jsonify(cat.to_cat_dict())