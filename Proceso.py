class Proceso:
    def __init__(self, pid: int, vruntime: float):
        self.pid = pid
        self.vruntime = vruntime

    def __repr__(self):
        return f"Proceso(pid={self.pid}, vruntime={self.vruntime})"
        