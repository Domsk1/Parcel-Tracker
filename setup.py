import json

slugs = [
    "Courier Slug",
    "italy-sda",
    "specialisedfreight-za",
    "ensenda",
    "india-post-int",
    "bpost",
    "chronopost-portugal",
    "ptt-posta",
    "fastway-za",
    "spain-correos-es",
    "saudi-post",
    "dpd-ireland",
    "austrian-post-registered",
    "kerry-logistics",
    "posten-norge",
    "thailand-post",
    "hong-kong-post",
    "portugal-seur",
    "international-seur",
    "yrc",
    "canada-post",
    "aramex",
    "gati-kwe",
    "dhl-global-mail-asia",
    "dhl-poland",
    "asendia-usa",
    "envialia",
    "magyar-posta",
    "nova-poshta",
    "cambodia-post",
    "xend",
    "2go",
    "chronopost-france",
    "sgt-it",
    "globegistics",
    "nightline",
    "tnt-au",
    "acscourier",
    "uk-mail",
    "siodemka",
    "kn",
    "safexpress",
    "skynet",
    "nipost",
    "oca-ar",
    "aeroflash",
    "dhl-global-mail",
    "sapo",
    "taqbin-hk",
    "deltec-courier",
    "mexico-senda-express",
    "mexico-redpack",
    "japan-post",
    "sagawa",
    "viettelpost",
    "postnl-3s",
    "tiki",
    "opek",
    "ceska-posta",
    "geodis-calberson-fr",
    "ppbyb",
    "taqbin-jp",
    "apc",
    "ups-mi",
    "professional-couriers",
    "gojavas",
    "cj-gls",
    "ups-freight",
    "singapore-speedpost",
    "taiwan-post",
    "nacex-spain",
    "lasership",
    "china-ems",
    "taqbin-sg",
    "bgpost",
    "brazil-correios",
    "fedex",
    "ukrposhta",
    "jam-express",
    "estes",
    "dtdc",
    "interlink-express",
    "austrian-post",
    "star-track",
    "first-logistics",
    "postnord",
    "belpost",
    "cyprus-post",
    "spanish-seur",
    "air21",
    "lbcexpress",
    "vnpost",
    "rl-carriers",
    "sf-express",
    "lietuvos-pastas",
    "ec-firstclass",
    "an-post",
    "usps",
    "swiss-post",
    "india-post",
    "aupost-china",
    "danmark-post",
    "gls-netherlands",
    "dpd-uk",
    "hrvatska-posta",
    "posta-romana",
    "courierpost",
    "gdex",
    "singapore-post",
    "tnt-fr",
    "fastway-au",
    "new-zealand-post",
    "poste-italiane",
    "hermes-de",
    "wahana",
    "dynamic-logistics",
    "taqbin-my",
    "dhl",
    "citylinkexpress",
    "wedo",
    "malaysia-post-posdaftar",
    "pos-indonesia",
    "pos-indonesia-int",
    "xdp-uk",
    "portugal-ctt",
    "hermes",
    "fastway-ireland",
    "raf",
    "yundaex",
    "delhivery",
    "dpe-za",
    "equick-cn",
    "ecom-express",
    "tnt-click",
    "4px",
    "jcex",
    "post56",
    "dhl-es",
    "transmission-nl",
    "la-poste-colissimo",
    "gls-italy",
    "malaysia-post",
    "sto",
    "elta-courier",
    "postnl-international",
    "toll-ipec",
    "asendia-de",
    "correosexpress",
    "ecargo-asia",
    "fercam",
    "dawnwing",
    "jayonexpress",
    "apc-overnight",
    "bert-fr",
    "tuffnells",
    "ninjavan",
    "airpak-express",
    "imxmail",
    "norsk-global",
    "parcelpost-sg",
    "gofly",
    "empsexpress",
    "detrack",
    "old-dominion",
    "airspeed",
    "jne",
    "pandulogistics",
    "mondialrelay",
    "lion-parcel",
    "ups",
    "australia-post",
    "dhl-nl",
    "israel-post-domestic",
    "skynetworldwide",
    "tnt",
    "parcel-force",
    "abf",
    "directlink",
    "dhlparcel-nl",
    "greyhound",
    "dhl-germany",
    "gls",
    "i-parcel",
    "colissimo",
    "poczta-polska",
    "bpost-international",
    "taxydromiki",
    "skynetworldwide-uk",
    "rpxonline",
    "17postservice",
    "ghn",
    "israel-post",
    "yodel",
    "trakpak",
    "redur-es",
    "bluedart",
    "emirates-post",
    "szdpex",
    "qxpress",
    "courier-plus",
    "800bestex",
    "courierit",
    "dhl-deliverit",
    "dbschenker-se",
    "xpressbees",
    "dotzot",
    "korea-post",
    "yodel-international",
    "mypostonline",
    "panther",
    "collectplus",
    "tntpost-it",
    "boxc",
    "deutsch-post",
    "first-flight",
    "asm",
    "brt-it",
    "colis-prive",
    "estafeta",
    "dhl-benelux",
    "mrw-spain",
    "toll-priority",
    "tnt-it",
    "tnt-uk",
    "arrowxl",
    "tgx",
    "ontrac",
    "star-track-express",
    "fedex-uk",
    "exapaq",
    "wishpost",
    "sic-teliway",
    "packlink",
    "sweden-posten",
    "canpar",
    "myhermes-uk",
    "ramgroup-za",
    "dhl-pieceid",
    "speedexcourier",
    "speedcouriers-gr",
    "dpd",
    "dmm-network",
    "vnpost-ems",
    "dsv",
    "sfb2c",
    "russian-post",
    "flytexpress",
    "abxexpress-my",
    "kangaroo-my",
    "yanwen",
    "posti",
    "cnexps",
    "zjs-express",
    "asendia-uk",
    "cbl-logistica",
    "correos-chile",
    "dpd-poland",
    "newgistics",
    "easy-mail",
    "fastrak-th",
    "fastway-nz",
    "nanjingwoyuan",
    "lwe-hk",
    "yunexpress",
    "ubi-logistics",
    "purolator",
    "bondscouriers",
    "nationwide-my",
    "jet-ship",
    "rpx",
    "nhans-solutions",
    "cuckooexpress",
    "bh-posta",
    "rzyexpress",
    "rrdonnelley",
    "post-serbia",
    "costmeticsnow",
    "correos-de-mexico",
    "fedex-freight",
    "quantium",
    "tnt-reference",
    "tnt-uk-reference",
    "xdp-uk-reference",
    "Apr 72",
    "dpex",
    "dpd-de",
    "oneworldexpress",
    "delcart-in",
    "sekologistics",
    "kerryttc-vn",
    "postur-is",
    "ninjavan-my",
    "hh-exp",
    "srekorea",
    "parcelled-in",
    "couriers-please",
    "adsone",
    "smsa-express",
    "inpost-paczkomaty",
    "omniparcel",
    "dhl-hk",
    "kgmhub",
    "con-way",
    "echo",
    "matkahuolto",
    "china-post",
    "postnl",
    "lao-post",
    "raben-group",
    "360lion",
    "pfcexpress",
    "matdespatch",
    "rocketparcel",
    "raiderex",
    "cpacket",
    "yto",
    "adicional",
    "sfcservice",
    "directfreight-au",
    "skypostal",
    "xq-express",
    "dpe-express",
    "idexpress",
    "buylogic",
    "courex",
    "scudex-express",
    "b2ceurope",
    "expeditors",
    "thecourierguy",
    "dtdc-au",
    "ninjavan-id",
    "imexglobalsolutions",
    "alphafast",
    "landmark-global",
    "roadbull",
    "geodis-espace",
    "simplypost",
    "dhl-global-forwarding",
    "interlink-express-reference",
    "jersey-post",
    "directlog",
    "jocom",
    "sendle",
    "ekart",
    "hunter-express",
    "xl-express",
    "yakit",
    "zyllem",
    "dhl-active-tracing",
    "eparcel-kr",
    "dex-i",
    "brt-it-parcelid",
    "holisol",
    "sendit",
    "mailamericas",
    "copa-courier",
    "mara-xpress",
    "mikropakket",
    "wndirect",
    "kiala",
    "ruston",
    "wanbexpress",
    "cj-korea-thai",
    "wise-express",
    "rpd2man",
    "acommerce",
    "panther-reference",
    "wiseloads",
    "rincos",
    "alliedexpress",
    "hermes-it",
    "asendia-hk",
    "ninjavan-thai",
    "eurodis",
    "whistl",
    "abcustom",
    "tipsa",
    "ninjavan-philippines",
    "zto-express",
    "nim-express",
    "alljoy",
    "doora",
    "collivery",
    "gsi-express",
    "rcl",
    "mxe",
    "birdsystem",
    "paquetexpress",
    "line",
    "efs",
    "instant",
    "kpost",
    "collectco",
    "ddexpress",
    "smooth",
    "panther-order-number",
    "sailpost",
    "tcs",
    "ezship",
    "nova-poshtaint",
    "skynetworldwide-uae",
    "demandship",
    "pickup",
    "mainfreight",
    "aprisaexpress",
    "shreetirupati",
    "omniva",
    "acsworldwide",
    "janco",
    "dylt",
    "uds",
    "zepto-express",
    "skybox",
    "jinsung",
    "amazon-fba-us",
    "saia-freight",
    "star-track-courier",
    "dpd-ro",
    "sky-postal",
    "wepost",
    "palexpress",
    "chitchats",
    "aduiepyle",
    "pilot-freight",
    "ecms",
    "jx",
    "bestwayparcel",
    "zinc",
    "etotal",
    "xpost",
    "lonestar",
    "m-xpress",
    "gls-cz",
    "cj-malaysia",
    "bjshomedelivery",
    "bneed",
    "cj-malaysia-international",
    "dtdc-express",
    "deliveryontime",
    "k1-express",
    "alfatrex",
    "parcelpoint",
    "ep-box",
    "pickupp-sgp",
    "pickupp-mys",
    "dpd-ru",
    "j-net",
    "trans-kargo",
    "lht-express",
    "dpd-hk",
    "clevy-links",
    "bluecare",
    "chrobinson",
    "cjlogistics",
    "dbschenker-sv",
    "post-slovenia",
    "bluestar",
    "megasave",
    "007ex",
    "pixsell",
    "cloudwish-asia",
    "dhlparcel-es",
    "cj-philippines",
    "shippit",
    "shopfans",
    "pitney-bowes",
    "shree-maruti",
    "tophatterexpress",
    "celeritas",
    "dimerco",
    "skynet-za",
    "fedex-crossborder",
    "mailplus",
    "spoton",
    "tolos",
    "kwt",
    "sap-express",
    "sending",
    "sypost",
    "qualitypost",
    "intexpress",
    "seino",
    "jtexpress",
    "linkbridge",
    "national-sameday",
    "shiptor",
    "bh-worldwide",
    "parcel2go",
    "endeavour-delivery",
    "kerrytj",
    "aaa-cooper",
    "aersure",
    "mglobal",
    "watkins-shepard",
    "ocs",
    "descartes",
    "champion-logistics",
    "usf-reddaway",
    "latvijas-pasts",
    "fedex-fims",
    "sefl",
    "danske-fragt",
    "gso",
    "sf-express-webhook",
    "efex",
    "wmg",
    "paack-webhook",
    "apc-overnight-connum",
    "usps-webhook",
    "osm-worldwide",
    "expeditors-api",
    "seko-sftp",
    "antron",
    "pickupp-vnm",
    "janio",
    "brt-it-sender-ref",
    "kurasi",
    "gls-spain",
    "total-express",
    "newzealand-couriers",
    "lotte",
    "fmx",
    "knuk",
    "hx-express",
    "shippify",
    "gls-croatia",
    "dpd-fr-reference",
    "dhl-supply-chain-au",
    "always-express"
]

config = {
    "api_key": "YOUR API-KEY HERE (https://api.aftership.com/v4)",
    "email": "YOUR EMAIL HERE",
    "lang": "en",
    "parcels": [
        {
            "tracking_number": "YOUR-TRACKING-HERE",
            "slug": "YOUR PARCEL SERVICE HERE (Pick from slug.json)"
        }
    ]
}


def setup_slugs():
    """Set up slugs and config without user config"""
    with open("slugs.json", "w") as f:
        json.dump(slugs, f, indent=4)


def setup_config():
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)


def bat():
    with open("run.bat", "w") as f:
        f.write("tracker.exe\npause")
