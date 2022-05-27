from lib import Region, Attraction, Importance, Dataset
from lib import get_attraction_by_name

_base = Attraction("Appartement", 0, set(), Importance.NONE, 0)

_dataset = Dataset(
    attractions=frozenset({
        _base,
        # Île de la Cité -> Marais
        Attraction("Fontaine Stravinsky", 0.25, set(), Importance.MHI),
        Attraction("Pont Neuf", 0.25, set(), Importance.MHI),
        Attraction("Musée du Louvre", 8, set(), Importance.HIGH, 0),  # M x M D F S S
        Attraction("Carrousel du Louvre", 1.5, set(), Importance.MID),
        Attraction("Jardin des Tuileries", 1, set(), Importance.MID),
        Attraction("Palais Royal et Jardin", 2, set(), Importance.MID),
        Attraction("Place Vendôme", 0.25, set(), Importance.MID),
        Attraction("Galerie Vivienne", 2, set(), Importance.MHI),
        Attraction("Place du Marché Ste. Cathérine", 1, set(), Importance.MHI),
        Attraction("Place des Vosges", 1, set(), Importance.MHI),
        Attraction("Notre-Dame", 0.5, set(), Importance.HIGH),
        # Quartier Latin -> Tour Eiffel
        Attraction("Panthéon", 1.5, set(), Importance.MHI),
        Attraction("Rue Mouffetard", 0.5, set(), Importance.MHI),
        Attraction("Musée de la Sculpture en plein air", 0.5, set(), Importance.MHI),
        Attraction("Jardin du Luxembourg", 1.5, set(), Importance.MHI),
        Attraction("Tour Eiffel - Trocadero", 1, set(), Importance.HIGH),
        Attraction("Musée d'Orsay", 4, set(), Importance.MHI),  # x D M D F S S
        # Champs-Élysées -> Opéra
        Attraction("Arc de Triomphe - Champs-Élysées", 1.5, set(), Importance.HIGH, 0),  # M D M D F S S
        Attraction("Pont Alexandre III.", 0.25, set(), Importance.MHI),
        Attraction("Place de la Concorde", 0.25, set(), Importance.MID),
        # Canal St-Martin -> Bois de Vincennes
        Attraction("Canal St-Martin", 4, set(), Importance.MHI),
        Attraction("Coulée verte René-Dumont", 2, set(), Importance.MHI),
        # Montparnasse -> Bois de Boulogne
        Attraction("Tour Montparnasse", 1.5, set(), Importance.HIGH, 28),  # M D M D F S S
        Attraction("Ile aux Cygnes", 2, set(), Importance.MHI),
        Attraction("Le Corbusier", 2, set(), Importance.MID),
        Attraction("Bois de Boulogne", 5, set(), Importance.MHI),
        # Montmartre -> Belleville
        Attraction("Sacre-Coeur", 1.5, set(), Importance.HIGH),
        Attraction("Cité des Sciences", 6, set(), Importance.HIGH, 18),  # x D M D F S S
        Attraction("Parc des Buttes-Chaumont", 2, set(), Importance.MID),
        # Versailles
        Attraction("Versailles", 8, set(), Importance.MID, 0),  # x D M D F S S
    }),
    distances={
        # Île de la Cité -> Marais
        ("Fontaine Stravinsky", "Pont Neuf"): 0.15,
        ("Fontaine Stravinsky", "Musée du Louvre"): 0.1,
        ("Fontaine Stravinsky", "Jardin des Tuileries"): 0.2,
        ("Fontaine Stravinsky", "Palais Royal et Jardin"): 0.2,
        ("Fontaine Stravinsky", "Place Vendôme"): 0.3,
        ("Fontaine Stravinsky", "Galerie Vivienne"): 0.25,
        ("Fontaine Stravinsky", "Place du Marché Ste. Cathérine"): 0.2,
        ("Fontaine Stravinsky", "Place des Vosges"): 0.15,
        ("Fontaine Stravinsky", "Notre-Dame"): 0.2,
        ("Pont Neuf", "Musée du Louvre"): 0.1,
        ("Pont Neuf", "Jardin des Tuileries"): 0.2,
        ("Pont Neuf", "Palais Royal et Jardin"): 0.15,
        ("Pont Neuf", "Place Vendôme"): 0.25,
        ("Pont Neuf", "Galerie Vivienne"): 0.25,
        ("Pont Neuf", "Place du Marché Ste. Cathérine"): 0.25,
        ("Pont Neuf", "Place des Vosges"): 0.25,
        ("Pont Neuf", "Notre-Dame"): 0.2,
        ("Musée du Louvre", "Carrousel du Louvre"): 0.05,
        ("Musée du Louvre", "Jardin des Tuileries"): 0.1,
        ("Musée du Louvre", "Palais Royal et Jardin"): 0.1,
        ("Musée du Louvre", "Place Vendôme"): 0.15,
        ("Musée du Louvre", "Galerie Vivienne"): 0.15,
        ("Musée du Louvre", "Place du Marché Ste. Cathérine"): 0.2,
        ("Musée du Louvre", "Place des Vosges"): 0.25,
        ("Musée du Louvre", "Notre-Dame"): 0.25,
        # Carrousel omitted due to exact overlap with Louvre
        ("Jardin des Tuileries", "Palais Royal et Jardin"): 0.2,
        ("Jardin des Tuileries", "Place Vendôme"): 0.1,
        ("Jardin des Tuileries", "Galerie Vivienne"): 0.25,
        ("Jardin des Tuileries", "Place du Marché Ste. Cathérine"): 0.25,
        ("Jardin des Tuileries", "Place des Vosges"): 0.3,
        ("Jardin des Tuileries", "Notre-Dame"): 0.3,
        ("Palais Royal et Jardin", "Place Vendôme"): 0.15,
        ("Palais Royal et Jardin", "Galerie Vivienne"): 0.1,
        ("Palais Royal et Jardin", "Place du Marché Ste. Cathérine"): 0.25,
        ("Palais Royal et Jardin", "Place des Vosges"): 0.3,
        ("Palais Royal et Jardin", "Notre-Dame"): 0.3,
        ("Place Vendôme", "Galerie Vivienne"): 0.2,
        ("Place Vendôme", "Place du Marché Ste. Cathérine"): 0.35,
        ("Place Vendôme", "Place des Vosges"): 0.4,
        ("Place Vendôme", "Notre-Dame"): 0.4,
        ("Galerie Vivienne", "Place du Marché Ste. Cathérine"): 0.3,
        ("Galerie Vivienne", "Place des Vosges"): 0.35,
        ("Galerie Vivienne", "Notre-Dame"): 0.35,
        ("Place du Marché Ste. Cathérine", "Place des Vosges"): 0.1,
        ("Place du Marché Ste. Cathérine", "Notre-Dame"): 0.25,
        ("Place des Vosges", "Notre-Dame"): 0.25,
        # Quartier Latin -> Tour Eiffel
        ("Panthéon", "Rue Mouffetard"): 0.1,
        ("Panthéon", "Musée de la Sculpture en plein air"): 0.2,
        ("Panthéon", "Jardin du Luxembourg"): 0.1,
        ("Panthéon", "Tour Eiffel - Trocadero"): 0.6,
        ("Panthéon", "Musée d'Orsay"): 0.4,
        ("Rue Mouffetard", "Musée de la Sculpture en plein air"): 0.25,
        ("Rue Mouffetard", "Jardin du Luxembourg"): 0.2,
        ("Rue Mouffetard", "Tour Eiffel - Trocadero"): 0.75,
        ("Rue Mouffetard", "Musée d'Orsay"): 0.5,
        ("Musée de la Sculpture en plein air", "Jardin du Luxembourg"): 0.25,
        ("Musée de la Sculpture en plein air", "Tour Eiffel - Trocadero"): 0.7,
        ("Musée de la Sculpture en plein air", "Musée d'Orsay"): 0.4,
        ("Jardin du Luxembourg", "Tour Eiffel - Trocadero"): 0.45,
        ("Jardin du Luxembourg", "Musée d'Orsay"): 0.25,
        ("Tour Eiffel - Trocadero", "Musée d'Orsay"): 0.3,
        # Champs-Élysées -> Opéra
        ("Arc de Triomphe - Champs-Élysées", "Pont Alexandre III."): 0.15,
        ("Arc de Triomphe - Champs-Élysées", "Place de la Concorde"): 0.05,
        ("Pont Alexandre III.", "Place de la Concorde"): 0.15,
        # Canal St-Martin -> Bois de Vincennes
        ("Canal St-Martin", "Coulée verte René-Dumont"): 0.3,
        # Montparnasse -> Bois de Boulogne
        ("Tour Montparnasse", "Ile aux Cygnes"): 0.4,
        ("Tour Montparnasse", "Le Corbusier"): 0.55,
        ("Tour Montparnasse", "Bois de Boulogne"): 0.55,
        ("Ile aux Cygnes", "Le Corbusier"): 0.3,
        ("Ile aux Cygnes", "Bois de Boulogne"): 0.55,
        ("Le Corbusier", "Bois de Boulogne"): 0.2,
        # Montmartre -> Belleville
        ("Sacre-Coeur", "Cité des Sciences"): 0.55,
        ("Sacre-Coeur", "Parc des Buttes-Chaumont"): 0.4,
        ("Cité des Sciences", "Parc des Buttes-Chaumont"): 0.35,
        # Appartement
        ("Appartement", "Fontaine Stravinsky"): 0.45,
        ("Appartement", "Pont Neuf"): 0.4,
        ("Appartement", "Musée du Louvre"): 0.45,
        ("Appartement", "Carrousel du Louvre"): 0.45,
        ("Appartement", "Jardin des Tuileries"): 0.6,
        ("Appartement", "Palais Royal et Jardin"): 0.5,
        ("Appartement", "Place Vendôme"): 0.55,
        ("Appartement", "Galerie Vivienne"): 0.35,
        ("Appartement", "Place du Marché Ste. Cathérine"): 0.45,
        ("Appartement", "Place des Vosges"): 0.45,
        ("Appartement", "Notre-Dame"): 0.5,
        ("Appartement", "Panthéon"): 0.35,
        ("Appartement", "Rue Mouffetard"): 0.35,
        ("Appartement", "Musée de la Sculpture en plein air"): 0.45,
        ("Appartement", "Jardin du Luxembourg"): 0.55,
        ("Appartement", "Tour Eiffel - Trocadero"): 0.7,
        ("Appartement", "Musée d'Orsay"): 0.65,
        ("Appartement", "Arc de Triomphe - Champs-Élysées"): 0.65,
        ("Appartement", "Pont Alexandre III."): 0.7,
        ("Appartement", "Place de la Concorde"): 0.6,
        ("Appartement", "Canal St-Martin"): 0.6,
        ("Appartement", "Coulée verte René-Dumont"): 0.55,
        ("Appartement", "Tour Montparnasse"): 0.5,
        ("Appartement", "Ile aux Cygnes"): 0.8,
        ("Appartement", "Le Corbusier"): 0.85,
        ("Appartement", "Bois de Boulogne"): 0.8,
        ("Appartement", "Sacre-Coeur"): 0.85,
        ("Appartement", "Cité des Sciences"): 0.75,
        ("Appartement", "Parc des Buttes-Chaumont"): 0.7,
        ("Appartement", "Versailles"): 1.25,
        # Random
        ("Versailles", "Tour Montparnasse"): 0.45,
        ("Versailles", "Tour Eiffel - Trocadero"): 0.55,
        ("Versailles", "Bois de Boulogne"): 0.9,
        ("Notre-Dame", "Panthéon"): 0.2,
        ("Tour Eiffel - Trocadero", "Tour Montparnasse"): 0.35,
        ("Tour Eiffel - Trocadero", "Pont Alexandre III."): 0.2,
        ("Tour Eiffel - Trocadero", "Arc de Triomphe - Champs-Élysées"): 0.35,
        ("Parc des Buttes-Chaumont", "Place des Vosges"): 0.45,
        ("Sacre-Coeur", "Place de la Concorde"): 0.35,
        ("Musée de la Sculpture en plein air", "Coulée verte René-Dumont"): 0.25,
        ("Canal St-Martin", "Parc des Buttes-Chaumont"): 0.2,
        ("Le Corbusier", "Tour Eiffel - Trocadero"): 0.35,
    },
    base=_base
)

