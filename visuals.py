# visuals.py
import plotly.express as px

def plot_qb_performance(df):
    """
    Creates an animated bubble chart showing Passing Yards vs Touchdowns
    moving through the Weeks.
    """
    fig = px.scatter(
        df,
        x="PassingYards",
        y="Touchdowns",
        animation_frame="Week",    # This creates the play button/slider
        animation_group="Player",  # This tells Plotly which dot is which player
        size="PassingYards",       # Bubble size based on yards
        color="Team",              # Color by team
        hover_name="Player",
        range_x=[0, 500],          # Fixed range so the chart doesn't jump around
        range_y=[0, 6],
        title="Quarterback Performance Evolution (Week by Week)",
        template="plotly_dark"     # "Dark" theme looks modern/gaming style
    )
    
    # Customizing for a "Visually Pleasing" look
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", # Transparent background
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Arial", size=14, color="white")
    )
    
    return fig

def plot_metric_card(label, value, delta):
    """
    Returns a simple metric styling (Streamlit handles this natively well).
    This function is just a placeholder if you want custom metric visuals later.
    """
    pass