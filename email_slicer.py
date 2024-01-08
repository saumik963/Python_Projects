def email_slicer():
    email=input("Enter Email: ")

    (username,domain)=email.split("@")
    (domain,extention)=domain.split(".")


    print("Username :", username)
    print("Domain :", domain)
    print("Extention :", extention)

email_slicer()