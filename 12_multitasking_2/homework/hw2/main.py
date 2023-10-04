from subprocess import getoutput
from re import findall

def process_count(username: str) -> int:
    """ Количество процессов, запущенных из-под текущего пользователя """
    cmd = f"ps -u {username} -f | wc -l"
    result = getoutput(cmd)
    return int(result) - 1  # минус строку с названиями столбцов


def total_memory_usage(root_pid: int, total_memory=0) -> float:
    """
    Сколько памяти (в %) потребляет дерево процесса с корнем root_pid.
    Медленный способ из-за рекурсии.
    :param root_pid: int
    :param total_memory: float
    :return: float
    """
    cmd = "ps axo pid,ppid,pmem | grep -v PID"
    # grep -v PID: убираем строку с названиями столбцов PID, PPID, %MEM
    result = getoutput(cmd).split('\n')

    for line in result:
        item = line.split()
        pid, ppid, memory = int(item[0]), int(item[1]), float(item[2])
        if pid == root_pid:
            total_memory += memory
        elif ppid == root_pid:
            total_memory += total_memory_usage(root_pid=pid)

    return round(total_memory, 3)


def total_memory_usage_re(root_pid: int) -> float:
    """ Более быстрый вариант с pstree и re """
    cmd = f"pstree -p {root_pid}"
    output = getoutput(cmd)
    result = findall(r'\(\d{1,8}\)', output)
    result = [int(i[1:-1]) for i in result]
    # result.sort()

    cmd = "ps axo pid,pmem | grep -v PID"
    output = getoutput(cmd).split('\n')
    total_memory = 0
    for line in output:
        item = line.split()
        pid, memory = int(item[0]), float(item[1])
        if pid in result:
            total_memory += memory

    return round(total_memory, 3)


if __name__ == "__main__":
    print(process_count('root'))
    print(total_memory_usage(1))
    print(total_memory_usage_re(1))
