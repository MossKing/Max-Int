#Búa þarf til int input breytu og breytu til að halda utan um stærstu töluna sem hefur komið.
#Nota While loop til að keyra forritið þangað til að tala < 0 kemur fyrir og prenntar síðan max_int út
#Nota if/elif/else til að max_int taki hæsta gildið

num = int(input("Enter a number: "))
max_int = 0

while num > 0:
    if max_int < num:
        max_int = num
    num = int(input("Enter a number: "))
print(max_int)