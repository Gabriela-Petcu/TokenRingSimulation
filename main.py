from token_ring import TokenRing

if __name__ == "__main__":
    directie = input("Alege sensul de circulatie a jetonului (inainte / inapoi): ").strip().lower()
    
    while directie not in ["inainte", "inapoi"]:
        directie = input("Te rog sa alegi doar 'inainte' sau 'inapoi': ").strip().lower()

    #instanta retelei TonkenRing
    token_ring = TokenRing(directie)

    #simularea
    token_ring.simuleaza()
