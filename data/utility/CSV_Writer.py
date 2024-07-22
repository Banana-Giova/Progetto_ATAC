import csv

def csv_passenger(data:list[list[str]]):
    header = ['passenger_id', 'name', 'surname']

    with open('scripts/data/load0.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(header)
        writer.writerows(data)

def csv_line(data:list[list[str]]):
    header = ['line_number', 'name']

    with open('scripts/data/load1.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(header)
        writer.writerows(data)

def csv_stop(data:list[list[str]]):
    header = ['stop_id', 'name', 'latitude', 'longitude']

    with open('scripts/data/load2.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(header)
        writer.writerows(data)

def csv_bus(data:list[list[str]]):
    header = ['bus_id', 'capacity']

    with open('scripts/data/load3.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(header)
        writer.writerows(data)

def csv_driver(data:list[list[str]]):
    header = ['driver_id', 'name', 'surname']

    with open('scripts/data/load4.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(header)
        writer.writerows(data)



csv_passenger([
        ['L0R3NZ0', 'Lorenzo', 'Maggi'],
        ['L30N', 'Francisco', 'Felici'],
        ['D4N13L3', 'Daniele', 'Pietropaolo']
    ])
csv_line([
        ['682', 'Ponte Milvio'],
        ['451', 'Ponte Mammolo'],
        ['558', 'Gardenie']
    ])
csv_stop([
        ['R0M4', 'Romanisti', 42.3, 45.5],
        ['PR1M4', 'Primavera', 32.3, 31.9],
        ['P40L0', 'San Paolo', 332.3, 311.1],
    ])
csv_bus([
        ['7077', 60],
        ['4343', 40],
        ['2002', 30]
    ])
csv_driver([
        ['4NDR34', 'Andrea', 'Bardi'],
        ['G4L3R10', 'Galerio', 'Garpisi'],
        ['B4RDH', 'Bardh', 'Prenkaj']
    ])