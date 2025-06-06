def keszit_diagram_sort(nap_szama, homerseklet):
    csillagok_szama = int(homerseklet)
    csillagok = '*' * csillagok_szama
    sor = f"Nap {nap_szama:2}: {csillagok} ({homerseklet}°C)"
    return sor
#függvény egy sor diagramot hoz létre egy nap hőmérsékletének vizualizálásához.

def rajzolj_diagram(homersekletek):
    print("Napi átlaghőmérséklet diagram (°C)")
    print("-" * 40)
#minden naphoz elkészíti a megfelelő sort
    
    for i in range(len(homersekletek)):
        nap = i + 1  # Napok számozása 1-től indul
        sor = keszit_diagram_sort(nap, homersekletek[i])
        print(sor)


napi_atlaghomersekletek = [12, 15, 14, 16, 13, 17, 18]

rajzolj_diagram(napi_atlaghomersekletek)

#minden egyes naphoz egy külön ciklust futtat le
