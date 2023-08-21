import re


phone_numbers=[]
emails=[]
name=[]
file=open("test.txt.txt","r")
def get_num (file):
    numbers=re.compile(r"01[012]\d{8}")

    matnum= numbers.finditer(file.read())

    for match in matnum:
        phone_numbers.append(match)


def get_mail(file):
    mails=re.compile(r"[a-zA-Z0-9 ]+@gmail\.com")


    mate=mails.finditer(file.read())

    for match in mate:
        emails.append(match)
names=re.compile(r"\b[a-zA-Z]+ [a-zA-Z]+")


mate=names.finditer(file.read())

for match in mate:
        name.append(match)








