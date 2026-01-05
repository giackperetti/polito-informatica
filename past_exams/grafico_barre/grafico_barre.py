import csv
from pprint import pprint


def leggi_dati(filepath):
    with open(filepath, "r") as file:
        return [
            {"label": riga["label"], "value": int(riga["value"])}
            for riga in csv.DictReader(file)
        ]


def leggi_config(filepath):
    defaults = {
        "max_bar_length": 50,
        "bar_char": "*",
        "show_values": True,
        "sort": None,
        "title": "",
    }

    config = {}
    with open(filepath, "r") as file:
        for riga in file:
            chiave, valore = riga.strip().split("=")
            chiave = chiave.strip()
            valore = valore.strip()

            if chiave == "max_bar_length":
                valore = int(valore)
            elif chiave == "show_values":
                valore = valore.lower() == "true"
            elif chiave == "sort":
                valore = valore if valore in ("asc", "desc") else None

            config[chiave] = valore

    return {**defaults, **config}


def disegna_grafico(dati, config):
    max_bar_length = config["max_bar_length"]
    bar_char = config["bar_char"]
    show_values = config["show_values"]
    sort = config["sort"]
    title = config["title"]
    
    if sort == "asc":
        dati = sorted(dati, key=lambda d: d["value"])
    elif sort == "desc":
        dati = sorted(dati, key=lambda d: d["value"], reverse=True)
    
    if title:
        print(title)
    
    dato_massimo = max(d["value"] for d in dati)
    
    for d in dati:
        bar_length = int((d["value"] * max_bar_length) / dato_massimo)
        bar = bar_char * bar_length
        
        if show_values:
            print(f"{d['label']:<20} | {bar} {d['value']}")
        else:
            print(f"{d['label']:<20} | {bar}")


def main() -> None:
    dati = leggi_dati("./data/dati.csv")
    config = leggi_config("./data/config1.txt")
    
    disegna_grafico(dati, config)


if __name__ == "__main__":
    main()
