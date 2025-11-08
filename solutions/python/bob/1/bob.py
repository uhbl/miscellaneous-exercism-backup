if False:
    def response(hey_bob):
        hey_bob = hey_bob.strip()
        silence = True
        for i in hey_bob:
            if i.isalnum():
                silence = False
        if hey_bob == "" or silence:
            return "Fine. Be that way!"
        elif not hey_bob.isupper() and hey_bob[-1] == "?":
            return "Sure."
        elif hey_bob.isupper() and not hey_bob[-1] == "?":
            return "Whoa, chill out!"
        elif hey_bob.isupper() and hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        else:
            return "Whatever."

def response(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob:
        return "Fine. Be that way!"
    elif hey_bob.endswith("?"):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
