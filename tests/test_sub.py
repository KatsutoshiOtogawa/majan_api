"""test module sub"""

import json
from typing import List
import pytest
from majan import main


@pytest.mark.parametrize(('inputfile', 'expectfile'), [
    ("files/input.txt", "files/expect.txt"),
])
def test_sub(inputfile: str, expectfile: str):
    """_summary_

    Args:
        inputfile (str): 入力ファイル名
        expectfile (str): 予想出力ファイル名
    """
    # inputlines = get_file_read(inputfile)
    # expectlines = list(map(int, get_file_read(expectfile)))

    # output = main.sub(inputlines)
    ## ファイル読み込んで辞書にする
    inputjson_data = main.json_file_read('files/input.json')

    ## 辞書から役を計算
    output_point = main.calc_point(inputjson_data)
    
    ## 必要なデータだけjsonデータとして返す。
    output =main.hand_result2json(output_point)

    ## 期待するデータ
    expect_data = main.json_file_read('files/input.json')

    assert json.loads(output) == expect_data
