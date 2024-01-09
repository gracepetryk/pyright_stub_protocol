from abc import abstractmethod
from typing import Protocol


class SupportsSomething(Protocol):
    @abstractmethod
    def something(self) -> int: ...
