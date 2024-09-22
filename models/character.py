from db import app, db, Stat, Armor, Health
    
def get_character_data():
    with app.app_context():
        character_stats = db.session.execute(db.select(Stat)).scalars()
        character_health = db.session.execute(db.select(Health)).scalars()
        character_armor = db.session.execute(db.select(Armor)).scalars()
        character_data = {
            "stats": [stat.as_dict() for stat in character_stats], 
            "health": [hp.as_dict() for hp in character_health], 
            "armor": [sp.as_dict() for sp in character_armor],
        }
    return character_data
    #     "name": "Neon Dream",
        
    #     "stats": [
    #         {
    #             "name": "INT",
    #             "value": 7, 
    #         },
    #         { 
    #             "name": "REF", 
    #             "value": 7, 
    #         },
    #         { 
    #             "name": "DEX", 
    #             "value":  6, 
    #         },
    #         { 
    #             "name": "TECH",
    #             "value": 5,
    #         },
    #         { 
    #             "name": "COOL",
    #             "value": 7,
    #         },
    #         { 
    #             "name": "WILL",
    #             "value": 6, 
    #         },
    #         { 
    #             "name": "LUCK", 
    #             "value": 6, 
    #         },
    #         { 
    #             "name": "MOVE", 
    #             "value": 7, 
    #         },
    #         { 
    #             "name": "BODY", 
    #             "value": 7, 
    #         },
    #         { 
    #             "name": "EMP",  
    #             "value": 5, 
    #         },
    #     ],

    #     "health": {
    #         "hit_points": [
    #             { 
    #                 "name": "HP",
    #                 "value": 53,
    #             }
    #         ],
    #         "armor": [
    #             { 
    #                 "name": "Head",
    #                 "value" : 9, 
    #             },
    #             { 
    #                 "name": "Body",
    #                 "value": 10, 
    #             },
    #         ],
    #     },

    #     "skills": [
    #         {   
    #             "name": "Concentration",
    #             "stat": "WILL",
    #             "value": 10,
    #         },
    #         {
    #             "name": "Perception",
    #             "stat": "INT",
    #             "value": 12,
    #         },
    #         {
    #             "name": "Handgun",
    #             "stat": "REF",
    #             "value": 14,
    #         },
    #         {
    #             "name": "Basic Tech",
    #             "stat": "TECH",
    #             "value": 9,
    #         },
    #         {
    #             "name": "Hacking",
    #             "stat": "TECH",
    #             "value": 15,
    #         },
            
    #     ]

    # }
