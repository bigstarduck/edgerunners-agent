from db import *

with app.app_context():
    db.create_all()

    int_stat = Stat(name="INT")
    ref_stat = Stat(name="REF")
    dex_stat = Stat(name="DEX")
    tech_stat = Stat(name="TECH")
    cool_stat = Stat(name="COOL")
    will_stat = Stat(name="WILL")
    luck_stat = Stat(name="LUCK")
    body_stat = Stat(name="BODY")
    emp_stat = Stat(name="EMP")
    
    concentration_skill = Skill(name="Concentration", stat=will_stat)
    perception_skill = Skill(name="Perception", stat=int_stat)
    handgun_skill = Skill(name="Handgun", stat=ref_stat)
    basic_tech_skill = Skill(name="Basic_tech", stat=tech_stat)
    hacking_skill = Skill(name="Hacking", stat=tech_stat)

    db.session.add(
        Character(
            name = "Neon Dream",
            stats = [
                CharacterStat(stat=int_stat,  value=7), 
                CharacterStat(stat=ref_stat,  value=7), 
                CharacterStat(stat=dex_stat,  value=6), 
                CharacterStat(stat=tech_stat, value=5), 
                CharacterStat(stat=cool_stat, value=7), 
                CharacterStat(stat=will_stat, value=6), 
                CharacterStat(stat=luck_stat, value=6), 
                CharacterStat(stat=body_stat, value=7), 
                CharacterStat(stat=emp_stat,  value=5), 
            ],
            skills = [
                CharacterSkill(skill=concentration_skill, value=10), 
                CharacterSkill(skill=perception_skill,    value=12), 
                CharacterSkill(skill=handgun_skill,       value=14), 
                CharacterSkill(skill=basic_tech_skill,    value=9 ),  
                CharacterSkill(skill=hacking_skill,       value=15), 
            ],
            health = [
                Health(location="Hp", hp=35),
            ],
            armor = [
                Armor(location='Head', hp=7),
                Armor(location='Body', hp=12),
            ],
        )
    )

    db.session.commit()
