"use strict";

// The maximum is exclusive and the minimum is inclusive
function getRandomInt(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
}

function rollD10() {
   return getRandomInt(1, 11);
}

function rollD6() {
   return getRandomInt(1, 7);
}

function render_stat(stat, stat_action=null) {
   let label = document.createElement("td");
   label.className = "skill-name";
   label.innerHTML = stat.name;

   let level = document.createElement("td");
   level.className = "skill-level";
   level.innerHTML = stat.value;

   if (stat_action === null) {
      let action_button = document.createElement("button");
      action_button.className = "action-button make-check";
      action_button.role = "button";
      action_button.innerHTML = "Make Check";
      action_button.onclick = stat.handleClick;

      stat_action = document.createElement("div");
      stat_action.className = "stat-action";
      stat_action.append(action_button);
   }

   let row = document.createElement("tr");
   row.append(label, level, stat_action);

   return row;
}

class Stat {
   constructor(name, value = 0) {
      this.name = name;
      this.value = value;
   }
   
   handleClick = () => {
      this.makeCheck();
   }
   
   makeCheck() {
      let dice_result = rollD10();
      
      let check_result = new StatCheckResult(this, dice_result);
      game_log.logEvent(check_result);
      game_log.render();
      // alert(check_result);
   }

   render() {
      return render_stat(this);
   }
}

class Skill {
   constructor(name, stat, value = 0) {
      this.name = name;
      this.stat = stat;
      this.value = value;
   }
   
   handleClick = () => {
      this.makeCheck();
   }

   makeCheck() {
      let dice_result = rollD10();

      let check_result = new SkillCheckResult(this, dice_result);
      game_log.logEvent(check_result);
      game_log.render();
      // alert(check_result);
   }

   render() {
      return render_stat(this);
   }
}

// Attributes are character values that change during the course of gameplay, 
// like Health or Armor 
class Attribute {
   constructor(name, value = 0) {
      this.name = name;
      this.value = value;
   }

   
   handleDecreaseClick = () => {
      this.changeValue(-1);
      renderHealthBox();
   }
   
   handleIncreaseClick = () => {
      this.changeValue(1);
      renderHealthBox();
   }

   changeValue(amount) {
      this.value += amount;
   }

   render() {
      let increase_button = document.createElement("button");
      increase_button.className = "action-button increase-attribute";
      increase_button.role = "button";
      increase_button.innerHTML = "+"
      increase_button.onclick = this.handleIncreaseClick;

      let decrease_button = document.createElement("button");
      decrease_button.className = "action-button decrease-attribute";
      decrease_button.role = "button";
      decrease_button.innerHTML = "-";;
      decrease_button.onclick = this.handleDecreaseClick;

      let stat_action = document.createElement("div");
      stat_action.className = "stat-action";
      stat_action.append(increase_button);
      stat_action.append(decrease_button);

      return render_stat(this, stat_action);
   }
}

class SkillCheckResult {
   constructor(skill, dice_result) {
      this.skill_name = skill.name;
      this.skill_value = skill.value;
      this.stat_name = skill.stat.name;
      this.stat_value = skill.stat.value;
      this.dice_result = dice_result;

      if (dice_result == 1) {
         this.critical = "FAILURE";
      } else if (dice_result == 10) {
         this.critical = "SUCCESS";
      } else {
         this.critical = "NONE";
      }

      this.result_value = this.skill_value + this.dice_result + this.stat_value;
   }

   toString() {
      let crit_message = "";
      if (this.critical == "FAILURE") {
         crit_message = "\nCritical Failure!";
      } else if (this.critical == "SUCCESS") {
         crit_message = "\nCritical Success!";
      }
      
      return `Player made ${this.skill_name} check.
${this.skill_name}: ${this.skill_value}
${this.stat_name}: ${this.stat_value}
Dice roll: ${this.dice_result} ${crit_message}

Result: ${this.result_value}
`;

   }
}

