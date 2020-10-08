import random
import time
from threading import Thread


class HandleData(Thread):

    SIZE = 5
    NAMES = ['a', 'b', 'c', 'd', 'e']
    NUMBERS = [1, 2, 3, 4, 5]

    def __init__(self, prom_client):
        super().__init__(daemon=False)

        self.prom_client = prom_client
        self.name_and_number_dict = {}

    def generate_new_dict(self):
        self.name_and_number_dict.clear()

        for i in range(self.SIZE):
            name = random.choice(self.NAMES)
            number = random.choice(self.NUMBERS)

            self.name_and_number_dict[name] = number
            # print(self.nameAndNumberDict)

        self.prom_client.collectors_handler.custom_collector.update(self.name_and_number_dict)

    def run(self):
        while True:
            self.generate_new_dict()
            print(self.name_and_number_dict)

            time.sleep(4)


if __name__ == '__main__':
    handle_data = HandleData()
    handle_data.start()

    handle_data.join()