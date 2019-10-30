def dictionaries(dict_type):
    genders = [
        ('None'," "),
        ('male', "male"),
        ('female', "female"),
        ('non_binary', "non-binary/third gender"),
        ('not_available', "prefer not to describe"),
    ]
    yearinschool = [
        ('None'," "),
        ('first', "first"),
        ('second', "second"),
        ('third', "third"),
        ('fourth', "fourth"),
        ('advanced', "advanced"),
    ]
    classchoice = [
        ('----',"----"),

    ]
    classchoiceind = [
         '----',
    ]
    hesfchoice = [
        ('----',"----"),
    ]
    if dict_type == "gender_type": 
        return (genders)
    if dict_type == "year_type": 
        return (yearinschool)
    if dict_type == "class_type": 
        return (classchoice)
    if dict_type == "hesf_type": 
        return (hesfchoice)
    if dict_type == "class_index":
        return (classchoiceind)


