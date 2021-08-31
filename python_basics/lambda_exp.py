
# def check_password(password):
#     if len(password) < 8:
#         return 'SHORT_PASSWORD'

#     if not any(c.isupper() for c in password):
#         return 'NO_CAPITAL_LETTER_PASSWORD'

#     return True

lambdas = [ 
    lambda x: 'SHORT_PASSWORD' if len(x) < 8 else None,
    lambda x: 'NO_CAPITAL_LETTER_PASSWORD' if not any(ch.isupper() for ch in x) else None
]

def check_password_using_lambda(password):

    for f in lambdas:
        if f(password) is not None:
            return f(password)

    return True

print( check_password_using_lambda('123') )            # SHORT_PASSWORD
print( check_password_using_lambda('12356789f') )      # NO_CAPITAL_LETTER_PASSWORD
print( check_password_using_lambda('123456789fF') )    # True

