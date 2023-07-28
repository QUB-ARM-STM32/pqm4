import os

def SpeedSignTime(name: str):
    keyGenCycles = []
    signCycles = []
    verifyCycles = []

    for type in os.listdir("./benchmarks/speed/crypto_sign/" + name + "/"):
        for data in os.listdir("./benchmarks/speed/crypto_sign/" + name + "/" + type + "/"):
            with open("./benchmarks/speed/crypto_sign/" + name + "/" + type + "/" + data) as f:
                f.readline()
                keyGenCycles.append(int(f.readline().split()[0]))
                f.readline()
                signCycles.append(int(f.readline().split()[0]))
                f.readline()
                verifyCycles.append(int(f.readline().split()[0]))

        # print the results for this folder
        keyGenTime = CalcTime(keyGenCycles, 120)
        signTime = CalcTime(signCycles, 120)
        verifyTime = CalcTime(verifyCycles, 120)
        print(name + "-" + type)
        print("KeyGen: " + str(round(keyGenTime, 3)) + "s")
        keyGenCycles.clear()

        print("Sign: " + str(round(signTime, 3)) + "s")
        signCycles.clear()

        print("Verify: " + str(round(verifyTime, 3)) + "s")
        verifyCycles.clear()

        print("Total: " + str(round(keyGenTime + signTime + verifyTime, 3)) + "s\n")


def CalcTime(cycles: list, speed: int) -> float:
    """
    Takes the cycles calculates the average and return the time in seconds
    :param cycles: list of cycles
    :param speed: speed of the processor in MHz
    :return: time in seconds
    """    

    avg = sum(cycles) / len(cycles)
    return avg * 1.0 / (speed * 1000000)


'''
Loads all the benchmark data and produces a rough execution time
'''
def main():
    SpeedSignTime("falcon-1024")


main()