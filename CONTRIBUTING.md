# Linee Guida
Il seguente documento contiene i comportamenti da seguire per evitare traduzioni incoerenti e la procedura che consigliamo per contribuire al lavoro.

## Attenzione
Il file di traduzione è in formato .xml. Ciò significa che vanno rispettate le regole di chiusura dei tag, così come delle variabili.

In nessun caso vanno tradotti i termini all'interno delle parentesi graffe (es: {user}) in quanto causerebbero errori.

È sempre bene accertarsi che il file, a seguito di un grande refactor, vengano testati in un ambiente di prova prima di essere caricati.

### Forma

I **Verbi** vengono coniugati con la forma del tu. Ad esempio:

- "Please enter your name" diventa "Inserisci il tuo nome".

Il termine **Please** è variabile. Es:

* _In caso di divieto non si applica_. Es: "Please don't forget to enter your name" diventa "Non dimenticare di inserire il tuo nome"
* _In caso di invito si applica_. Es: "Please enter your name" diventa "Per favore, inserisci il tuo nome"

### Variabili di traduzione

In questa parte troverai la forma con cui traduciamo le stringhe più comuni. Se hai dubbi su una traduzione, fai riferimento a questo blocco.

- Threads = Discussioni
- Posts = Messaggi
- To Post = Pubblicare (verbo)
- Notices = Notifiche
- Themes = Temi
- Nodes = Nodi
- Attachments = Allegati
- Thumbnails = Anteprime
- Warn = Avvertimento
- Alert = Avviso
- Resource = Release
- API Key = Chiave API
- Parent = Genitore
- Child = Figlio
- Sibling = Fratello
- Guest = Ospiti
- Username = Nome Utente
- Ban = Bannato
- Notable = Degno di Nota
- Sticky = In Rilievo
- Board = Forum
- Rich = Avanzate
- Spam Cleaner = Pulizia Spam
- Hard-delete = Eliminazione permanente
- Soft-delete = Rimozione pubblica
- Flag = Segnalazioni (inteso come "only count flags recorded ...")
- Featured = In primo piano
- Prompt = Modulo
- Hard Bounce = Rimbalzo forte
- Soft Bounce = Rimbalzo morbido
- Report = Segnalazione
- Watch = Seguire
- Sidebar = Barra laterale

### Rimangono invece nella loro forma
- Templates
- Smilies
- BB code
- Asset
- Avatar
- Feed
- Log
- Upgrade (User)
- Directory
- Add-on
- Breadcrumbs
- Informazioni tecniche specifiche, volte allo sviluppo di addon, template e altro.
- Home
- Sitemap
- Account
- Scope 
- Staff
- Padding
- Form
- Break point
- Tooltip
- Secret

### In nessun caso modificare i valori tra parentesi graffe, ad esempio*
- {user}

## Come partecipare alla Traduzione
La traduzione può contenere diverse parti divise da Backend e Frontend, si prega di non partecipare alla traduzione se non si conoscono le caratteristiche di XenForo 2 (si consiglia di avere una demo preinstallata su cui effettuare i propri test). Le frasi del frontend hanno la priorità!

In definitiva per partecipare a questo progetto bisogna:
1. Creare un fork
2. Effettua le modifiche
3. Richiedi di integrare il tuo lavoro tramite pull request
