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

    pseudo_numbers_list = []
    for _ in range(100):
        process.stdin.write("GetRandom\n")
        process.stdin.flush()
        response = process.stdout.readline().strip()
        number = int(response)
        pseudo_numbers_list.append(int(number))

    process.stdin.write("Shutdown\n")
    process.stdin.flush()
    process.stdin.close()
    status = process.poll()
    if status is None:
        print("ProgramA has shut down")

    pseudo_numbers_list.sort()
    print("Pseudo-Random Numbers List")
    print(pseudo_numbers_list)
    print("Average: " + str(sum(int(x) for x in pseudo_numbers_list ) / len(pseudo_numbers_list)))
    print("Median: " + str(median(pseudo_numbers_list)))

programB()


