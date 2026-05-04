#modulo per il salvataggio su file dei risultati
def salva_risultati(righe, ora_avvio): #ricevo le righe già pronte e l'ora d'avvio per costruire il nome file univoco
    nome_file = f"vendite_{ora_avvio.strftime('%Y%m%d_%H%M%S')}.txt" #includo il timestamp nel nome per evitare sovrascritture tra esecuzioni diverse
    with open(nome_file, "w", encoding="utf-8") as f: #uso il with per garantire la chiusura del file anche in caso di eccezione
        f.write("\n".join(righe)) #join() concatena tutti gli elementi della lista in un'uunica stringa separata da newline
    print(f"Risultati salvati in '{nome_file}'.")
