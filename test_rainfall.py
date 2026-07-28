import pandas as pd

from risk_engine.rainfall import (
    detect_rainfall_risk
)

def test_rainfall():

    df = pd.DataFrame({

        "Rainfall":[
            20,
            60,
            120
        ]

    })

    result = detect_rainfall_risk(df)

    assert result[
        "Heavy Rainfall"
    ] == 2