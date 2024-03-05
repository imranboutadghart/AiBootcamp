from datetime import datetime
print("Seconds since January 1, 1970:", end=" ")
print("{:,.4f}".format(datetime.timestamp(datetime.now())), end=" or ")
print("{:.2e}".format(datetime.timestamp(datetime.now())), end="")
print(" in scientific notation")
date = datetime.now()
formatted = date.strftime("%b %d %Y")
print(formatted)
