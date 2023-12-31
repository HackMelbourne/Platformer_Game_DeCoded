normal_level_map = [
'                                                        ',
'                                                        ',
'                                                        ',
'       TTT        TTT TT           TTT        TTT TT    ',
'    P           T                         T             ',
'              TT       TTTT               XT       TTTT ',
'            TT  TT         T            TT  TT         T',
'          TTXX      TTT    X          TTXX      TTT    X',
'          XXXX        XT   X          XXXX        XT   X',
'    TTTT  XXXXTT  TT  XXTTTX    TTTT  XXXXTT  TT  XXTTTX',
'TTTTXXXXTTXXXXXXTTXXTTXXXXXXTTTTXXXXTTXXXXXXTTXXTTXXXXXX'
]

level_map = [
'                                                        ',
'                                                        ',
'                                                        ',
'       CCC        CCC CC           CCC        CCC CC    ',
'    P           C                         C             ',
'              CC       CCCC               MC       CCCC ',
'            CC  CC         C            CC  CC         C',
'          CCMM      CCC    M          CCMM      CCC    M',
'          MMMM        MC   M          MMMM        MC   M',
'    CCCC  MMMMCC  CC  MMCCCM    CCCC  MMMMCC  CC  MMCCCM',
'CCCCMMMMCCMMMMMMCCMMCCMMMMMMCCCCMMMMCCMMMMMMCCMMCCMMMMMM'
]

tile_types = {
    'T': '../graphics/Tiles/grassMid.png',
    'X': '../graphics/Tiles/grassCenter.png',
    'C': '../graphics/Tiles/castleMid.png',
    'M': '../graphics/Tiles/castleCenter.png',
}

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
