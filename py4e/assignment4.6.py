#介紹function寫法

def computepay(h, r):
    if h <= 40:
        pay = h *r
    elif h > 40:
        regpay = 40*r
        overpay = (h-40)*(r*1.5)
        grosspay = regpay + overpay
        return grosspay

h = input("Enter Hours:")
h = float(h)
r = input("Enter rate:")
r = float(r)
p = computepay(h, r)
print("Pay", p)
