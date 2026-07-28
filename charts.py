import plotly.express as px
import plotly.graph_objects as go


def temperature_chart(climate_df):

    fig = px.line(
        climate_df,
        x="Date",
        y="Temp_Max",
        title="Temperature Trend"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Temperature (°C)",
        template="plotly_white"
    )

    return fig


def rainfall_chart(climate_df):

    fig = px.bar(
        climate_df,
        x="Date",
        y="Rainfall",
        title="Rainfall Trend"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Rainfall (mm)",
        template="plotly_white"
    )

    return fig


def forecast_chart(forecast_df):

    fig = px.line(
        forecast_df,
        x="ds",
        y="yhat",
        title="Temperature Forecast"
    )

    fig.update_layout(
        xaxis_title="Forecast Date",
        yaxis_title="Predicted Temperature (°C)",
        template="plotly_white"
    )

    return fig


def confidence_interval_chart(forecast_df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=forecast_df["ds"],
            y=forecast_df["yhat"],
            mode="lines",
            name="Forecast"
        )
    )

    if "yhat_upper" in forecast_df.columns:

        fig.add_trace(
            go.Scatter(
                x=forecast_df["ds"],
                y=forecast_df["yhat_upper"],
                mode="lines",
                name="Upper Confidence",
                line=dict(dash="dash")
            )
        )

    if "yhat_lower" in forecast_df.columns:

        fig.add_trace(
            go.Scatter(
                x=forecast_df["ds"],
                y=forecast_df["yhat_lower"],
                mode="lines",
                name="Lower Confidence",
                line=dict(dash="dash")
            )
        )

    fig.update_layout(
        title="Forecast Confidence Interval",
        xaxis_title="Date",
        yaxis_title="Temperature (°C)",
        template="plotly_white"
    )

    return fig