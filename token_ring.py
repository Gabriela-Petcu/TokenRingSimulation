import random
from computer import Computer
from my_token import Token

class TokenRing:
    """
    clasa TokenRing simuleaza o retea Token Ring
    unde mesajele sunt transmise folosind un jeton intre calc
    """

    def __init__(self, directie="inainte", debug_mode=True):
        """
        initializeaza reteaua Token Ring cu directia specificata
        
        param:
        -directie(str): sensul de circulatie al jetonului
        -debug_mode:daca este true, afiseaza info suplimentare pt debug
        """
        self.computers = self._genereaza_calculatoare()
        self.token = Token()
        self.index_start = 0  # pleaca de aici jetonul la fiecare simulare
        self.directie = directie
        self.debug_mode = debug_mode

    def _genereaza_ip(self):
        """
        genereaza un IP aleator format din 4 octeti
        """
        return ".".join(str(random.randint(0, 255)) for _ in range(4))

    def _genereaza_calculatoare(self):
        """
        genereaza 10 calc cu IP-uri unice si nume de la C0 la C9
        
        return: lista cu 10 obiecte Computer
        """
        computere = []
        ipuri_folosite = set()
        for i in range(10):
            ip = self._genereaza_ip()
            while ip in ipuri_folosite:
                ip = self._genereaza_ip()
            ipuri_folosite.add(ip)
            computere.append(Computer(f"C{i}", ip))
        return computere

    def _afiseaza_stare_retea(self):
        """
        afiseaza starea actuala a fiecarui calc din retea
        """
        for c in self.computers:
            print(str(c))

    def _alege_sursa_si_destinatie(self):
        """
        alege aleator un calc sursa si unul destinatie diferite
        
        return: tuple(sursa, destinatie)
        """
        sursa = random.choice(self.computers)
        destinatie = random.choice(self.computers)
        while destinatie == sursa:
            destinatie = random.choice(self.computers)
        return sursa, destinatie

    def simuleaza(self, nr_simulari=10):
        """
        simuleaza transmiterea mesajelor in reteaua Token Ring
        
        param:
        -nr_simulari: nr de simulari de transmisie a mesajelor
        """
        for simulare in range(nr_simulari):
            print(f"\n--- Simulare {simulare + 1} ---")

            sursa, destinatie = self._alege_sursa_si_destinatie()
            mesaj = f"Mesaj de test {simulare + 1}"
            print(f"Sursa: {sursa.name} Destinatia: {destinatie.name}")
            print(f"Directia jetonului: {self.directie.upper()}")

            if self.debug_mode:
                print(f"[DEBUG] IP sursa: {sursa.ip}, IP destinatie: {destinatie.ip}")

            token = self.token
            token.liber = True
            token.istoric.clear()

            index = self.index_start
            inceput = True
            jeton_incarcat = False
            n = len(self.computers)

            while True:
                computer = self.computers[index]
                token.istoric.append(computer.name)

                #calc sursa preia jetonul liber si incarca mesajul
                if token.liber and computer == sursa and not jeton_incarcat:
                    print(f"{computer.name}: Preia jetonul")
                    token.ip_sursa = sursa.ip
                    token.ip_destinatie = destinatie.ip
                    token.mesaj = mesaj
                    token.liber = False
                    jeton_incarcat = True
                    if self.debug_mode:
                        print(f"[DEBUG] {computer.name} ({computer.ip}) incarca jetonul: Destinatie = {token.ip_destinatie}, Mesaj = '{token.mesaj}'")
                
                #jetonul a ajuns la destinatie
                elif not token.liber:
                    if computer.ip == token.ip_destinatie and not token.ajuns_la_destinatie:
                        print(f"{computer.name}: Am ajuns la destinatie")
                        computer.buffer = token.mesaj
                        token.ajuns_la_destinatie = True
                        if self.debug_mode:
                            print(f"[DEBUG] {computer.name} ({computer.ip}) a copiat mesajul in buffer: '{computer.buffer}'")
                    
                    #jetonul revine la sursa dupa ce mesajul a fost livrat
                    elif computer.ip == token.ip_sursa and token.ajuns_la_destinatie:
                        print(f"{computer.name}: Am ajuns inapoi")
                        if self.debug_mode:
                            print(f"[DEBUG] {computer.name} ({computer.ip}) reseteaza jetonul. Istoric: {token.istoric}")
                        token.reset()
                        self.index_start = index  # urm simulare pleaca de aici
                        break
                    else:
                        print(f"{computer.name}: Muta jetonul")
                        if self.debug_mode:
                            prev_index = (index - 1 + n) % n if self.directie == "inapoi" else (index - 1) % n
                            print(f"[DEBUG] Jetonul a fost transmis de la {self.computers[prev_index].name} la {computer.name}")
                
                #jetonul liber continua sa circule
                else:
                    print(f"{computer.name}: Muta jetonul")
                    if self.debug_mode:
                        prev_index = (index - 1 + n) % n if self.directie == "inapoi" else (index - 1) % n
                        print(f"[DEBUG] Jetonul a fost transmis de la {self.computers[prev_index].name} la {computer.name}")

                index = (index + 1) % n if self.directie == "inainte" else (index - 1 + n) % n
                
                #conditie de oprire pt a nu intra in bucla infinita
                if not inceput and index == self.index_start and token.liber:
                    break
                inceput = False

            if self.debug_mode:
                print(f"[DEBUG] Traseu complet jeton: {' -> '.join(token.istoric)}")

            #afis starea finala dupa fiecare simualare
            self._afiseaza_stare_retea()
