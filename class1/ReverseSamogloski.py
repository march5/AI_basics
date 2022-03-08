def reverse(slowo):
    noweslowo=""
    for litera in slowo:
        if litera in ("aeuioy"):
            noweslowo=litera+noweslowo
    return (noweslowo)
print(reverse("jakiesslowo"))