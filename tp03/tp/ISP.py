from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_document(self, document: str) -> None:
        ...


class Scannable(ABC):
    @abstractmethod
    def scan_document(self, document: str) -> None:
        ...


class Faxable(ABC):
    @abstractmethod
    def fax_document(self, document: str) -> None:
        ...


class BasicPrinter(Printable):
    def print_document(self, document: str) -> None:
        print(f"[Print] {document}")


class AdvancedPrinter(Printable, Scannable, Faxable):
    def print_document(self, document: str) -> None:
        print(f"[Print] {document}")

    def scan_document(self, document: str) -> None:
        print(f"[Scan ] {document}")

    def fax_document(self, document: str) -> None:
        print(f"[Fax  ] {document}")


class Teachable(ABC):
    @abstractmethod
    def teach(self, course: str) -> None:
        ...


class Researchable(ABC):
    @abstractmethod
    def research(self, topic: str) -> None:
        ...


class MedicalPractice(ABC):
    @abstractmethod
    def treat(self, patient: str) -> None:
        ...


class ProfessorResearcher(Teachable, Researchable):
    def teach(self, course: str) -> None:
        print(f"[Teach   ] Course: {course}")

    def research(self, topic: str) -> None:
        print(f"[Research] Topic: {topic}")


class FullTimeResearcher(Researchable):
    def research(self, topic: str) -> None:
        print(f"[Research] Topic: {topic}")


class HospitalProfessorResearcher(MedicalPractice, Teachable, Researchable):
    def teach(self, course: str) -> None:
        print(f"[Teach   ] Course: {course}")

    def research(self, topic: str) -> None:
        print(f"[Research] Topic: {topic}")

    def treat(self, patient: str) -> None:
        print(f"[Medicine] Treating patient: {patient}")


if __name__ == "__main__":
    doc1 = "Document_A.pdf"
    doc2 = "Document_B.pdf"

    basic = BasicPrinter()
    print("BasicPrinter:")
    basic.print_document(doc1)

    pro = AdvancedPrinter()
    print("AdvancedPrinter:")
    pro.print_document(doc2)
    pro.scan_document(doc2)
    pro.fax_document(doc2)

    print("-" * 40)

    prof = ProfessorResearcher()
    print("ProfessorResearcher:")
    prof.teach("Algorithms")
    prof.research("Graph Neural Networks")

    ronly = FullTimeResearcher()
    print("FullTimeResearcher:")
    ronly.research("Quantum Computing")

    hosp = HospitalProfessorResearcher()
    print("HospitalProfessorResearcher:")
    hosp.teach("Medical Imaging")
    hosp.research("AI for Radiology")
    hosp.treat("Patient #42")
