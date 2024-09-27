from db import app, db, Character
    
def get_character_data():
    
    with app.app_context():
        
        character_data = db.session.execute(db.select(Character)).scalars().one()

    return character_data.as_dict()
