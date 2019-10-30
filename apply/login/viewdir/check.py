import hashlib

def hash_code(s, salt='*********'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def hesf_choice_null(user):
    message = "You may select Physical Education as a 5th class."
    complete = ""
    if user.hesfchoice == "----":
        return message
    else: 
        return complete

def class_choice_null(user):
    message = "You have not selected four courses for the program."
    repeat = "Please do not select two identical courses"
    complete = "You have successfully selected four classes!"
    classchoices = []
    classlist = [user.classchoice1, user.classchoice2, user.classchoice3, user.classchoice4]
    for i in classlist:
        if i == "----":
            return message
        if i in classchoices:
            return repeat
        classchoices.append(i)
    return complete

def upload_null(user):
    message = []
    filenames = [user.ps_uploaded, user.rl_uploaded, user.md_uploaded]
    filetypes = ["personal statement", "letter of recommendation", "medication background"]
    for i in range(0,3):
        if filenames[i] == "Ready for upload":
            message.append("Please upload your %s"%filetypes[i])
        else: 
            message.append("You have uploaded %s as your %s" % (filenames[i], filetypes[i]))
    return message

