import data
import lib

if __name__ == '__main__':
    importance = lib.Importance.LOW
    size = (20, 20)
    seed = 40
    lib.draw_graph(data.tuscany.dataset, importance, size, seed).show()
