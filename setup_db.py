from db import app,db,Stat,Health,Armor

with app.app_context():
    db.create_all()
    db.session.add_all([
        Stat('INT',7),
        Stat('REF',7),
        Stat('DEX',6),
        Stat('TECH',5),
        Stat('COOL',7),
        Stat('WILL',6),
        Stat('LUCK',6),
        Stat('BODY',7),
        Stat('EMP',5),
        Health('35'),
        Armor('Head',7),
        Armor('Body',12),
        ])
    db.session.commit()