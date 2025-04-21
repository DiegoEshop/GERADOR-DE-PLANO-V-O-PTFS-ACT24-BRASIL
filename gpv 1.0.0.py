import random

aeroportos = ["IRFD", "IZOL", "IPPH", "ILAR", "ITKO"]

# SIDs com nome + sequência de fixos
procedimentos = {
    "IRFD": {
        "sids": {
            "PABE1B": ["LADNO", "ATPEV", "OCEEN"],
            "DAVU2B": ["LADNO", "ATPEV", "ANYMS"],
            "FAGU2A": ["JAMSI", "GRASS", "RENTS"]
        }
    },
    "ITKO": {
        "sids": {
            "HIBA1A": ["KNIFE", "ALLRY", "JOOPY"],
            "UREI1A": ["KNIFE", "ALLRY", "DINER"],
            "MIKA2B": ["KNIFE", "ONDER", "TUDEP"]
        }
    },
    "IZOL": {
        "sids": {
            "ABIR1A": ["ABSRS", "BILLO", "JUSTY"],
            "DORU1B": ["ABSRS", "CHAIN", "DEBUG"],
            "FURI3B": ["BILLO", "CHAIN", "NUBER"]
        }
    },
    "ILAR": {
        "sids": {
            "AQRT1A": ["AQWRT", "FORIA", "REAPR"],
            "GOGU2B": ["AQWRT", "FORIA", "LAZER"],
            "TRIO3C": ["AQWRT", "ODOKU", "PEPUL"]
        }
    },
    "IPPH": {
        "sids": {
            "AQRT1A": ["AQWRT", "FORIA", "REAPR"],
            "GOGU2B": ["AQWRT", "FORIA", "LAZER"],
            "TRIO3C": ["AQWRT", "ODOKU", "PEPUL"]
        }
    }
}

# STARs genéricas para qualquer aeroporto
stars_disponiveis = {
    "STAR1A": ["FROOT", "SUNSTA", "REAPR"],
    "STAR2B": ["CAMEL", "ODOKU", "CHAIN"],
    "STAR3C": ["SKOPELOS", "PIPER", "BILLO"]
}

fixos_adicionais = [
    "DOGGO", "CAMEL", "TRELN", "GOLDEN", "MORRD", "FRANK", "TOKY", "SKOPELOS", "FROOT", "GEORG", 
    "PIPER", "SUNSTA", "STACK", "DELIVERY", "COWO", "ODOKU", "SHELL", "DUNKS", "JAF", "GARRY"
]

def gerar_numero_voo():
    return f"PT{random.randint(1000, 9999)}"

def gerar_altitude_cruzeiro():
    return random.choice([4000, 5000, 6000, 7000, 8000, 9000, 10000])  # até FL100

def gerar_rota_completa(origem, destino, numero_voo, aeronave, qtd_intermediarios=3):
    if origem not in procedimentos or destino not in procedimentos:
        print("\033[91m⚠️ Aeroporto inválido! Use um dos seguintes:\033[0m", ", ".join(procedimentos.keys()))
        return

    sid_nome, sid_fixos = random.choice(list(procedimentos[origem]["sids"].items()))
    arr_nome, arr_fixos = random.choice(list(stars_disponiveis.items()))
    altitude = gerar_altitude_cruzeiro()

    usados = set(sid_fixos + arr_fixos + [origem, destino])
    intermediarios = random.sample(
        [f for f in fixos_adicionais if f not in usados],
        qtd_intermediarios
    )

    rota_completa = [origem] + sid_fixos + intermediarios + arr_fixos + [destino]

    print("\n📋 PLANO DE VOO:")
    print(f"FLTNBR: {numero_voo}")
    print(f"SID: {sid_nome}")
    print(f"ARR: {arr_nome}")
    print(f"AERONAVE: {aeronave}")
    print(f"CRZ: FL{altitude // 100} ({altitude} pés)")
    print(f"ROTA: {' '.join(rota_completa)}")

def listar_planos(icao):
    icao = icao.upper()
    if icao not in procedimentos:
        print("\033[91m⚠️ ICAO inválido! Use um dos seguintes:\033[0m", ", ".join(procedimentos.keys()))
        return

    print(f"\n📋 Procedimentos para {icao}:")
    sids = procedimentos[icao]["sids"]
    print("🛫 SIDs disponíveis:")
    for nome, fixos in sids.items():
        print(f"  - {nome}: {' → '.join(fixos)}")

    print("\n🛬 STARs disponíveis (genéricas):")
    for nome, fixos in stars_disponiveis.items():
        print(f"  - {nome}: {' → '.join(fixos)}")

def mostrar_comando_gg():
    print("\n🎮 Participe do nosso servidor do Discord!")
    print("Link de convite: https://discord.gg/EsRayCb6yh")

# Interface de comandos
if __name__ == "__main__":
    while True:
        cmd = input("\n💻 Digite um comando (/help para ajuda): ").strip().lower()

        if cmd.startswith("/listplns"):
            partes = cmd.split()
            if len(partes) != 2:
                print("\033[91mUso correto: /listplns [ICAO]\033[0m")
            else:
                listar_planos(partes[1])

        elif cmd == "/gg":
            mostrar_comando_gg()

        elif cmd == "/help":
            print("\n📘 Comandos disponíveis:")
            print("  /listplns [ICAO] → Mostra as SIDs e STARs disponíveis")
            print("  /gg → Mostra o link do servidor Discord")
            print("  /gen → Gera um plano de voo completo")
            print("  /exit → Sai do programa")

        elif cmd == "/gen":
            origem = input("🛫 Aeroporto de saída (ex: ITKO): ").strip().upper()
            destino = input("🛬 Aeroporto de chegada (ex: IZOL): ").strip().upper()

            voo_input = input("📋 Número do voo (ex: GOL1234) ou Enter para gerar: ").strip().upper()
            numero_voo = voo_input if voo_input else gerar_numero_voo()

            aeronave = input("✈️ Modelo da aeronave (ex: A320neo, B737): ").strip().upper()
            if not aeronave:
                aeronave = "DESCONHECIDA"

            gerar_rota_completa(origem, destino, numero_voo, aeronave)

        elif cmd == "/exit":
            print("👋 Saindo...")
            break

        else:
            print("\033[91m❌ Comando inválido. Use /help para ver os comandos disponíveis.\033[0m")
