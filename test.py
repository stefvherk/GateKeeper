from datetime import datetime

def decide():
    h = datetime.now().hour
    return ("Goedemorgen" if 7 <= h < 12 else "Goedemiddag" if 12 <= h < 18 else "Goedenavond" if 18 <= h < 23 else None)

greeting = decide()
print(f"{greeting}! Welkom bij Fonteyn Vakantieparken" if greeting else "Sorry, de parkeerplaats is s'nachts gesloten")