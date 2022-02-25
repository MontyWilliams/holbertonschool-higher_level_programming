
def
    try:
        quotient = a / b
    except:
        quotient = None
    finally:
        print("Inside results: {}".format(quotient))
        return quotient