content = Region(
    dataset=_dataset,
    clusters={
        frozenset({
            get_attraction_by_name("Fontaine Stravinsky", _dataset.attractions),
            get_attraction_by_name("Pont Neuf", _dataset.attractions),
            get_attraction_by_name("Musée du Louvre", _dataset.attractions),
            get_attraction_by_name("Carrousel du Louvre", _dataset.attractions),
            get_attraction_by_name("Jardin des Tuileries", _dataset.attractions),
            get_attraction_by_name("Palais Royal et Jardin", _dataset.attractions),
            get_attraction_by_name("Place Vendôme", _dataset.attractions),
            get_attraction_by_name("Galerie Vivienne", _dataset.attractions),
            get_attraction_by_name("Place du Marché Ste. Cathérine", _dataset.attractions),
            get_attraction_by_name("Place des Vosges", _dataset.attractions),
            get_attraction_by_name("Notre-Dame", _dataset.attractions),
            get_attraction_by_name("Panthéon", _dataset.attractions),
            get_attraction_by_name("Rue Mouffetard", _dataset.attractions),
            get_attraction_by_name("Musée de la Sculpture en plein air", _dataset.attractions),
            get_attraction_by_name("Jardin du Luxembourg", _dataset.attractions),
            get_attraction_by_name("Tour Eiffel - Trocadero", _dataset.attractions),
            get_attraction_by_name("Musée d'Orsay", _dataset.attractions),
            get_attraction_by_name("Arc de Triomphe - Champs-Élysées", _dataset.attractions),
            get_attraction_by_name("Pont Alexandre III.", _dataset.attractions),
            get_attraction_by_name("Place de la Concorde", _dataset.attractions),
            get_attraction_by_name("Canal St-Martin", _dataset.attractions),
            get_attraction_by_name("Coulée verte René-Dumont", _dataset.attractions),
            get_attraction_by_name("Tour Montparnasse", _dataset.attractions),
            get_attraction_by_name("Ile aux Cygnes", _dataset.attractions),
            get_attraction_by_name("Le Corbusier", _dataset.attractions),
            get_attraction_by_name("Bois de Boulogne", _dataset.attractions),
            get_attraction_by_name("Sacre-Coeur", _dataset.attractions),
            get_attraction_by_name("Cité des Sciences", _dataset.attractions),
            get_attraction_by_name("Parc des Buttes-Chaumont", _dataset.attractions),
            get_attraction_by_name("Versailles", _dataset.attractions),
        }),
    }
)
