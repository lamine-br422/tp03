from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailService(NotificationService):
    def send(self, message: str) -> None:
        print(f"[EMAIL] {message}")


class SMSService(NotificationService):
    def send(self, message: str) -> None:
        print(f"[SMS  ] {message}")


class PushService(NotificationService):
    def send(self, message: str) -> None:
        print(f"[PUSH ] {message}")


class Notification:
    def __init__(self, service: NotificationService):
        self._service = service

    def set_service(self, service: NotificationService) -> None:
        self._service = service

    def send(self, message: str) -> None:
        self._service.send(message)


if __name__ == "__main__":
    email = EmailService()
    sms = SMSService()
    push = PushService()

    notifier = Notification(email)
    notifier.send("Hello via Email!")

    notifier.set_service(sms)
    notifier.send("Hello via SMS!")

    notifier.set_service(push)
    notifier.send("Hello via Push!")
