def moving_average(df, column, window=5):
    return df[column].rolling(window).mean()

def health_score(df):
    score = 100

    if df["voltage"].mean() > 240 or df["voltage"].mean() < 180:
        score -= 20

    if df["temperature"].mean() > 75:
        score -= 30

    if df["load"].mean() > 85:
        score -= 20

    return max(score, 0)

def generate_insights(df):
    insights = []

    if df["temperature"].iloc[-1] > df["temperature"].mean():
        insights.append("Temperature is rising")

    if df["load"].iloc[-1] > 90:
        insights.append("Load nearing critical capacity")

    if df["voltage"].std() > 15:
        insights.append("Voltage instability detected")

    return insights