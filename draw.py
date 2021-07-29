import data
import lib

if __name__ == '__main__':
    importance = lib.Importance.LOW
    size = (20, 10)
    seed = 40
    lib.draw_graph(data.sicily.dataset, importance, size, seed).show()
