from lib import Attraction, Importance, Equipment, Dataset, Region
from lib import get_attraction_by_name

_base = Attraction("Casa", 0, [], Importance.NONE, 0)

_dataset = Dataset(
    attractions=[
        Attraction("Casa", 0, [], Importance.NONE, 0),
        Attraction("Spiaggia", 4, [Equipment.SWIMMING], Importance.HIGH, 0),
        Attraction("Catania", 5, [Equipment.CAMERA], Importance.MHI, 24.8),
        Attraction("Etna", 1, [Equipment.CAMERA, Equipment.TREKKING_SHOES], Importance.HIGH),
        Attraction("Pineta dei Monti Rossi", 1, [Equipment.CAMERA, Equipment.TREKKING_SHOES], Importance.MID),
        Attraction("Taormina", 3, [Equipment.CAMERA], Importance.HIGH),
        Attraction("Giardini Naxos - Archeo", 3, [Equipment.CAMERA], Importance.MID),
        Attraction("Gole del Alcantara", 3, [Equipment.CAMERA, Equipment.WATER_SHOES], Importance.HIGH, 24),
        Attraction("Messina", 3, [Equipment.CAMERA], Importance.MLO),
        # Attraction(
        #     "Reggio Calabro", 5, [Equipment.CAMERA], Importance.LOW
        # ),
        Attraction("Tindari", 1, [Equipment.CAMERA], Importance.MLO),
        Attraction("Siracusa - Ortigia", 7, [Equipment.CAMERA], Importance.HIGH),
        Attraction("Caltagirone", 2, [Equipment.CAMERA], Importance.MLO),
        Attraction("Enna", 2, [Equipment.CAMERA], Importance.MLO),
        Attraction("Piazza Armerina - Villa Romana del Casale", 3, [Equipment.CAMERA], Importance.MID, 10),
        Attraction("Noto", 2, [Equipment.CAMERA], Importance.LOW),
        Attraction("Cava Grande", 5,
                   [Equipment.CAMERA, Equipment.TREKKING_SHOES, Equipment.WATER_SHOES, Equipment.SWIMMING],
                   Importance.MLO),
        Attraction("Vendicari", 4, [Equipment.CAMERA], Importance.MHI),
        Attraction("Modica", 2, [Equipment.CAMERA], Importance.LOW),
        Attraction("Palermo", 4, [Equipment.CAMERA], Importance.HIGH),
        Attraction("Monte Pellegrino", 2, [Equipment.CAMERA, Equipment.TREKKING_SHOES], Importance.MID),
        Attraction("Corleone", 2, [Equipment.CAMERA], Importance.MLO),
        Attraction("Cefalù", 2, [Equipment.CAMERA], Importance.MID),
        Attraction("Erice", 4, [Equipment.CAMERA], Importance.MID, 9),
        Attraction("Scopello", 6, [Equipment.CAMERA], Importance.MHI, 5),
        Attraction("Segesta", 4, [Equipment.CAMERA, Equipment.SWIMMING], Importance.MID),
        Attraction("Selinunte", 2, [Equipment.CAMERA], Importance.MID, 6),
        Attraction("Valle dei Templi", 4, [Equipment.CAMERA, Equipment.TREKKING_SHOES], Importance.MID, 10)
    ],
    distances={
        # Base Cluster NE
        ("Casa", "Spiaggia"): 0.001,
        ("Casa", "Taormina"): 0.5,
        ("Casa", "Catania"): 1.5,
        ("Casa", "Pineta dei Monti Rossi"): 1,
        # ("Casa", "Etna"): 1.25,
        ("Pineta dei Monti Rossi", "Etna"): 0.4,
        ("Etna", "Gole del Alcantara"): 1.25,
        ("Gole del Alcantara", "Casa"): 0.6,
        ("Casa", "Giardini Naxos - Archeo"): 0.4,
        ("Taormina", "Giardini Naxos - Archeo"): 0.25,
        ("Casa", "Messina"): 0.5,
        # ("Messina", "Reggio Calabro"): 2,
        ("Messina", "Tindari"): 1,
        ("Casa", "Tindari"): 1.25,
        ("Giardini Naxos - Archeo", "Catania"): 0.7,
        ("Taormina", "Messina"): 0.65,
        ("Catania", "Pineta dei Monti Rossi"): 0.6,
        ("Gole del Alcantara", "Tindari"): 1.5,
        # Base Cluster NW
        ("Palermo", "Monte Pellegrino"): 0.5,
        ("Palermo", "Corleone"): 1.2,
        ("Palermo", "Cefalù"): 1,
        ("Cefalù", "Monte Pellegrino"): 1.25,
        ("Cefalù", "Corleone"): 1.5,
        ("Corleone", "Monte Pellegrino"): 1.4,
        # Base Cluster SW
        ("Erice", "Scopello"): 0.75,
        ("Erice", "Segesta"): 0.6,
        ("Erice", "Selinunte"): 1.1,
        ("Erice", "Valle dei Templi"): 2.2,
        ("Scopello", "Segesta"): 0.7,
        ("Scopello", "Selinunte"): 1,
        ("Scopello", "Valle dei Templi"): 2,
        ("Segesta", "Selinunte"): 0.8,
        ("Segesta", "Valle dei Templi"): 1.9,
        ("Selinunte", "Valle dei Templi"): 1.4,
        # Base Cluster SE
        ("Siracusa - Ortigia", "Caltagirone"): 1.3,
        ("Siracusa - Ortigia", "Enna"): 1.7,
        ("Siracusa - Ortigia", "Piazza Armerina - Villa Romana del Casale"): 1.7,
        ("Siracusa - Ortigia", "Noto"): 0.5,
        ("Siracusa - Ortigia", "Cava Grande"): 0.6,  # Ingresso nord
        ("Siracusa - Ortigia", "Vendicari"): 0.75,
        ("Siracusa - Ortigia", "Modica"): 1,
        ("Caltagirone", "Enna"): 1,
        ("Caltagirone", "Piazza Armerina - Villa Romana del Casale"): 0.6,
        ("Caltagirone", "Noto"): 1.5,
        ("Caltagirone", "Cava Grande"): 1.4,  # Ingresso nord
        ("Caltagirone", "Vendicari"): 1.9,
        ("Caltagirone", "Modica"): 1.1,
        ("Enna", "Piazza Armerina - Villa Romana del Casale"): 0.7,
        ("Enna", "Noto"): 1.75,
        ("Enna", "Cava Grande"): 1.9,  # Ingresso nord
        ("Enna", "Vendicari"): 1.9,
        ("Enna", "Modica"): 2,
        ("Piazza Armerina - Villa Romana del Casale", "Noto"): 1.9,
        ("Piazza Armerina - Villa Romana del Casale", "Cava Grande"): 1.8,  # Ingresso nord
        ("Piazza Armerina - Villa Romana del Casale", "Vendicari"): 2.1,
        ("Piazza Armerina - Villa Romana del Casale", "Modica"): 1.5,
        ("Noto", "Cava Grande"): 0.5,  # Ingresso nord
        ("Noto", "Vendicari"): 0.4,
        ("Noto", "Modica"): 0.7,
        ("Cava Grande", "Vendicari"): 0.8,
        ("Cava Grande", "Modica"): 1.1,
        ("Vendicari", "Modica"): 1,
        # Additional distances
        ("Cefalù", "Messina"): 1.9,
        ("Scopello", "Palermo"): 1.6,
        ("Segesta", "Palermo"): 1.2,
        ("Valle dei Templi", "Enna"): 1,
        ("Catania", "Siracusa - Ortigia"): 0.8,
        ("Casa", "Siracusa - Ortigia"): 1.5,
        ("Casa", "Caltagirone"): 1.7,
        ("Casa", "Enna"): 1.9,
        ("Casa", "Piazza Armerina - Villa Romana del Casale"): 1.9,
        ("Casa", "Noto"): 1.75,
        ("Casa", "Cava Grande"): 1.8,
        ("Casa", "Vendicari"): 1.9,
        ("Casa", "Modica"): 2.2,
        ("Casa", "Palermo"): 3,
        ("Casa", "Monte Pellegrino"): 3.5,
        ("Casa", "Corleone"): 3.5,
        ("Casa", "Cefalù"): 2.2,
        ("Casa", "Erice"): 4,
        ("Casa", "Scopello"): 3.75,
        ("Casa", "Segesta"): 3.8,
        ("Casa", "Selinunte"): 3.9,
        ("Casa", "Valle dei Templi"): 2.5
    },
    base=_base,
)

