class Token:
    """
    repr jetonul folosit in reteaua Token Ring.
    jetonul transporta un mesaj de la o sursa la o destinatie specificata
    """
    def __init__(self):
        """
        initializare jeton cu param impliciti
        """
        self.ip_sursa = None
        self.ip_destinatie = None
        self.mesaj = None
        self.ajuns_la_destinatie = False
        self.liber = True
        self.istoric = []

    def reset(self):
        """
        reseteaza jetonul la starea initiala dupa ce mesajul a fost livrat si a revenit la sursa
        """
        self.ip_sursa = None
        self.ip_destinatie = None
        self.mesaj = None
        self.ajuns_la_destinatie = False
        self.liber = True
        self.istoric = []
