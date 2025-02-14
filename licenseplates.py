from datetime import datetime

license_plates = [
    "AB-12-CD", "EF-34-GH", "IJ-56-KL", "MN-78-OP", "QR-90-ST",
    "UV-12-WX", "YZ-34-AB", "CD-56-EF", "GH-78-IJ", "KL-90-MN",
    "OP-12-QR", "ST-34-UV", "WX-56-YZ", "AB-78-CD", "EF-90-GH",
    "IJ-12-KL", "MN-34-OP", "QR-56-ST", "UV-78-WX", "YZ-90-AB",
    "CD-12-EF", "GH-34-IJ", "KL-56-MN", "OP-78-QR", "ST-90-UV",
    "WX-12-YZ", "AB-34-CD", "EF-56-GH", "IJ-78-KL", "MN-90-OP"
]

def decide():
    h = datetime.now().hour
    return (
        "Goedemorgen" if 7 <= h < 12 else
        "Goedemiddag" if 12 <= h < 18 else
        "Goedenavond" if 18 <= h < 23 else
        None
)

while True:
    license_plate = input("Voer uw kenteken in: ")
    if license_plate.lower() == 'exit':
        break

    greeting = decide() if license_plate in license_plates else None
    print(
        f"{greeting}! Welkom bij Fonteyn Vakantieparken" if greeting else
        "Sorry, de parkeerplaats is s'nachts gesloten" if greeting is None else
        "U heeft helaas geen toegang tot het parkeerterrein"
    )