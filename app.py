# ==========================================================
# Airbnb Analytics Dashboard
# Part 1
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------------
# Page Config
# ----------------------------------------------------------

st.set_page_config(
    page_title="Airbnb Analytics Dashboard",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(r"C:\Users\Mubeen Khan\OneDrive\Desktop\Data-analytics-visulaition-project\airbnb_clean.csv")

df = load_data()

df["neighbourhood group"] = df["neighbourhood group"].astype(str).str.strip()
df["room type"] = df["room type"].astype(str).str.strip()

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------

st.sidebar.title("🏠 Airbnb Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Price Analysis",
        "Location Analysis",
        "Host Analysis",
        "Market Insights"
    ]
)

# ----------------------------------------------------------
# Filters
# ----------------------------------------------------------

boroughs = ["All"] + sorted(df["neighbourhood group"].dropna().unique().tolist())

selected_borough = st.sidebar.selectbox(
    "Neighbourhood Group",
    boroughs
)

room_types = ["All"] + sorted(df["room type"].dropna().unique().tolist())

selected_room = st.sidebar.selectbox(
    "Room Type",
    room_types
)

filtered_df = df.copy()

if selected_borough != "All":
    filtered_df = filtered_df[
        filtered_df["neighbourhood group"] == selected_borough
    ]

if selected_room != "All":
    filtered_df = filtered_df[
        filtered_df["room type"] == selected_room
    ]

# ==========================================================
# Plot Functions
# ==========================================================

def price_distribution(data):

    fig = px.histogram(
        data,
        x="price",
        nbins=40,
        template="plotly_white",
        title="Distribution of Airbnb Listing Prices",
        color_discrete_sequence=["royalblue"]
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title="Price (£)",
        yaxis_title="Listings"
    )

    return fig


def borough_price(data):

    avg_price = (
        data.groupby("neighbourhood group")["price"]
        .mean()
        .reset_index()
        .sort_values("price", ascending=False)
    )

    fig = px.bar(
        avg_price,
        x="neighbourhood group",
        y="price",
        color="price",
        template="plotly_white",
        color_continuous_scale="Viridis",
        title="Average Listing Price by Neighbourhood Group"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title="Neighbourhood Group",
        yaxis_title="Average Price (£)",
        coloraxis_showscale=False
    )

    return fig


def room_price(data):

    fig = px.box(
        data,
        x="room type",
        y="price",
        color="room type",
        template="plotly_white",
        title="Price Distribution by Room Type",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_layout(
        title_x=0.5,
        showlegend=False,
        xaxis_title="Room Type",
        yaxis_title="Price (£)"
    )

    return fig


def neighbourhood_chart(data):

    top = (
        data["neighbourhood"]
        .value_counts()
        .head(15)
        .reset_index()
    )

    top.columns = ["Neighbourhood", "Listings"]

    fig = px.bar(
        top,
        x="Listings",
        y="Neighbourhood",
        orientation="h",
        color="Listings",
        template="plotly_white",
        color_continuous_scale="Blues",
        title="Top 15 Neighbourhoods"
    )

    fig.update_layout(
        title_x=0.5,
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False
    )

    return fig


def verification_chart(data):

    fig = px.box(
        data,
        x="host_identity_verified",
        y="price",
        color="host_identity_verified",
        template="plotly_white",
        title="Host Verification vs Price",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_layout(
        title_x=0.5,
        showlegend=False
    )

    return fig


def instant_booking_chart(data):

    fig = px.violin(
        data,
        x="instant_bookable",
        y="price",
        color="instant_bookable",
        box=True,
        template="plotly_white",
        title="Instant Booking vs Price",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_layout(
        title_x=0.5,
        showlegend=False
    )

    return fig


def availability_chart(data):

    fig = px.box(
        data,
        x="room type",
        y="availability 365",
        color="room type",
        template="plotly_white",
        title="Availability by Room Type",
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    fig.update_layout(
        title_x=0.5,
        showlegend=False
    )

    return fig


# ==========================================================
# HOME
# ==========================================================

if page == "Home":

    st.title("🏠 Airbnb Analytics Dashboard")

    st.markdown(
        """
        ### Interactive Business Intelligence Dashboard

        This dashboard explores Airbnb listings using
        interactive Plotly visualisations.

        Use the sidebar to navigate through the analyses.
        """
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Listings",
        f"{len(filtered_df):,}"
    )

    c2.metric(
        "Average Price",
        f"£{filtered_df['price'].mean():.2f}"
    )

    c3.metric(
        "Average Rating",
        f"{filtered_df['review rate number'].mean():.2f}"
    )

    c4.metric(
        "Average Availability",
        f"{filtered_df['availability 365'].mean():.0f}"
    )

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(
        filtered_df.head(),
        use_container_width=True
    )

    st.subheader("Dataset Statistics")

    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
    else:
        st.dataframe(
            filtered_df.select_dtypes(include="number").describe().T,
            use_container_width=True
        )

# ==========================================================
# PRICE ANALYSIS
# ==========================================================

elif page == "Price Analysis":

    st.title("💰 Price Analysis")

    st.markdown(
        "Explore Airbnb pricing trends across neighbourhoods and room types."
    )

    st.plotly_chart(
        price_distribution(filtered_df),
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            borough_price(filtered_df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            room_price(filtered_df),
            use_container_width=True
        )
# ==========================================================
# LOCATION ANALYSIS
# ==========================================================

elif page == "Location Analysis":

    st.title("📍 Location Analysis")

    st.plotly_chart(
        neighbourhood_chart(filtered_df),
        use_container_width=True
    )

    fig = px.scatter_mapbox(
        filtered_df,
        lat="lat",
        lon="long",
        color="price",
        size="price",
        hover_name="NAME",
        hover_data=[
            "room type",
            "neighbourhood group",
            "price"
        ],
        zoom=10,
        height=700,
        color_continuous_scale="Turbo",
        title="Geographical Distribution of Airbnb Listings"
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        margin=dict(r=0, t=50, l=0, b=0),
        title_x=0.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# HOST ANALYSIS
# ==========================================================

elif page == "Host Analysis":

    st.title("👤 Host Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            verification_chart(filtered_df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            instant_booking_chart(filtered_df),
            use_container_width=True
        )

    st.plotly_chart(
        availability_chart(filtered_df),
        use_container_width=True
    )

# ==========================================================
# MARKET INSIGHTS
# ==========================================================

elif page == "Market Insights":

    st.title("📈 Market Insights")

    bubble = px.scatter(
        filtered_df,
        x="number of reviews",
        y="price",
        size="availability 365",
        color="room type",
        hover_name="NAME",
        opacity=0.7,
        template="plotly_white",
        title="Reviews vs Price vs Availability",
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    bubble.update_layout(
        title_x=0.5,
        xaxis_title="Number of Reviews",
        yaxis_title="Price (£)"
    )

    st.plotly_chart(
        bubble,
        use_container_width=True
    )

    corr = filtered_df.select_dtypes(include="number").corr()

    heatmap = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Correlation Matrix"
    )

    heatmap.update_layout(
        title_x=0.5
    )

    st.plotly_chart(
        heatmap,
        use_container_width=True
    )

    st.subheader("Summary")

    st.success(
        """
        • Price varies substantially across room types.

        • Neighbourhood influences listing concentration.

        • Host verification has minimal impact on pricing.

        • Instant booking shows little effect on listing prices.

        • Entire homes generally command higher prices.

        • Multiple variables collectively influence Airbnb pricing.
        """
    )