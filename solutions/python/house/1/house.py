dict_id = {
    1: "This is the house that Jack built.",
    2: "that lay in the house that Jack built.",
    3: "This is the malt",
    4: "that ate the malt",
    5: "This is the rat",
    6: "that killed the rat",
    7: "This is the cat",
    8: "that worried the cat",
    9: "This is the dog",
    10: "that tossed the dog",
    11: "This is the cow with the crumpled horn",
    12: "that milked the cow with the crumpled horn",
    13: "This is the maiden all forlorn",
    14: "that kissed the maiden all forlorn",
    15: "This is the man all tattered and torn",
    16: "that married the man all tattered and torn",
    17: "This is the priest all shaven and shorn",
    18: "that woke the priest all shaven and shorn",
    19: "This is the rooster that crowed in the morn",
    20: "that kept the rooster that crowed in the morn",
    21: "This is the farmer sowing his corn",
    22: "that belonged to the farmer sowing his corn",
    23: "This is the horse and the hound and the horn"
    }

if False:
    def recite(start_verse, end_verse):
        init_list = []

        for i in range(start_verse - 1, end_verse):
            temp = list(range(0, 2*i+1, 2))
            temp.remove(0)
            temp.append(2*i+1)
            init_list.append(temp[::-1])

        plchldr_str = ""

        for i in init_list:
            for k in i:
                plchldr_str += dict_id[k]
                plchldr_str += " "
            plchldr_str += " "
        
        return plchldr_str.strip(" ")

# Sometimes those eazy problems get crazy

PARTS = [
    "the house that Jack built.",
    "the malt that lay in the house that Jack built.",
    "the rat that ate the malt that lay in the house that Jack built.",
    "the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built."
]

def recite(start, end):
    return [ "This is " + PARTS[i] for i in range(start-1, end) ]