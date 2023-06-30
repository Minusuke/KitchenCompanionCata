from models import db
from models.relations import relations

class Recipe(db.Model):
    __tablename__='recipes'
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    ingredient_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    ingredient = db.relationship('Ingredient', cascade="all,delete", secondary=relations.ingredient_user, backref="recipes")

def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
        
def save(self):
    db.session.add(self)
    db.session.commit()
    
def update(self):
    db.session.commit()
        
def delete(self):
    db.session.delete(self)
    db.session.commit()