from os import walk, path
import pygame

initial_level_map = [
'                                                        ',
'                                                        ',
'                                                        ',
'       TTT        TTT TT           TTT        TTT TT    ',
'                T                         T             ',
'              TT       TTTT               XT       TTTT ',
'            TT  TT         T            TT  TT         T',
'          TTXX      TTT    X          TTXX      TTT    X',
'          XXXX        XT   X          XXXX        XT   X',
'    TTTT  XXXXTT  TT  XXTTTX    TTTT  XXXXTT  TT  XXTTTX',
'TTTTXXXXTTXXXXXXTTXXTTXXXXXXTTTTXXXXTTXXXXXXTTXXTTXXXXXX'
]

player_level_map = [
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

door_level_map = [
'                                                        ',
'                                                        ',
'                                                        ',
'       CCC        CCC CC           CCC        CCC CC    ',
'    P           C                         C             ',
'              CC       CCCC               MC       CCCC ',
'          J CC  CC         C            CC  CC         C',
'          CCMM      CCC    M          CCMM      CCC    M',
'          MMMM        MC   M          MMMM        MC   M',
'    CCCC  MMMMCC  CC  MMCCCM    CCCC  MMMMCC  CC  MMCCCM',
'CCCCMMMMCCMMMMMMCCMMCCMMMMMMCCCCMMMMCCMMMMMMCCMMCCMMMMMM'
]

door_level_map2 = [
'                                                        ',
'                                                        ',
'                                                        ',
'       CCC        CCC CC           CCC        CCC CC    ',
'    P           C                         C             ',
'                       CCCC               MC       CCCC ',
'                           C            CC  CC         C',
'                CCCCCCC    M          CCMM      CCC    M',
'    CC    CCCC        MC   M          MMMM        MC   M',
'    MMCC  MMMMCC  CC  MMCCCM    CCCC  MMMMCC  CC  MMCCCM',
'CCCCMMMMCCMMMMMMCCMMCCMMMMMMCCCCMMMMCCMMMMMMCCMMCCMMMMMM'
]

normal_level_map = [
'                                                        ',
'                                                        ',
'                                                        ',
'       TTT        TTT TT           TTT        TTT TT    ',
'    P           T                         T             ',
'             ETT       TTTT               XT       TTTT ',
'            TT  TT         T           ETT  TT         T',
'          TTXX      TTT    X          TTXX      TTT    X',
'          XXXX        XT   X          XXXX        XT   X',
'    TTTT  XXXXTT  TT  XXTTTX    TTTT  XXXXTT  TT  XXTTTX',
'TTTTXXXXTTXXXXXXTTXXTTXXXXXXTTTTXXXXTTXXXXXXTTXXTTXXXXXX'
]

level_map = [
'                                                        ',
'                                                        ',
'                                    E                   ',
'       CCC        CCC CC           CCC        CCC CC    ',
'    P           C       E                 C           J ',
'              CC       CCCC              EMC       CCCC ',
'           ECC  CC         C           ECC  CC         C',
'          CCMM      CCC    M          CCMM      CCCE   M',
'          MMMM    E   MC   M          MMMM        MC   M',
'    CCCC  MMMMCC  CC  MMCCCM    CCCC EMMMMCC  CC  MMCCCM',
'CCCCMMMMCCMMMMMMCCMMCCMMMMMMCCCCMMMMCCMMMMMMCCMMCCMMMMMM'
]

level_map2 = [
'                                                        ',
'                                                        ',
'                                    E                   ',
'       CCC        CCC CC           CCC        CCC CC    ',
'    P           C       E                 C             ',
'              CC       CCCC              EMC       CCCC ',
'           ECC  CC         C           ECC  CC         C',
'          CCMM      CCC    M          CCMM      CCCE   M',
'          MMMM    E   MC   M          MMMM        MC   M',
'    CCCC  MMMMCC  CC  MMCCCM    CCCC EMMMMCC  CC  MMCCCM',
'CCCCMMMMCCMMMMMMCCMMCCMMMMMMCCCCMMMMCCMMMMMMCCMMCCMMMMMM'
]

base_path = path.join(path.dirname(__file__), '..', 'graphics')

tile_types = {
    'T': path.join(base_path, 'Tiles', 'grassMid.png'),
    'X': path.join(base_path, 'Tiles', 'grassCenter.png'),
    'C': path.join(base_path, 'Tiles', 'castleMid.png'),
    'M': path.join(base_path, 'Tiles', 'castleCenter.png'),
}

tile_size = 64
clock_tick = 1000
screen_width = 1200
screen_height = len(level_map) * tile_size
