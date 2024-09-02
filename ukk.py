calls = 0


def count_calls():
    global calls
    calls = 1


def string_info(name):
    return (len(name), name.upper(), name.lower())



print(string_info("string"))



def is_contains(name):
    return [list(name)]


print(is_contains("list_to_search",))

print(calls)