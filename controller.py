import subprocess
from statistics import median


def controller():
    process = subprocess.Popen(
        ["python", "generator.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    test_hi(process)

    pseudo_numbers_list = []
    for _ in range(100):
        pseudo_numbers_list.append(get_number(process))

    test_shutdown(process)

    pseudo_numbers_list.sort()
    print("Pseudo-Random numbers list: ")
    print(pseudo_numbers_list)

    average_from_list(pseudo_numbers_list)
    median_from_list(pseudo_numbers_list)


def test_hi(process):
    process.stdin.write("Hi\n")
    process.stdin.flush()
    response = process.stdout.readline().strip()
    if response == "Hi":
        print("generator sent Hi")


def get_number(process):
    process.stdin.write("GetRandom\n")
    process.stdin.flush()
    response = process.stdout.readline().strip()
    return int(response)


def test_shutdown(process):
    process.stdin.write("Shutdown\n")
    process.stdin.flush()
    process.stdin.close()
    status = process.poll()
    if status is None:
        print("generator has shut down")


def average_from_list(list):
    print("Average: " + str(sum(int(x) for x in list) / len(list)))


def median_from_list(list):
    print("Median: " + str(median(list)))


controller()
