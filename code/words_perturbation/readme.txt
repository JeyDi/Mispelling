leggi file txt con il tuo testo (oppure leggi direttamente una stringa)
trasforma in una stringa

conta quante frasi ci sono nel file

calcola il tot percento del numero di frasi in input arrotondato per difetto
n frasi : 100 = x frasi : percentuale
quindi x frasi = difetto(nfrase * percentuale / 100)

cicla sul numero di frasi per arrivare a quella percentuale
    calcola indice max di numero di frasi (ce l'ho già)
    genera randomicamente un numero da 1 a max(numero frasi)
    estrai la parola con indice = numero random
    perturba parola aggiungendo caratteri a caso (?)
    salva la parola in un vettore (oppure in un dizionario dove la chiave è la posizione? o in un data frame?)
    ricalcola il massimo e aggiorna l'indice max del random

alla fine del ciclo ripopola le frasi nel posto corretto nella stringa

Rigenera il file con la perturbazione
    