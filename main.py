class Package:
    def __init__(self, sender, receiver, weight):
        self.sender = sender
        self.receiver = receiver
        self.weight = weight
        self.delivered = False

    def deliver(self):
        self.delivered = True
        print("Yetkazildi.")

    def get_info(self):
        status = "Yetkazildi" if self.delivered else "Jarayonda"
        return f"{self.sender} -> {self.receiver} | {self.weight}kg | {status}"


class DeliveryService:
    def __init__(self):
        self.packages = []

    def add_package(self, package):
        self.packages.append(package)

    def deliver_all(self):
        for p in self.packages:
            p.deliver()

    def show_packages(self):
        print("\nPaketlar:")
        for p in self.packages:
            print(p.get_info())


def run_delivery():
    service = DeliveryService()

    p1 = Package("Ali", "Vali", 2)
    p2 = Package("Sami", "Karim", 5)

    service.add_package(p1)
    service.add_package(p2)

    service.show_packages()

    service.deliver_all()

    service.show_packages()


run_delivery()
