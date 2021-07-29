from lib import get_itineraries, Attraction, Ride
import data

if __name__ == '__main__':
    for itinerary in get_itineraries(data.sicily):
        print("#" * 24)
        print("Steps:")
        duration = 0
        cost = 0
        equipment = set()
        for step in itinerary:
            if isinstance(step, Attraction):
                print("> A {}".format(step.name))
                duration += step.time_est
                equipment = equipment.union(step.things)
                cost += step.price or 0
            elif isinstance(step, Ride):
                print("> R {:.2f} h".format(step.duration))
                duration += step.duration
        print("Duration : {:5.2f} h".format(duration))
        print("Cost     : {:5.2f} €".format(cost))
        print("Equipment:")
        for eq in equipment:
            print("> {}".format(eq.value))
        print("")
