from lib import get_itineraries
import data

if __name__ == '__main__':
    for itinerary in get_itineraries(data.sicily):
        print("#" * 24)
        print(itinerary)
        print("")