class StatCheckResult {
   constructor(stat, dice_result) {
      this.stat_name = stat.name;
      this.stat_value = stat.value;
      this.dice_result = dice_result;

      if (dice_result == 1) {
         this.critical = "FAILURE";
      } else if (dice_result == 10) {
         this.critical = "SUCCESS";
      } else {
         this.critical = "NONE";
      }

      this.result_value = this.stat_value + this.dice_result;
   }

   render() {
      let wrapper = document.createElement("div");
      
      let head = document.createElement("div");
      head.innerHTML = `Player made ${this.stat_name} check.`;
      wrapper.append(head);
      
      let stat_info = document.createElement("div");
      stat_info.innerHTML = `${this.stat_name}: ${this.stat_value}`;
      wrapper.append(stat_info);

      let roll_info = document.createElement("div");
      roll_info.innerHTML = `Dice roll: ${this.dice_result}`;
      wrapper.append(roll_info);

      if (this.critical == "FAILURE") {
         
         let crit = document.createElement("div");
         crit.className = "critical-failure";
         crit.innerHTML = "Critical Failure!";
         wrapper.append(crit);

      } else if (this.critical == "SUCCESS") {
         
         let crit = document.createElement("div");
         crit.className = "critical-success";
         crit.innerHTML = "Critical Success!";
         wrapper.append(crit);

      }

      let result = document.createElement("div");
      result.className = "check-result";
      result.innerHTML = `Result: ${this.result_value}`
      wrapper.append(result);

      return wrapper;
   }

   toString() {
      let crit_message = "";
      if (this.critical == "FAILURE") {
         crit_message = "\nCritical Failure!";
      } else if (this.critical == "SUCCESS") {
         crit_message = "\nCritical Success!";
      }
      
      return `Player made ${this.stat_name} check.
${this.stat_name}: ${this.stat_value}
Dice roll: ${this.dice_result} ${crit_message}

Result: ${this.result_value}
`;

   }
}

class GameLog {
   constructor(events = []) {
      this.events = events;
   }

   logEvent(event) {
      this.events.push(event) 
   }

   render() {
      let log_box = document.querySelector("#log .log-box");
      let log_lines = this.events.map((event) => {
         let elem = document.createElement("div");
         elem.className = "log-entry";
         if (typeof event.render === "function") {
            elem.append(event.render());
         } else {
            elem.innerHTML = event.toString();
         }
         return elem;
      });

      log_box.replaceChildren(...log_lines);
   }
}

let game_log = new GameLog(["Player has joined the game!"])

let stats = {
   "INT": new Stat("INT", 7),
   "REF": new Stat("REF", 7),
   "DEX": new Stat("DEX", 6),
   "TECH": new Stat("TECH", 5),
   "COOL": new Stat("COOL", 7),
   "WILL": new Stat("WILL", 6),
   "LUCK": new Stat("LUCK", 6),
   "MOVE": new Stat("MOVE", 7),
   "BODY": new Stat("BODY", 7),
   "EMP": new Stat("EMP", 5),
};

let skills = [
   new Skill("Concentration", stats["WILL"], 10),
   new Skill("Perception", stats["INT"], 12),
   new Skill("Handgun", stats["REF"], 14),
   new Skill("Basic Tech", stats["TECH"], 9),
];

let health = [
   new Attribute("Hit Points", 30),
   new Attribute("Armor", 8),
]

function renderStatBox() {
   let stat_box = document.querySelector("#stats .stat-box tbody");
   let stat_list = Object.values(stats).map((stat) => stat.render());
   stat_box.replaceChildren(...stat_list);
}

function renderHealthBox() {
   let health_box = document.querySelector("#health .stat-box tbody");
   let health_list = health.map((attribute) => attribute.render());
   health_box.replaceChildren(...health_list);
}

function renderSkillBox() {
   let skill_box = document.querySelector("#skills .stat-box tbody");
   let skill_list = skills.map((skill) => skill.render());
   skill_box.replaceChildren(...skill_list);
}

window.onload = function() {

   renderStatBox();
   renderHealthBox();
   renderSkillBox();

   game_log.render();

   // document.querySelector('#character-sheet').style.display = 'none';
   // document.querySelector('#character-sheet').style.display = 'block';

}