# Selected by hand for now
content = Region(
    dataset=_dataset,
    clusters=[
        {
            get_attraction_by_name("Messina", _dataset.attractions),
            get_attraction_by_name("Tindari", _dataset.attractions)
        }, {
            get_attraction_by_name("Spiaggia", _dataset.attractions)
        }, {
            get_attraction_by_name("Taormina", _dataset.attractions),
            get_attraction_by_name("Giardini Naxos - Archeo", _dataset.attractions)
        }, {
            get_attraction_by_name("Catania", _dataset.attractions)
        }, {
            get_attraction_by_name("Gole del Alcantara", _dataset.attractions),
            get_attraction_by_name("Etna", _dataset.attractions),
            get_attraction_by_name("Pineta dei Monti Rossi", _dataset.attractions)
        }, {
            get_attraction_by_name("Palermo", _dataset.attractions),
            get_attraction_by_name("Cefalù", _dataset.attractions)
        }, {
            get_attraction_by_name("Siracusa - Ortigia", _dataset.attractions)
        }, {
            get_attraction_by_name("Enna", _dataset.attractions),
            get_attraction_by_name("Caltagirone", _dataset.attractions),
            get_attraction_by_name("Piazza Armerina - Villa Romana del Casale", _dataset.attractions)
        }, {
            get_attraction_by_name("Vendicari", _dataset.attractions),
            get_attraction_by_name("Cava Grande", _dataset.attractions)
        }
    ]
)
