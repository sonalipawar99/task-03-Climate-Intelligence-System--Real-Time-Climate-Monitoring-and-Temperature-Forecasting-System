import pandas as pd

from risk_engine.heatwave import (
    detect_heatwaves
)

def test_heatwave():

    df = pd.DataFrame({

        "Temp_Max":[
            35,
            42,
            47
        ]

    })

    result = detect_heatwaves(df)

    assert result[
        "Heatwave Days"
    ] == 2