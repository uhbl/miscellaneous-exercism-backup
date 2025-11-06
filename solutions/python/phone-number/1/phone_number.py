if False:
    class PhoneNumber:
        def __init__(self, number):
            initial = ""
            for i in number:
                if i.isalpha():
                    raise ValueError("letters not permitted")
                elif i in ["{", "}", "[", "]", "!", "@", "#", "$", "%", "^", "&", "*", "_", "=", "|", "\\", "/", ":", ";", "\"", "'", "<", ">", ",", "?", "~"]:
                    raise ValueError("punctuations not permitted")
                elif i.isdigit():
                    initial += i
            for i, k in enumerate(initial):
                if i == 0 and k != "1":
                    raise ValueError("11 digits must start with 1")
                elif i == 1 and k == "0":
                    raise ValueError("exchange code cannot start with zero")
                elif i == 1 and k == "1":
                    raise ValueError("exchange code cannot start with one")
                elif i == 4 and k == "0":
                    raise ValueError("area code cannot start with zero")
                elif i == 4 and k == "1":
                    raise ValueError("area code cannot start with one")
            if len(initial) < 11:
                raise ValueError("must not be fewer than 10 digits")
            elif len(initial) > 11:
                raise ValueError("must not be greater than 11 digits")
            self.number = initial[1::]

class PhoneNumber:
    def __init__(self, number):
        digits = ""
        allowed = set("0123456789.+- ()")

        # Filter and validate characters
        for ch in number:
            if ch.isalpha():
                raise ValueError("letters not permitted")
            if ch not in allowed and not ch.isspace():
                raise ValueError("punctuations not permitted")
            if ch.isdigit():
                digits += ch

        # Length validation
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")

        # Handle country code
        if len(digits) == 11:
            if digits[0] != "1":
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]

        # Area and exchange code validation
        if digits[0] == "0":
            raise ValueError("area code cannot start with zero")
        if digits[0] == "1":
            raise ValueError("area code cannot start with one")
        if digits[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = digits
        self.area_code = digits[:3]

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
