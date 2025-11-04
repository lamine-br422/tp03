from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def write_log(self, msg: str) -> None:
        pass


class FileLogger(Logger):
    def write_log(self, msg: str) -> None:
        print(f"[FILE] {msg}")


class DBLogger(Logger):
    def write_log(self, msg: str) -> None:
        print(f"[DATABASE] {msg}")


class SystemApp:
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    def run(self) -> None:
        self._logger.write_log("System is now running...")


if __name__ == "__main__":
    app = SystemApp(FileLogger())
    app.run()

    app_db = SystemApp(DBLogger())
    app_db.run()
