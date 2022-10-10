
def func_attributes(num):
    intermediate_var = num ** 2 + num + 1

    if intermediate_var % 2:
        y = intermediate_var ** 3
    else:
        y = intermediate_var ** 3 + 1

    func_attributes.optional_return = intermediate_var
    func_attributes.is_awesome = 'This function attribute is awesome'

    return y


ans = func_attributes(3)
print(ans)

print(func_attributes.optional_return)
print(func_attributes.is_awesome)
