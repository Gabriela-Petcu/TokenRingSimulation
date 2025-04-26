class Computer:
    """
    reprezinta un calculator din reteaua token ring
    
    atribute:
    -name(str): numele calc
    -ip(str): adresa ip a calc
    -buffer(str): mesaj primit si stocat temporar in buffer
    """
    def __init__(self, name, ip):
        """
        initializeaza un calc cu un nume si o adresa IP.
        
        param:
        -name(str): numele calc
        -ip(str): adresa IP a calc
        """
        self.name = name
        self.ip = ip
        self.buffer = None

    def __str__(self):
        """
        return reprezentarea sub forma de string a calc, afisand nume,IP-ul si mesajul din buffer.
        """
        msg = self.buffer if self.buffer else "null"
        return f"{self.name}({self.ip}) -> {msg}"
