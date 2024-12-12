# MIC to exchange name
mic2name = dict(
    sorted(
        {
            "BMEX": "Bolsas y Mercados Españoles",
            "XAMS": "Euronext Amsterdam",
            "XBRU": "Euronext Brussels",
            "XCSE": "Nasdaq Copenhagen A/S",
            "XDUB": "Irish Stock Exchange",
            "XETR": "XETRA",
            "XHEL": "Nasdaq Helsinki LTD",
            "XLIS": "Euronext Lisbon",
            "XLON": "London Stock Exchange",
            "XMIL": "Borsa Italiana S.P.A.",
            "XOSL": "Oslo Børs ASA",
            "XPAR": "Euronext Paris",
            "XSTO": "Nasdaq Stockholm AB",
            "XSWX": "SIX Swiss Exchange",
            "XWBO": "Wiener Börse AG",
            "XIST": "Borsa Istanbul",
            "XWAR": "Warsaw Stock Exchange",
            "ASEX": "Athens Stock Exchange",
            "XPRA": "Prague Stock Exchange",
            "XBUD": "Budapest Stock Exchange",
            "XJSE": "Johannesburg Stock Exchange",
            "XTAE": "Tel Aviv Stock Exchange",
            "XNYS": "New York Stock Exchange",
            "XNAS": "Nasdaq Stock Exchange",
            "XTSE": "Toronto Stock Exchange",
        }.items()
    )
)

# All supported operating MICs.
operating_mics = sorted(list(mic2name.keys()))

# Set of supported operating MICs.
# @unique
# class ExchangeEnum(str, Enum):
#     BMEX = "Bolsas y Mercados Españoles"
#     XAMS = "Euronext Amsterdam"
#     XBRU = "Euronext Brussels"
#     XCSE = "Nasdaq Copenhagen A/S"
#     XDUB = "Irish Stock Exchange"
#     XETR = "XETRA"
#     XHEL = "Nasdaq Helsinki LTD"
#     XLIS = "Euronext Lisbon"
#     XLON = "London Stock Exchange"
#     XMIL = "Borsa Italiana S.P.A."
#     XOSL = "Oslo Børs ASA"
#     XPAR = "Euronext Paris"
#     XSTO = "Nasdaq Stockholm AB"
#     XSWX = "SIX Swiss Exchange"
#     XWBO = "Wiener Börse AG"
#     XIST = "Borsa Istanbul"
#     XWAR = "Warsaw Stock Exchange"
#     ASEX = "Athens Stock Exchange"
#     XPRA = "Prague Stock Exchange"
#     XBUD = "Budapest Stock Exchange"
#     XJSE = "Johannesburg Stock Exchange"
#     XTAE = "Tel Aviv Stock Exchange"
#     XNYS = "New York Stock Exchange"
#     XNAS = "Nasdaq Stock Exchange"
#     XTSE = "Toronto Stock Exchange"