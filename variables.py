import os
import sys

proxies = [

    'http://80.90.80.54:8080', 'http://umhnxdxl:db70460384@107.174.143.220:36505',
    'http://umhnxdxl:db70460384@172.245.103.125:36505', 'http://umhnxdxl:db70460384@107.174.139.141:36505',
    'http://umhnxdxl:db70460384@192.3.126.142:36505', 'http://umhnxdxl:db70460384@107.174.143.231:36505',
    'http://umhnxdxl:db70460384@192.3.126.146:36505', 'http://umhnxdxl:db70460384@198.23.169.86:36505',
    'http://umhnxdxl:db70460384@23.94.177.130:36505', 'http://umhnxdxl:db70460384@23.94.177.151:36505',

    'http://ghulrcuk:bad3428050@192.227.241.105:36505', 'http://rcrvtkug:21d0ec259e@23.94.75.149:36505',
    'http://rcrvtkug:21d0ec259e@198.46.174.110:36505', 'http://rcrvtkug:21d0ec259e@107.172.65.205:36505',
    'http://ghulrcuk:bad3428050@107.172.227.249:36505', 'http://ghulrcuk:bad3428050@171.22.121.42:36505',
    'http://ghulrcuk:bad3428050@23.94.32.57:36505', 'http://ghulrcuk:bad3428050@23.94.32.28:36505',
    'http://ghulrcuk:bad3428050@198.46.201.164:36505',

    'http://ghulrcuk:bad3428050@198.12.66.196:36505', 'http://rcrvtkug:21d0ec259e@198.46.203.46:36505',
    'http://rcrvtkug:21d0ec259e@192.227.253.235:36505', 'http://ghulrcuk:bad3428050@171.22.121.131:36505',
    'http://rcrvtkug:21d0ec259e@107.172.71.71:36505',

    'http://rcrvtkug:21d0ec259e@192.3.147.213:36505',
    'http://ghulrcuk:bad3428050@172.245.103.97:36505',
    'http://rcrvtkug:21d0ec259e@198.46.176.68:36505',
    'http://rcrvtkug:21d0ec259e@172.245.242.237:36505'

]
groups = ['@CRYPTOMOONGEMs', '@dexgemschat', '@uniswapgemspumpz', '@defisearch', '@gemcollectors', '@moonhunters',
          '@supergemhunter', '@themoonboyschat', '@UniswapGemGroup', '@jumpsquad', '@BitSquad', '@uniswapresearch',
          '@shitcoincz', '@DeFiRaccoons', '@CryptoFamilyGroup', '@CryproPriceTalks', '@TheSelectiveApe',
          '@BSCStreetBetsCaptain', '@BSCApe', '@bscgemz', '@RedRoomTG', '@moonshotcartel', '@uniswaptalk',
          '@uniswaprektplebs', '@tehmoonwalkers', '@cryptodakurobinhooders', '@wolfonairechatbox', '@SmartChainApes',
          '@BitSquad', '@Satoshi_club', '@CryptoFamilyGroup', '@elliotradescrypto', '@TradeCoinUnderGround',
          '@cryptodakurobinhooders', '@moonhunters', '@tehMoonwalkeRs', '@DeFiRaccoons', '@uniswapgemsv2', '@de_fi',
          '@gemcollectors', '@cryptoM00NShots', '@dexgemschat', '@uniswapresearch', '@infinitygainzz', '@uniswaplegit',
          '@acmecrypto', '@oddgemsfamilia', '@thegemhunterstg', '@uniswapgemspumpz', '@WhalersClub101', '@Uniswapchina',
          '@Cryptosupportservices', '@uniswapgem123', '@UniswapEarlyCalls', '@crypto_revolution1',
          '@overdose_gems_group', '@GemSnipers', '@InfinityGainzz', '@unigemchatz', '@supergemhunter',
          '@The_Trading_Pit', '@deficrew', '@Farmingroom', '@Pumpchads', '@uniswapone', '@shitcoincz',
          '@uniswap_gem_alerts', '@binancedextrading', '@uniswapunofficial', '@CryproPriceTalks', '@gemsfordegensgroup',
          '@gemdiscussion', '@gemtalkc', '@InfinityBotz', '@cryptomindsgroup', '@themoonboyschat', '@sgdefi',
          '@UniswapGemGroup', '@Uniswap_Gem_Dicuss', '@defisearch', '@SuicidalPumpGroup', '@illuminatiGem']

api_id = 4014948
api_hash = 'c2774cd88072d9bf329442f1eefa6612'
api_id_test = 5893246
api_hash_test = "0c9b26086f1d626b2e778b02b1f7d141"


def get_base_path():
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS

    except Exception:
        return None
    return base_path
