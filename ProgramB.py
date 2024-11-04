import subprocess
from statistics import median

def programB():
    process = subprocess.Popen(
        ["python", "programA.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    process.stdin.write("Hi\n")
    process.stdin.flush()
    response = process.stdout.readline().strip()
    if response == "Hi":
        print("ProgramA sent Hi")
    list = []
    for _ in range(100):
        process.stdin.write("GetRandom\n")
        process.stdin.flush()
        response = process.stdout.readline().strip()
        number = int(response)
        list.append(int(number))

    process.stdin.write("Shutdown\n")
    process.stdin.flush()
    process.stdin.close()

    list.sort()
    print(list)
    print("Average: " + str(sum(int(x) for x in list ) / len(list)))
    print("Median: " + str(median(list)))

programB()


