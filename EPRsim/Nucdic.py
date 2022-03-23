# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:35:34 2017

Libraries with the all relevant nuclear spins and gyromagnetic ratios.
The spin is given as mutliplicity for all nuclear spins unequal zero for
all non-radiocative isotopes.
The corresponding gyromagnetic ratio is is given as Nuclear-Bohrmagneton
in the unit of MHz/T. Before the value is returned it is transformed
to Hz/mT.


Main functions:
dictionary_Nuclear_spins()
Nuc_zeemandict()

@author: Stephan Rein, University of Freiburg, 2017
"""
import EPRsim.Tools as tool


def isotopes_catalogue(element):
    """
    Catalogue of isotopes for a given element

    Parameters
    ----------
    element : :class:`string`
              Abbreviation of the element name (e.g., "H", "Mn", "Fe", ....)


    Returns
    -------
    field : :class:`list`
            List of strings with all stable isotopes of the element.


    See Also
    --------
    nuclear_properties : Elementary information about a specific isotope

    Notes
    -------

    This is a cataloge of stable isotopes (non-radioactive isotopes) for
    each element reaching from hydrogen to uranium. The function
    nuclear_properties() can be used to get detailed information about a
    specific isotope.

    Examples
    --------

    Get isotopes of nitrogen, calcium and vanadium

    >>> import cwEPRsim.Nucdic as nucdic
    >>> Isotopes = nucdic.isotopes_cataloge("N")
    >>> print(Isotopes)
    ['14N', '15N']
    >>> Isotopes2 = nucdic.isotopes_cataloge("Ca")
    >>> print(Isotopes2)
    ['42Ca', '43Ca', '44Ca', '46Ca', '48Ca']
    >>> Isotopes3 = nucdic.isotopes_cataloge("V")
    >>> print(Isotopes3)
    ['50V', '51V']
    """

    Isotopes = {
        "H": ["1H", "2H"],
        "He": ["3He"],
        "Li": ["6Li", "7Li"],
        "Be": ["9Be"],
        "B": ["10B", "11B"],
        "C": ["12C", "13C"],
        "N": ["14N", "15N"],
        "O": ["16O", "17O", "18O"],
        "F": ["19F"],
        "Ne": ["20Ne", "21Ne", "22Ne"],
        "Na": ["22Na", "23Na"],
        "Mg": ["24Mg", "25Mg", "26Mg"],
        "Al": ["27Al"],
        "Si": ["29Si", "30Si"],
        "P": ["31P"],
        "S": ["32S", "33S", "34S", "36S"],
        "Cl": ["35Cl", "37Cl"],
        "Ar": ["36Ar", "38Ar", "40Ar"],
        "K": ["39K", "40K", "41K"],
        "Ca": ["42Ca", "43Ca", "44Ca", "46Ca", "48Ca"],
        "Sc": ["45Sc"],
        "Ti": ["46Ti", "47Ti", "48Ti", "49Ti", "50Ti"],
        "V": ["50V", "51V"],
        "Cr": ["50Cr", "52Cr", "53Cr", "54Cr"],
        "Mn": ["55Mn"],
        "Fe": ["54Fe", "56Fe", "57Fe", "58Fe"],
        "Co": ["59Co"],
        "Ni": ["58Ni", "60Ni", "61Ni", "62Ni", "64Ni"],
        "Cu": ["63Cu", "65Cu"],
        "Zn": ["64Zn", "66Zn", "67Zn", "68Zn", "70Zn"],
        "Ga": ["69Ga", "71Ga"],
        "Ge": ["70Ge", "72Ge", "73Ge", "74Ge", "76Ge"],
        "As": ["75As"],
        "Se": ["74Se", "76Se", "77Se", "78Se", "80Se", "82Se"],
        "Br": ["79Br", "81Br"],
        "Kr": ["78Kr", "80Kr", "82Kr", "83Kr", "84Kr", "86Kr"],
        "Rb": ["85Rb", "87Rb"],
        "Sr": ["84Sr", "86Sr", "87Sr", "88Sr"],
        "Y": ["89Y"],
        "Zr": ["90Zr", "91Zr", "92Zr", "94Zr", "96Zr"],
        "Nb": ["93Nb"],
        "Mo": ["92Mo", "94Mo", "95Mo", "96Mo", "97Mo", "98Mo", "100Mo"],
        "Tc": ["99Tc"],
        "Ru": ["96Ru", "98Ru", "99Ru", "100Ru", "101Ru", "102Ru", "104Ru"],
        "Rh": ["103Rh"],
        "Pd": ["102Pd", "104Pd", "105Pd", "106Pd", "108Pd", "110Pd"],
        "Ag": ["107Ag", "109Ag"],
        "Cd": ["106Cd", "108Cd", "110Cd", "111Cd", "112Cd", "113Cd", "114Cd", "116Cd"],
        "In": ["113In", "115In"],
        "Sn": [
            "112Sn",
            "114Sn",
            "115Sn",
            "116Sn",
            "117Sn",
            "118Sn",
            "119Sn",
            "120Sn",
            "122Sn",
            "124Sn",
        ],
        "Sb": ["121Sb", "123Sb"],
        "Te": ["120Te", "122Te", "123Te", "124Te", "125Te", "126Te", "128Te", "130Te"],
        "I": ["127I"],
        "Xe": [
            "124Xe",
            "126Xe",
            "128Xe",
            "129Xe",
            "130Xe",
            "131Xe",
            "132Xe",
            "134Xe",
            "136Xe",
        ],
        "Cs": ["133Cs"],
        "Ba": ["130Ba", "132Ba", "134Ba", "135Ba", "136Ba", "137Ba", "138Ba"],
        "La": ["138La", "139La"],
        "Ce": ["136Ce", "138Ce", "140Ce", "142Ce"],
        "Pr": ["141Pr"],
        "Nd": ["142Nd", "143Nd", "144Nd", "145Nd", "146Nd", "148Nd", "150Nd"],
        "Pm": ["147Pm"],
        "Sm": ["144Sm", "147Sm", "148Sm", "149Sm", "150Sm", "152Sm", "154Sm"],
        "Eu": ["151Eu", "153Eu"],
        "Gd": ["152Gd", "154Gd", "155Gd", "156Gd", "157Gd", "158Gd", "160Gd"],
        "Tb": ["159Tb"],
        "Dy": ["156Dy", "158Dy", "160Dy", "161Dy", "162Dy", "163Dy", "164Dy"],
        "Ho": ["165Ho"],
        "Er": ["162Er", "164Er", "166Er", "167Er", "168Er", "170Er"],
        "Tm": ["169Tm"],
        "Yb": ["168Yb", "170Yb", "171Yb", "172Yb", "173Yb", "174Yb", "176Yb"],
        "Lu": ["175Lu", "176Lu"],
        "Hf": ["174Hf", "176Hf", "177Hf", "178Hf", "179Hf", "180Hf"],
        "Ta": ["180Ta", "182Ta"],
        "W": ["180W", "182W", "183W", "184W", "186W"],
        "Re": ["185Re", "187Re"],
        "Os": ["184Os", "186Os", "187Os", "188Os", "189Os", "190Os", "192Os"],
        "Ir": ["191Ir", "193Ir"],
        "Pt": ["190Pt", "192Pt", "194Pt", "195Pt", "196Pt", "198Pt"],
        "Au": ["197Au"],
        "Hg": ["196Hg", "198Hg", "199Hg", "200Hg", "201Hg", "202Hg", "204Hg"],
        "Tl": ["203Tl", "205Tl"],
        "Pb": ["204Pb", "206Pb", "207Pb", "208Pb"],
        "Bi": ["209Bi"],
        "Th": ["232Th"],
        "U": ["235U", "238U"],
    }
    try:
        return Isotopes[element]
    except KeyError:
        return [element]


def nuclear_properties(nucleus, style=1):
    """
    Nuclear properties of a specific nuclear isotope

    Parameters
    ----------
    element : :class:`string`
              Abbreviation of the element name (e.g., "H", "Mn", "Fe", ....)

    style : :class:`int`
             Different units which are used for the nuclear spin properties.
             See Notes for detailed description of the styles.

    Returns
    -------
    prop : :class:`list`
            List with three elements. The first element is the gyromagnetic
            ratio or the nuclear g factor (different styles are explained
            below),
            the second element is the multiplicity M or the
            nuclear spin quantum number (different styles are explained
            below). The third element is the natural abundance normalized to
            one.

    Notes
    -------
    The different styles are listed in the table.

    =======  ================  =================   ================
     style      prop[0]            prop[1]              prop[2]
    =======  ================  =================   ================
    style=1   gyro. in MHz/mT    multiplicity      nat. abundance
    style=2   gyro. in MHz/mT  spin quantum num.   nat. abundance
    style=3  nuclear g-factor    multiplicity      nat. abundance
    style=4  nuclear g-factor  spin quantum num.   nat. abundance
    =======  ================  =================   ================


    Examples
    --------

    Information about a 14N isotopes using standard style (style=1).

    >>> import cwEPRsim.Nucdic as nucdic
    >>> N = nucdic.nuclear_properties("14N")
    >>> print(N)
    [3.077705887, 3, 0.99632]

    Information about a 1H isotopes using different styles.

    >>> import cwEPRsim.Nucdic as nucdic
    >>> H = nucdic.nuclear_properties("1H")
    >>> print(H)
    [42.57747876, 2, 0.99989]
    >>> H = nucdic.nuclear_properties("1H", 2)
    >>> print(H)
    [42.57747876, 0.5, 0.99989]
    >>> H = nucdic.nuclear_properties("1H", 3)
    >>> print(H)
    [5.585694680337019, 2, 0.99989]
    >>> H = nucdic.nuclear_properties("1H", 4)
    >>> print(H)
    [5.585694680337019, 0.5, 0.99989]

    Get direct access to only the nuclear g-factor of the 13C isotope.

    >>> import cwEPRsim.Nucdic as nucdic
    >>> C = nucdic.nuclear_properties("13C", 3)[0]
    >>> print(C)
    1.4048235948355339

    Get direct access to only the natural abundance of the 15N isotope.

    >>> import cwEPRsim.Nucdic as nucdic
    >>> N = nucdic.nuclear_properties("15N", 3)[2]
    >>> print(N)
    0.00368
    """

    Nuclear_spins = {
        # Name      gyro        2I+1     abundance
        "1H": [42.57747876, 2, 0.99989],
        "2H": [6.53590266, 3, 0.00011],
        "3He": [-32.434099669, 2, 0.9999],
        "6Li": [6.26613223, 3, 0.0759],
        "7Li": [16.5482765, 4, 0.9241],
        "9Be": [-5.983354599, 4, 1.0],
        "10B": [4.575194829, 7, 0.199],
        "11B": [13.662984, 4, 0.801],
        "12C": [0.0, 1, 0.9893],
        "13C": [10.7083989, 2, 0.017],
        "14N": [3.077705887, 3, 0.99632],
        "15N": [-4.3172667, 2, 0.00368],
        "16O": [0.0, 1, 0.99757],
        "17O": [-5.77423637, 6, 0.00038],
        "18O": [0.0, 1, 0.00205],
        "19F": [40.077583, 2, 1.00],
        "20Ne": [0.0, 1, 0.9048],
        "21Ne": [-3.3630729, 4, 0.0027],
        "22Ne": [0.0, 1, 0.0925],
        "22Na": [4.4363492, 7, 0.0],
        "23Na": [11.2688455, 4, 1.00],
        "24Mg": [0.0, 1, 0.7899],
        "25Mg": [-2.60829897, 6, 0.10],
        "26Mg": [0.0, 1, 0.1101],
        "27Al": [11.10309072, 6, 1.0],
        "28Si": [0.0, 1, 0.92229],
        "29Si": [-8.46549965, 2, 0.0468],
        "30Si": [0.0, 1, 0.03087],
        "31P": [17.25145312, 2, 1.0],
        "32S": [0.0, 1, 0.9493],
        "33S": [3.27172375, 4, 0.0076],
        "34S": [0.0, 1, 0.0429],
        "35S": [0.0, 1, 0.0002],
        "35Cl": [4.17654235, 4, 0.7578],
        "37Cl": [3.4765306396, 4, 0.2422],
        "36Ar": [0.0, 1, 0.003365],
        "38Ar": [0.0, 1, 0.000632],
        "40Ar": [0.0, 1, 0.996003],
        "39K": [1.98934439, 4, 0.932582],
        "40K": [-2.4737221, 9, 0.000117],
        "41K": [1.09191133, 4, 0.0673],
        "40Ca": [0.0, 1, 0.96941],
        "42Ca": [0.0, 1, 0.00647],
        "43Ca": [-2.8689154, 8, 0.00135],
        "44Ca": [0.0, 1, 0.02086],
        "46Ca": [0.0, 1, 0.00004],
        "48Ca": [0.0, 1, 0.000187],
        "45Sc": [10.359028, 8, 1.0],
        "46Ti": [0.0, 1, 0.0825],
        "47Ti": [-2.404089696, 6, 0.0744],
        "48Ti": [0.0, 1, 0.7372],
        "49Ti": [-2.40475286, 8, 0.0541],
        "50Ti": [0.0, 1, 0.0518],
        "50V": [4.25047083, 13, 0.0025],
        "51V": [11.213292, 8, 0.9975],
        "50Cr": [0.0, 1, 0.04345],
        "52Cr": [0.0, 1, 0.83789],
        "53Cr": [-2.4114836, 4, 0.09501],
        "54Cr": [0.0, 1, 0.02365],
        "55Mn": [10.5290881, 6, 1.0],
        "54Fe": [0.0, 1, 0.05845],
        "56Fe": [0.0, 1, 0.91754],
        "57Fe": [1.378927125, 2, 0.02119],
        "58Fe": [0.0, 1, 0.00282],
        "59Co": [10.077068, 8, 1.0],
        "58Ni": [0.0, 1, 0.680769],
        "60Ni": [0.0, 1, 0.26223],
        "61Ni": [-3.811372868, 4, 0.01399],
        "62Ni": [0.0, 1, 0.036345],
        "64Ni": [0.0, 1, 0.009256],
        "63Cu": [11.29973229, 4, 0.6917],
        "65Cu": [12.1031536, 4, 0.3083],
        "64Zn": [0.0, 1, 0.4863],
        "66Zn": [0.0, 1, 0.2790],
        "67Zn": [2.66937119, 6, 0.0410],
        "68Zn": [0.0, 1, 0.1875],
        "70Zn": [0.0, 1, 0.0062],
        "69Ga": [10.24773819, 4, 0.60108],
        "71Ga": [13.0208, 4, 0.39892],
        "70Ge": [0.0, 1, 0.2084],
        "72Ge": [0.0, 1, 0.2754],
        "73Ge": [-1.4897391, 10, 0.0763],
        "74Ge": [0.0, 1, 0.3628],
        "76Ge": [0.0, 1, 0.0773],
        "75As": [7.3150216, 4, 1.0],
        "74Se": [0.0, 1, 0.0089],
        "76Se": [0.0, 1, 0.0937],
        "77Se": [8.1567846, 1, 0.0763],
        "78Se": [0.0, 1, 0.2377],
        "80Se": [0.0, 1, 0.4961],
        "82Se": [0.0, 1, 0.0873],
        "79Br": [10.70415620, 4, 0.5069],
        "81Br": [11.53838, 4, 0.4961],
        "78Kr": [0.0, 1, 0.0035],
        "80Kr": [0.0, 1, 0.0228],
        "82Kr": [0.0, 1, 0.1158],
        "83Kr": [-1.64422386, 10, 0.1149],
        "84Kr": [0.0, 1, 0.5700],
        "86Kr": [0.0, 1, 0.1730],
        "85Rb": [4.125287, 6, 0.7217],
        "87Rb": [13.98143, 4, 0.2783],
        "84Sr": [0.0, 1, 0.0056],
        "86Sr": [0.0, 1, 0.0986],
        "87Sr": [-1.85107, 10, 0.0700],
        "88Sr": [0.0, 1, 0.8258],
        "89Y": [-2.0949, 2, 1.0],
        "90Zr": [0.0, 1, 0.5145],
        "91Zr": [-3.9748, 6, 0.1122],
        "92Zr": [0.0, 1, 0.1715],
        "94Zr": [0.0, 1, 0.1738],
        "96Zr": [0.0, 1, 0.0280],
        "93Nb": [10.45210, 10, 1.0],
        "92Mo": [0.0, 1, 0.1484],
        "94Mo": [0.0, 1, 0.0925],
        "95Mo": [-2.78758, 6, 0.1592],
        "96Mo": [0.0, 1, 0.1668],
        "97Mo": [-2.8463, 6, 0.0955],
        "98Mo": [0.0, 1, 0.2413],
        "100Mo": [0.0, 1, 0.963],
        "99Tc": [9.6289, 10, 1.0],
        "96Ru": [0.0, 1, 0.054],
        "98Ru": [0.0, 1, 0.0187],
        "99Ru": [-1.9514, 6, 0.1276],
        "100Ru": [0.0, 1, 0.1260],
        "101Ru": [-2.1953, 6, 0.1706],
        "102Ru": [0.0, 1, 0.3155],
        "104Ru": [0.0, 1, 0.1862],
        "103Rh": [1.3477, 2, 1.0],
        "102Pd": [0.0, 1, 0.0102],
        "104Pd": [0.0, 1, 0.1114],
        "105Pd": [-1.959, 6, 0.2233],
        "106Pd": [0.0, 1, 0.2733],
        "108Pd": [0.0, 1, 0.2646],
        "110Pd": [0.0, 1, 0.1172],
        "107Ag": [-1.7314, 2, 0.5184],
        "109Ag": [-1.9904, 2, 0.4816],
        "106Cd": [0.0, 1, 0.0125],
        "108Cd": [0.0, 1, 0.0089],
        "110Cd": [0.0, 1, 0.1249],
        "111Cd": [-9.0691, 2, 0.1289],
        "112Cd": [0.0, 1, 0.2413],
        "113Cd": [-9.4871, 2, 0.1222],
        "114Cd": [0.0, 1, 0.2873],
        "116Cd": [0.0, 1, 0.0749],
        "113In": [9.3651, 10, 0.0429],
        "115In": [9.3857, 10, 0.9571],
        "112Sn": [0.0, 1, 0.0097],
        "114Sn": [0.0, 1, 0.0066],
        "115Sn": [-14.008, 2, 0.0034],
        "116Sn": [0.0, 1, 0.1454],
        "117Sn": [-15.261, 2, 0.0768],
        "118Sn": [0.0, 1, 0.2422],
        "119Sn": [-15.966, 2, 0.0859],
        "120Sn": [0.0, 1, 0.3258],
        "122Sn": [0.0, 1, 0.0463],
        "124Sn": [0.0, 1, 0.0579],
        "121Sb": [10.255, 6, 0.5721],
        "123Sb": [5.5531, 8, 0.4279],
        "120Te": [0.0, 1, 0.0009],
        "122Te": [0.0, 1, 0.0255],
        "123Te": [-11.2349, 2, 0.0089],
        "124Te": [0.0, 1, 0.0474],
        "125Te": [-13.545, 2, 0.0707],
        "126Te": [0.0, 1, 0.1884],
        "128Te": [0.0, 1, 0.3174],
        "130Te": [0.0, 1, 0.3408],
        "127I": [8.5778, 6, 1.0],
        "124Xe": [0.0, 1, 0.0009],
        "126Xe": [0.0, 1, 0.0009],
        "128Xe": [0.0, 1, 0.0192],
        "129Xe": [-11.8604, 2, 0.2644],
        "130Xe": [0.0, 1, 0.0408],
        "131Xe": [3.5140, 4, 0.2118],
        "132Xe": [0.0, 1, 0.2689],
        "134Xe": [0.0, 1, 0.1044],
        "136Xe": [0.0, 1, 0.0887],
        "133Cs": [5.62335, 8, 1.0],
        "130Ba": [0.0, 1, 0.00106],
        "132Ba": [0.0, 1, 0.00101],
        "134Ba": [0.0, 1, 0.02417],
        "135Ba": [4.2582, 4, 0.06592],
        "136Ba": [0.0, 1, 0.07854],
        "137Ba": [4.7634, 4, 0.11232],
        "138Ba": [0.0, 1, 0.71698],
        "138La": [5.6615, 11, 0.0009],
        "139La": [6.06115, 8, 0.9991],
        "136Ce": [0.0, 1, 0.00185],
        "138Ce": [0.0, 1, 0.00251],
        "140Ce": [0.0, 1, 0.88450],
        "142Ce": [0.0, 1, 0.11114],
        "141Pr": [13.036, 6, 1.0],
        "142Nd": [0.0, 1, 0.2720],
        "143Nd": [-2.3196, 8, 0.1220],
        "144Nd": [0.0, 1, 0.2380],
        "145Nd": [-1.4254, 8, 0.0830],
        "146Nd": [0.0, 1, 0.1720],
        "148Nd": [0.0, 1, 0.0570],
        "150Nd": [0.0, 1, 0.0560],
        "147Pm": [5.618, 8, 1.0],
        "144Sm": [0.0, 1, 0.0307],
        "147Sm": [-1.76844, 8, 0.1499],
        "148Sm": [0.0, 1, 0.1124],
        "149Sm": [-1.4544, 8, 0.1382],
        "150Sm": [0.0, 1, 0.0738],
        "152Sm": [0.0, 1, 0.2675],
        "154Sm": [0.0, 1, 0.2275],
        "151Eu": [0.585, 6, 0.4781],
        "153Eu": [4.676, 6, 0.5219],
        "152Gd": [0.0, 1, 0.0020],
        "154Gd": [0.0, 1, 0.0218],
        "155Gd": [-1.307, 4, 0.1480],
        "156Gd": [0.0, 1, 0.2047],
        "157Gd": [-1.727, 4, 0.1565],
        "158Gd": [0.0, 1, 0.2484],
        "160Gd": [0.0, 1, 0.2186],
        "159Tb": [10.237, 4, 1.0],
        "156Dy": [0.0, 1, 0.0006],
        "158Dy": [0.0, 1, 0.0010],
        "160Dy": [0.0, 1, 0.0234],
        "161Dy": [-1.4635, 6, 0.1891],
        "162Dy": [0.0, 1, 0.2551],
        "163Dy": [2.0505, 6, 0.2490],
        "164Dy": [0.0, 1, 0.2818],
        "165Ho": [12.7145, 8, 1.0],
        "162Er": [0.0, 1, 0.0014],
        "164Er": [0.0, 1, 0.0161],
        "166Er": [0.0, 1, 0.3361],
        "167Er": [-1.228, 8, 0.2293],
        "168Er": [0.0, 1, 0.2678],
        "170Er": [0.0, 1, 0.1493],
        "169Tm": [-3.5216, 2, 1.0],
        "168Yb": [0.0, 1, 0.0013],
        "170Yb": [0.0, 1, 0.0304],
        "171Yb": [0.0, 1, 0.1428],
        "172Yb": [0.0, 1, 0.2183],
        "173Yb": [-1.9758, 6, 0.1613],
        "174Yb": [0.0, 1, 0.3183],
        "176Yb": [0.0, 1, 0.1276],
        "175Lu": [4.862, 8, 0.9741],
        "176Lu": [3.443, 15, 0.0259],
        "174Hf": [0.0, 1, 0.0016],
        "176Hf": [0.0, 1, 0.0526],
        "177Hf": [1.728, 8, 0.1860],
        "178Hf": [0.0, 1, 0.2728],
        "179Hf": [0.0, 1, 0.1362],
        "180Hf": [0.0, 1, 0.3508],
        "180Ta": [4.0865, 19, 0.00012],
        "181Ta": [5.1627, 8, 0.99988],
        "180W": [0.0, 1, 0.0012],
        "182W": [0.0, 1, 0.2650],
        "183W": [1.7957, 2, 0.1431],
        "184W": [0.0, 1, 0.3064],
        "186W": [0.0, 1, 0.2843],
        "185Re": [9.7173, 6, 0.3740],
        "187Re": [9.817, 6, 0.6260],
        "184Os": [0.0, 1, 0.0002],
        "186Os": [0.0, 1, 0.0159],
        "187Os": [0.9856, 2, 0.0196],
        "188Os": [0.0, 1, 0.1324],
        "189Os": [3.3536, 4, 0.1615],
        "190Os": [0.0, 1, 0.2626],
        "192Os": [0.0, 1, 0.4078],
        "191Ir": [0.76607, 4, 0.3730],
        "193Ir": [0.8316, 4, 0.6270],
        "190Pt": [0.0, 1, 0.00014],
        "192Pt": [0.0, 1, 0.00784],
        "194Pt": [0.0, 1, 0.32967],
        "195Pt": [9.2919, 2, 0.33832],
        "196Pt": [0.0, 1, 0.25242],
        "198Pt": [0.0, 1, 0.07163],
        "197Au": [0.7406, 4, 1.0],
        "196Hg": [0.0, 1, 0.0015],
        "186Hg": [0.0, 1, 0.0997],
        "199Hg": [7.7123, 2, 0.1687],
        "200Hg": [0.0, 1, 0.2310],
        "201Hg": [-2.8469, 4, 0.1318],
        "202Hg": [0.0, 1, 0.2986],
        "204Hg": [0.0, 1, 0.0687],
        "203Tl": [24.7316, 2, 0.29524],
        "205Tl": [4.9748, 2, 0.70476],
        "204Pb": [0.0, 1, 0.014],
        "206Pb": [0.0, 1, 0.241],
        "207Pb": [9.0337, 2, 0.221],
        "208Pb": [0.0, 1, 0.542],
        "209Bi": [6.9625, 10, 1.0],
        "232Th": [0.0, 1, 1.0],
        "235U": [-0.83086, 8, 0.0073],
        "238U": [0.0, 1, 0.9927],
    }
    Spininfo = Nuclear_spins[nucleus]
    if style == 1:
        pass
    elif style == 2:
        Spininfo = Nuclear_spins[nucleus]
        Spininfo[1] = (Spininfo[1] - 1) / 2
    elif style == 3:
        Spininfo = Nuclear_spins[nucleus]
        Spininfo[0] = tool.gyro2gn(Spininfo[0])
    elif style == 4:
        Spininfo = Nuclear_spins[nucleus]
        Spininfo[1] = (Spininfo[1] - 1) / 2
        Spininfo[0] = tool.gyro2gn(Spininfo[0])
    return Spininfo
