
import streamlit as st
from movie_recommender import recommend

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Movie Recommendation Website",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------
# WEBSITE HEADER
# --------------------------------

st.title("🎬 Movie Recommendation Website")

st.header("Discover Your Next Favourite Movie")

st.write(
    "Find movies similar to your favourite films "
    "using our content-based recommendation system."
)

st.divider()

# --------------------------------
# MOVIE SEARCH SECTION
# --------------------------------

st.subheader("Search for a Movie")

movie_name = st.text_input(
    "Enter the name of a movie",
    placeholder="Example: Avatar"
)

if st.button("Recommend Movies", type="primary"):

    if movie_name.strip():

        with st.spinner("Finding similar movies..."):

            results = recommend(movie_name)

        if results:

            st.success("Here are your recommendations!")

            st.subheader("Your Recommended Movies")

            # Create five columns
            cols = st.columns(5)

            # Display recommendations
            for i, movie in enumerate(results):

                with cols[i]:
                    st.markdown(f"### {i + 1}")
                    st.markdown(f"**{movie}**")
                    st.caption("Recommended Movie")

        else:
            st.warning(
                "Movie not found. Please check the spelling."
            )

    else:
        st.warning("Please enter a movie name!")

# --------------------------------
# EXPLORE SECTION
# --------------------------------

st.divider()

st.subheader("Explore Our System")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Movie Discovery")
    st.write(
        "Discover movies that share similar characteristics "
        "with the movie you already enjoy."
    )

with col2:
    st.markdown("### Recommendation Engine")
    st.write(
        "Our system uses content-based filtering, "
        "movie metadata and similarity calculations."
    )

# --------------------------------
# FOOTER
# --------------------------------

st.divider()

st.caption(
    "Movie Recommendation System | Built with Python and Streamlit"
)
