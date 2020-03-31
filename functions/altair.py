import altair as alt


def generate_time_series_chart_meta(df, x, y):
    chart = alt.Chart(df).mark_line().encode(
        alt.X("{}:T".format(x)),
        alt.Y("{}:Q".format(y), scale=alt.Scale(zero=False))
    )
    return chart.to_dict()
