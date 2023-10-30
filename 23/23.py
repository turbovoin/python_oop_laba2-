class Validator:
    def isEmail(self, email):
        if str(email).find('email.') > -1:
            return True
        else:
            return False

validator = Validator()
print(validator.isEmail("Dima@email.com"))
print(validator.isEmail("Dima@eail.com"))
