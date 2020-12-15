def testaa(sana):
    """Testaa onko sana vähintään viisi merkkiä pitkä ja sisältääkö sana
    sekä kirjaimia että numeroita."""

    return (len(sana) >= 5 and not(sana.isdigit() or sana.isalpha()))

