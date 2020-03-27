import altair as alt


def generate_time_series_chart_meta(df, x, y):
    chart = alt.Chart(df).mark_line().encode(
        x="{}:T".format(x),
        y="{}:Q".format(y)
    )
    return chart.to_dict()
