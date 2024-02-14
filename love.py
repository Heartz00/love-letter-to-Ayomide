import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Romantic Letter to My Crush", page_icon="❤️")
    
    # Video background
    # Set background image
   st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://drive.google.com/file/d/12s1Pztj96yk3_Fgy_WQ-wcQfRZQznhpa/view?usp=sharing")
    }
   .sidebar .sidebar-content {
        background: url("https://drive.google.com/file/d/1uxWget3iqpndrZKamzV9nz0Alh7Lkhnt/view?usp=sharing")
    }
    </style>
    """,
    unsafe_allow_html=True
)

    st.title("A Letter to Omo Adeyanju, aya nobody🙂")

    st.write(
        """
        As I sit down to pen these words, my heart races with the melody of emotions that only you can compose within me. Valentine's Day has arrived, and it serves as the perfect chance to express the feelings that have blossomed in the garden of my soul—feelings that have taken root and grown into a symphony of love.

        From the very first glance we exchanged, something magical ignited within me. Your laughter became the sweetest melody I've ever heard, and your smile (like the one in the video below- pure joy), a masterpiece that brightened even the darkest days. In the quiet moments, it's the sound of your voice that brings me peace, (especially when you call, “Oladele Ayomide”) like a familiar song that soothes my soul.

        I want you to know that you've become an inspiration behind my future plans as a spiritual man. Every memory we've created together holds a special place in my heart. Whether it's the shared jokes that still make me chuckle or the stolen glances that speak volumes, each moment with you is a cherished note in the melody of our love story.

        As I reminisce about our journey together, I can't help but smile at the beautiful memories we've woven into the fabric of our relationship. The late-night and long conversations that lasted until dawn mostly when we are supposed to be reading in white house (smiles), the adventures that made our hearts race, and even the quiet moments where we simply enjoyed each other's company – these are the moments that define us, the moments that make our bond crazy.

        Even though we've had our share of disagreements, those moments were just me trying to navigate our future together. I dislike confrontations actually, it saddens me to see you angry; I'd rather be in a heated argument and still be talking to you than endure a prolonged silence. As we celebrate this day dedicated to love, I want you to know that you've changed me in ways I never thought possible.

        I am happy that I got to know you, I usually hear people say someone brighten up their days, omoo I actually experienced that with you firsthand. Sadly, I do not know if this will be my final valentine gift to you, as I expect your sincere answer to my question soon. But it has been a good memory.

        I know words do not really matter to you, but i hope my actions so far has been able to prove to you how much you mean to me and how much I have fallen in love with you, Ademide.

        Ayomide Oladele

        """
    )

    # Displaying additional pictures
    st.image(Image.open("IMG_20230626_153329_359.jpg"), caption="The day we both signed out", use_column_width=True)
    st.image(Image.open("IMG_20230523_113433_316.jpg"), caption="Big head was trying to kiss your cheek", use_column_width=True)
 
    # Displaying additional videos
    st.video("post1.mp4", start_time=0)
    st.video("post this.mp4", start_time=0)

if __name__ == "__main__":
    main()
