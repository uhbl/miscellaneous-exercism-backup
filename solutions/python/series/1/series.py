def slices(series, length):
    if series == "":
        raise ValueError("series cannot be empty")
    
    if length == 0:
        raise ValueError("slice length cannot be zero")
    
    if length < 0:
        raise ValueError("slice length cannot be negative")
    
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    
    start = 0
    end = length
    final_list = []

    while end <= len(series):
        final_list.append(series[start:end])
        start += 1
        end += 1
    
    return final_list