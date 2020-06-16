def exception_function(divisor):
    try:
        result=5/divisor
    except (ZeroDivisionError,TypeError) as e:
        return f"Some error occured, {e}"
    return result

print(exception_function(5))
print(exception_function(0))
print(exception_function("asd"))