#計算
from mahjong.hand_calculating.hand import HandCalculator
#麻雀牌
from mahjong.tile import TilesConverter
#役, オプションルール
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
#鳴き
from mahjong.meld import Meld
#風(場&自)
from mahjong.constants import EAST, SOUTH, WEST, NORTH

import json
#HandCalculator(計算用クラス)のインスタンスを生成
calculator = HandCalculator()

#結果出力用
def hand_result2json(hand_result) -> str:
    """上がった形をjson形式でデータとして返す。

    Args:
        hand_result (_type_): _description_

    Returns:
        str: _description_
    """

    ## yaku_leveはハネ満とか。
    dic = {
        'yaku_level': hand_result.cost['yaku_level']
        ,'han': hand_result.han
        ,'fu': hand_result.fu
        ,'total': hand_result.cost['total']
        ,'yaku': list(map(str, hand_result.yaku))
        ,'detail': {
            'const': hand_result.cost
            ,'fu': hand_result.fu_details
        }
    }
    # #翻数, 符数
    # print(hand_result.han, hand_result.fu)
    # #点数(ツモアガリの場合[左：親失点, 右:子失点], ロンアガリの場合[左:放銃者失点, 右:0])
    # print(hand_result.cost['main'], hand_result.cost['additional'])
    # #役
    # print(hand_result.yaku)
    # #符数の詳細
    # for fu_item in hand_result.fu_details:
    #     print(fu_item)

    ## jsonにダンプ。
    dumped_json = json.dumps(dic)

    return dumped_json


def json_file_read(filepath: str) -> any:
    json_open = open(filepath, 'r')
    json_load = json.load(json_open)

    return json_load

def calc_point(json_data: any) -> any:
    """_summary_

    Args:
        data (any): jsonで手配の状況、上がり方などを計算する。
    """

    tiles = TilesConverter.string_to_136_array(**json_data['tehai'])

    # #アガリ牌
    win_tile = TilesConverter.string_to_136_array(**json_data['agarihai'])[0]

    #鳴き(なし)
    melds = json_data.get('melds')

    ## dora_indicators 表示配なので次の値がドラになる。
    # TilesConverter.string_to_136_array(man='1')[0],  in json_data.get('dora_indicators')['sow'] json_data.get('dora_indicators')['pin']
    # 後で実装
    
    #ドラ(なし)
    dora_indicators = json_data.get('dora_indicators')

    # option 青天井ルールとか赤ドラアリとか
    option = OptionalRules(**json_data['options'])

    # ツモったか、リーチしてたか、自分の風、場の風などの設定。
    config = HandConfig(**json_data['config'],options=option)

    ## ここから分ける。
    #計算
    result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)

    return result

def main():
    ## ファイル読み込んで辞書にする
    json_data = json_file_read('files/input.json')

    ## 辞書から役を計算
    result = calc_point(json_data)
    
    ## jsonデータとして返す。
    output_json = hand_result2json(result)

    print(output_json)

if __name__ == '__main__':
    main()
