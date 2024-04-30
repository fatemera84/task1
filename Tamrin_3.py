#اول ادعا های هر شخص رو توی آرایه ذخیره میکنیم 
def suspects():
    a1 = ["true", "false", "false"]
    a2 = ["false", "true", "false"]
    a3 = ["false", "false", "true"]
    b1 = ["false", "true", "false"]
    b2 = ["true", "false", "false"]
    b3 = ["false", "false", "true"]
    c1 = ["false", "true", "false"]
    c2 = ["true", "false", "false"]
    c3 = ["false", "false", "true"]
    d1 = ["false", "true", "false"]
    d2 = ["false", "false", "true"]
    d3 = ["true", "false", "false"]

    true_count = 0
    false_count = 0
#تحلیل ادعاهاو مقایسه اونایی که تناقض دارن با هم
    while true_count != 9 or false_count != 9:
        if a2[0] == "true":
            b3[0] = "false"
            false_count += 1
        if a2[1] == "true":
            b1[0] = "false"
            false_count += 1
        if a2[2] == "true":
            b2[0] = "false"
            false_count += 1

        if b1[0] == "true":
            c3[0] = "false"
            false_count += 1
        if b1[1] == "true":
            c1[0] = "false"
            false_count += 1
        if b1[2] == "true":
            c2[0] = "false"
            false_count += 1

        if c3[0] == "true":
            a2[0] = "false"
            false_count += 1
        if c3[1] == "true":
            a3[0] = "false"
            false_count += 1
        if c3[2] == "true":
            a1[0] = "false"
            false_count += 1

        if a1[0] == "true" and c2[0] == "true":
            b3[1] = "false"
            false_count += 1

        if b2[0] == "true" and c1[0] == "true":
            a3[1] = "false"
            false_count += 1

        if c2[0] == "true" and a3[0] == "true":
            b2[1] = "false"
            false_count += 1

        if a2[0] == "false" and b3[0] == "false":
            c1[1] = "true"
            true_count += 1

        if b2[0] == "false" and a3[0] == "false":
            c2[1] = "true"
            true_count += 1

        if c2[0] == "false" and a3[0] == "false":
            b2[1] = "true"
            true_count += 1

        if a1[0] == "true" and b2[0] == "false":
            c3[1] = "true"
            true_count += 1

        if b1[0] == "true" and c3[0] == "false":
            a2[1] = "true"
            true_count += 1

        if c3[0] == "true" and a2[0] == "false":
            b1[1] = "true"
            true_count += 1

        if d1[0] == "true":
            a1[0] = "true"
            true_count += 1
        if d2[0] == "true":
            a2[0] = "true"
            true_count += 1
        if d3[0] == "true":
            a3[0] = "true"
            true_count += 1

    if true_count == 9 and false_count == 9:
        print("The thief is C")

suspects()

