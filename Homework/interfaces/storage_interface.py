from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List, Dict


class StorageInterface(ABC):
    @abstractmethod
    def load_members(self) -> List[Dict[str, Any]]:
        ...

    @abstractmethod
    def load_events(self) -> List[Dict[str, Any]]:
        ...

    @abstractmethod
    def load_subscriptions(self) -> List[Dict[str, Any]]:
        ...

    @abstractmethod
    def load_donations(self) -> List[Dict[str, Any]]:
        ...
