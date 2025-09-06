def who_is_paying(name):
    truncated_name = [name]
    if len(name) > 2:
        truncated_name.append(name[0] + name[1])

    return truncated_name

print(who_is_paying("Me"))
