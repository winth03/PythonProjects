try:
    mode = input("Mode (av, a): ")
    mode = mode.lower()
    while True:
        if mode == "av":
            sum = 0
            for i in range(3):
                sum += float(input())
            print("Average : {:.2f}".format(sum / 3))
        elif mode == "a":
            s = float(input("s : "))
            t = float(input("t : "))
            print("Accelration : {:.2f}".format(2 * s / t ** 2))
        else:
            print("error")
            mode = input("Mode (av, a): ")
            mode = mode.lower()
except KeyboardInterrupt:
    print("Program End")
    input()