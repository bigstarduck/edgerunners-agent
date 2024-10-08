from db import Armor, Character, Health, app, db
    
def get_character_data():
    
    with app.app_context():
        
        # TODO: This will fail if there's more then one Character in the database.
        character_data = db.session.execute(db.select(Character)).scalar_one()

    return character_data.as_dict()

def set_health(id, hp, timestamp):
    print(type(timestamp))
    with app.app_context():
        health = db.session.execute(
            db.select(Health).where(Health.id == id)
        ).scalar_one()

        health.update_hp(hp, timestamp)

        db.session.commit()

        health_data = db.session.execute(
            db.select(Health).where(Health.id == id)
        ).scalar_one()

    return health_data.as_dict()

def set_armor(id, hp, timestamp):
    with app.app_context():
        armor = db.session.execute(
            db.select(Armor).where(Armor.id == id)
        ).scalar_one()

        armor.update_hp(hp, timestamp)

        db.session.commit()

        armor_data = db.session.execute(
            db.select(Armor).where(Armor.id == id)
        ).scalar_one()

    return armor_data.as_dict()
