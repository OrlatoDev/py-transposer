allNotes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

relatives = {
    "C": "Am",
    "G": "Em",
    "D": "Bm",
    "A": "F#m",
    "E": "C#m",
    "B": "G#m",
    "F#": "D#m",
    "C#": "A#m",
    "F": "Dm",
    "A#": "Gm",
    "D#": "Cm",
    "G#": "Fm"
}

print("(1) - Transpose")
print("(2) - Capo")
r = int(input("R: "))

if r == 1:
    notes = str(input("Notes: "))
    fromTone = str(input("From tone: "))
    toTone = str(input("To tone: "))

    notes = notes.split(", ")

    if "m" not in fromTone and "m" not in toTone or "m" in fromTone and "m" in toTone:
        iFromTone = allNotes.index(fromTone)
        iToTone = allNotes.index(toTone)

        semitones = iToTone - iFromTone

        notesTransposed = []

        for note in notes:
            iNote = allNotes.index(note)
            IToNote = iNote + semitones

            if IToNote > (len(allNotes) - 1):
                IToNote = IToNote - len(allNotes)

            transposedNote = allNotes[IToNote]
            notesTransposed.append(transposedNote)

        print(notesTransposed)

    else:
        if "m" in fromTone:
            toTone = relatives[toTone]
        
        if "m" in toTone:
            fromTone = relatives[fromTone]

        iFromTone = allNotes.index(fromTone[:fromTone.find("m")])
        iToTone = allNotes.index(toTone[:fromTone.find("m")])

        semitones = iToTone - iFromTone

        notesTransposed = []

        for note in notes:
            iNote = allNotes.index(note)
            IToNote = iNote + semitones

            if IToNote > (len(allNotes) - 1):
                IToNote = IToNote - len(allNotes)

            transposedNote = allNotes[IToNote]
            notesTransposed.append(transposedNote)

        print(notesTransposed)

else:
    fret = int(input("Capo's fret: "))

    notes = str(input("Notes: "))
    notes = notes.split(", ")

    semitones = fret

    notesTransposed = []

    for note in notes:
        iNote = allNotes.index(note)
        IToNote = iNote + semitones

        if IToNote > (len(allNotes) - 1):
            IToNote = IToNote - len(allNotes)

        transposedNote = allNotes[IToNote]
        notesTransposed.append(transposedNote)

    print(notesTransposed)