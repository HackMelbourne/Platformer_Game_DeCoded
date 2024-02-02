from os import walk
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

tile_types = {
    'T': 'C:\\Users\\Dhruv\\Desktop\\workshop\\Platformer_Game_DeCoded\\graphics\\Tiles\\grassMid.png',
    'X': 'C:\\Users\\Dhruv\\Desktop\\workshop\\Platformer_Game_DeCoded\\graphics\\Tiles\\grassCenter.png',
    'C': 'C:\\Users\\Dhruv\\Desktop\\workshop\\Platformer_Game_DeCoded\\graphics\\Tiles\\castleMid.png',
    'M': 'C:\\Users\\Dhruv\\Desktop\\workshop\\Platformer_Game_DeCoded\\graphics\\Tiles\\castleCenter.png',
}

base = 'C:\\Users\\Dhruv\\Desktop\\workshop\\Platformer_Game_DeCoded\\graphics\\'
tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size

def import_folder(path):
    surf_lst = []
    for _,_,img_files in walk(path):
        for img in img_files:
            full_path = path + '\\' + img
            img_surf = pygame.image.load(full_path).convert_alpha()
            surf_lst.append(img_surf)
    return surf_lst