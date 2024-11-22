from collections.abc import Sequence
from abc import ABC, abstractmethod
from typing import Any, ClassVar, TextIO, Generator, Callable
from xml.dom.minidom import Document


class AbstractXMLParser(ABC, Sequence):
    """
    Абстрактный класс XML Парсера
    """
    PARSER: ClassVar[Callable[[str | TextIO], Document] | None] = None

    @abstractmethod
    @classmethod
    def get_parser(cls) -> Callable[[str | TextIO], Document] | None:
        pass

    @abstractmethod
    def get_head(self) -> dict[str, str]:
        pass

    @abstractmethod
    def get_list(self) -> list[dict[str, str]] | None:
        pass

    @abstractmethod
    def get_generator(self) -> Generator[dict[str, str], Any] | None:
        pass
