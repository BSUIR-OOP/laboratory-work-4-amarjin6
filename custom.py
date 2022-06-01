from dotenv import load_dotenv
import os


class Workers:
    def __init__(self, techMaps: str):
        self.techMaps = techMaps

    def toDo(self):
        self.techMaps = ''
        print('Completed!')


class Manufacture:
    def __init__(self, item: str, workers: Workers):
        self.invoice = item
        self.workers = workers

    def produce(self):
        self.workers.toDo()
        self.invoice = ''
        print('Success!')


class Service:
    def __init__(self, manufacture: Manufacture):
        self.manufacture = manufacture

    def repair(self):
        self.manufacture.produce()
        print('Repaired!')


if __name__ == '__main__':
    load_dotenv()
    service = Service(Manufacture(item=os.getenv('item'), workers=Workers(techMaps=os.getenv('techMaps'))))
    service.repair()
