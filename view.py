def set_disc_position(name):
    position_set = False
    while not position_set:
        position = input(name + ", wähle eine Spalte von 0-6: ")
        try:
            position = int(position)
            if position < 0 or position > 6:
                raise IndexError()
            return position
        except:
            print("Es muss eine Zahl von 0-6 sein!")
