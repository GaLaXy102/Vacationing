from lib import Attraction, Importance, Equipment, Dataset, Region
from lib import get_attraction_by_name
_base = Attraction("Marti", 0, set(), Importance.HIGH, coordinates=(43.6319, 10.74781))

_dataset = Dataset(
    base=_base,
    attractions=frozenset({
        _base,
        Attraction("Museo Piaggio", duration=1.25, importance=Importance.HIGH, equipment=set(), price=0.00),
        Attraction("Terme di Saturnia", duration=2.00, importance=Importance.MID, equipment=set(), price=0.00),
        Attraction("Marina di Bibbona", duration=4.00, importance=Importance.MID, equipment=set(), price=None),
        Attraction("Firenze, Santa Maria Novella", duration=8.50, importance=Importance.HIGH, equipment=set(), price=57.20),
        Attraction("Fiesole", duration=4.00, importance=Importance.MHI, equipment=set(), price=12.00),
        Attraction("Montelupo Fiorentino", duration=3.00, importance=Importance.LOW, equipment=set(), price=0.00),
        Attraction("Certaldo", duration=2.00, importance=Importance.LOW, equipment=set(), price=0.00),
        # Attraction("MP53/5", duration=2.00, importance=Importance.MID, equipment=set(), price=0.00),
        # Attraction("Tenuta il Palagio", duration=0.50, importance=Importance.LOW, equipment=set(), price=0.00),
        Attraction("Reggello", duration=2.50, importance=Importance.MID, equipment=set(), price=0.00),
        Attraction("Prato", duration=4.00, importance=Importance.HIGH, equipment=set(), price=0.00),
        Attraction("Lago di Bilancino", duration=2.00, importance=Importance.MHI, equipment=set(), price=0.00),
        Attraction("Scarperia", duration=1.50, importance=Importance.MID, equipment=set(), price=0.00),
        Attraction("Pistoia", duration=4.00, importance=Importance.HIGH, equipment=set(), price=0.00),
        Attraction("Museo Ideale Leonardo da Vinci", duration=1.50, importance=Importance.MLO, equipment=set(), price=12.00),
        Attraction("Montecatini Terme", duration=3.00, importance=Importance.LOW, equipment=set(), price=14.00),
        Attraction("Pescia", duration=2.00, importance=Importance.LOW, equipment=set(), price=0.00),
        Attraction("Montagna Pistoiese", duration=6.00, importance=Importance.MLO, equipment=set(), price=0.00),
        Attraction("Siena, Piazza del Campo", duration=4.00, importance=Importance.HIGH, equipment=set(), price=0.00),
        Attraction("Arezzo", duration=3.00, importance=Importance.MID, equipment=set(), price=8.00),
        Attraction("Poppi", duration=1.50, importance=Importance.LOW, equipment=set(), price=0.00),
        Attraction("Casentino", duration=4.00, importance=Importance.MLO, equipment=set(), price=0.00),
        Attraction("Cortona", duration=2.00, importance=Importance.MLO, equipment=set(), price=0.00),
        Attraction("Greve in Chianti", duration=2.00, importance=Importance.MID, equipment=set(), price=0.00),
        Attraction("Monteriggioni", duration=1.50, importance=Importance.HIGH, equipment=set(), price=8.00),
        Attraction("San Gimignano", duration=4.00, importance=Importance.HIGH, equipment=set(), price=10.00),
        Attraction("Montalcino", duration=3.00, importance=Importance.LOW, equipment=set(), price=0.00),
        Attraction("Val D'Orcia", duration=2.00, importance=Importance.MID, equipment=set(), price=0.00),
        Attraction("Montepulciano", duration=2.00, importance=Importance.MLO, equipment=set(), price=0.00),
        Attraction("Massa Marittima", duration=2.00, importance=Importance.MID, equipment=set(), price=0.00),
        Attraction("Monte Argentario", duration=1.50, importance=Importance.MID, equipment=set(), price=0.00),
        Attraction("Pitigliano", duration=1.50, importance=Importance.MLO, equipment=set(), price=0.00),
        Attraction("Livorno, Acquario", duration=6.00, importance=Importance.MID, equipment=set(), price=28.00),
        Attraction("Bolgheri", duration=1.00, importance=Importance.MID, equipment=set(), price=0.00),
        Attraction("Parco Archeologico di Baratti e Populonia", duration=5.00, importance=Importance.MID, equipment=set(), price=50.00),
        Attraction("Lucca", duration=4.00, importance=Importance.MHI, equipment=set(), price=0.00),
        Attraction("Lago Massaciuccoli", duration=1.00, importance=Importance.MID, equipment=set(), price=0.00),
        Attraction("Pisa, Ponte di Mezzo", duration=4.00, importance=Importance.HIGH, equipment=set(), price=66.80),
        Attraction("Massa", duration=3.00, importance=Importance.LOW, equipment=set(), price=0.00),
        Attraction("Crete Senesi", duration=1.00, importance=Importance.MID, equipment=set(), price=0.00),
    }),
    distances={}
)

content = Region(
    dataset=_dataset,
    clusters=set()
)
