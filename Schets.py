
## Wat hebben we nodig? / Classes
    # Bord
        #FUNCTIE Initialiseer bord
            # Nested list d*d bord
            # Coordinaat uitgang 
            # Bevat voertuigen (DICT -> A : ["H", 2, 1, 2]) (laat hier voertuigen initaliseren, dus import data om dat te doen)
        #FUNCTIE Welke auto's zijn beweegbaar? -> Na elke move refresh
            # Loopen door alle auto's op het bord
                # Wat is voor en achter voor dit voertuig?
                # coordinaat pakken indexeren collum en row.
                # Als V of H -> x of y + en - 1 en size moet doen 
                # Is een van die locaties leeg?
                # Ja -> voeg auto aan lijst (dict?) toe
            # Return dict  
        #FUNCTIE Plekken ingenomen door voertuigen -> Na elke move refresh
            # Ga alle voertuigen af:
            # Per voertuig sla de locaties op die hij inneemt
                # For loop lengte voertuig
                    # als V: x = xcoordinaatv, y = ycoordinaatv +i, 
                    # Als H: x = xcoordinaatv + i, y = ycoordinaatv
                    # Sla x en y op als list
                    # Sla dict op Key = Voertuigletter, value = lijst x en y, VofH en grote
                    # Sla list op in set en 
            # Return set met daarin lists
        #FUNCTIE Locatie lege plekken
            # Alle coordinaten - coordinatenvoertuigen (LET OP DAT DIT KAN VOOR HET DATATYPE) (Set)
        #FUNCTIE Beweeg voertuig
            # Vraag voertuigletter
            # Verander voertuig dmv FUNCTIE LOCATIE in voertuigen class
        # Bevat einddoellocatie rood
        # Visualiserend het bord met verschillende kleuren. 
        # Donkergrijze border om d bij d lichtgrijs bord

    # Voertuigen
class voertuigen(object)
    def __init__(self) -> None:
        # Grote -> Verandert niet
        # Verticaal / horizontaal -> Verandert niet
        # Rood of niet rood -> Verandert niet
        # Locatie voertuig -> Start is hetzelfde per bord -> daarna verandering
        # FUNCTIE LOCATIE
            # Verander locatie -> nieuwe coordinaten

# MAIN:        
    # Roep Bord aan (die roept automatisch voertuigen aan)
    # Check of rode auto pad vrij heeft (als er niks staat voor de rode auto)
        # Ja -> +1 move, beweeg rode auto naar einde, end game
    # Nee ga door    
    # Eerst checken welke autos op dit moment schuifbaar zijn, dus lege plekken voor of achter zich hebben

    # Hoeveel is die auto schuifbaar? (dus -1 tot + 2 bijv)
        # Ga bij die auto van -1 totdat het geen lege plek meer is (while loop)
            # Sla data ergens op
        # Ga bij de auto van +1 totdat het geen lege plek meer is (while loop)
            # Sla data ergens op
    # Random 1 auto kiezen? -> later niet random
    # Random plaatsverandering +1 move (een random cijfer van verplaatsbaarheid dat niet 0 is) -> later niet random
    # Plaatsverandering opgeslaan.
    
    # Als endgame publiceer move
    