ticket = input("是否买票了？Y/N：")
if ticket == "Y":
    print("可以进站。")
    safe = input("安检是否通过？Y/N：")
    if safe == "Y":
        print("可以进入候车室。")
    else:
        print("安检未通过。")
else:
    print("没有买票。")
