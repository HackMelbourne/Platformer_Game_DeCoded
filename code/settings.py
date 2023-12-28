level_map = [
'                                                        ',
'                                                        ',
'                                                        ',
'       TTT        TTT TT           TTT        TTT TT    ',
'    P           T                         T             ' ,
'              TT       TTTT               XT       TTTT ',
'            TT  TT         T            TT  TT         T',
'          TTXX      TTT    X          TTXX      TTT    X',
'          XXXX        XT   X          XXXX        XT   X',
'    TTTT  XXXXTT  TT  XXTTTX    TTTT  XXXXTT  TT  XXTTTX',
'TTTTXXXXTTXXXXXXTTXXTTXXXXXXTTTTXXXXTTXXXXXXTTXXTTXXXXXX']

tile_types = {
    'T': '../graphics/Tiles/grassMid.png',
    'X': '../graphics/Tiles/grassCenter.png',
}

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
