
def fun(num):
    try:
        result = 100 / num
        print("Result: ", result)
    except (ZeroDivisionError, TypeError) as e:
        print("Error:", e)

fun(2)
fun(8)
fun("r")
fun("7")