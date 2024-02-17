from os import walk, path
import pygame

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

def import_folder(path_to_folder):
    surf_lst = []
    for _,_,img_files in walk(path_to_folder):
        for img in img_files:
            full_path = path.join(path_to_folder, img)
            img_surf = pygame.image.load(full_path).convert_alpha()
            surf_lst.append(img_surf)
    return surf_lst
