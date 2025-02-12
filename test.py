from datetime import datetime

def decide():
    current_time = datetime.now().time()
    if current_time >= datetime.strptime("07:00", "%H:%M").time() and current_time < datetime.strptime("12:00", "%H:%M").time():
        return "Goedemorgen"
    elif current_time >= datetime.strptime("12:00", "%H:%M").time() and current_time < datetime.strptime("18:00", "%H:%M").time():
        return "Goedemiddag"
    elif current_time >= datetime.strptime("18:00", "%H:%M").time() and current_time < datetime.strptime("23:00", "%H:%M").time():
        return "Goedenavond"
    else:
        return None

greeting = decide()
if greeting:
    print(greeting + "! Welkom bij Fonteyn Vakantieparken")
else:
    print("Sorry, de parkeerplaats is s'nachts gesloten")