import streamlit as st
from textblob import TextBlob

# Daftar kata positif dan negatif
positive_words = {'baik', 'bagus', 'lengkap', 'mantap', 'top', 'good', 'nice',
                  'manfaat', 'bantu', 'mudah', 'rekomendasi', 'sederhana', 'menarik',
                  'terimakasih', 'keren', 'puas', 'jelas', 'lancar', 'aman', 'nyaman',
                  'untung', 'ada', 'tersedia', 'terdaftar', 'dapat', 'jos'}
negative_words = {'lambat', 'jelek', 'aneh', 'heran', 'gagal', 'emosi', 'kecewa', 
                  'ganggu', 'sebal', 'tidak ada', 'tidak bisa', 'tidak dapat', 
                  'buruk', 'tidak jelas', 'tidak sesuai', 'freeze', 'sulit', 'lag', 
                  'bug', 'keluar', 'rusak', 'ups', 'haduh', 'eror', 'terhambat', 
                  'blokir', 'payah', 'hilang', 'tidak terdaftar', 'tidak tersedia', 
                  'ribet', 'riweh', 'pusing', 'parah', 'bobrok', 'maintenance', 
                  'kendala', 'masalah', 'down', 'buruk', 'dadak', 'lama', 'tai', 
                  'anjing'}

def detect_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"

def detect_custom_sentiment(text):
    words = text.lower().split()
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    if negative_count > positive_count:
        return "Negative"
    elif positive_count > negative_count:
        return "Positive"

# Streamlit UI
st.title("Sentiment Analysis")

# Membatasi ukuran kolom teks dengan CSS agar lebih sempit
st.markdown("""
    <style>
    .stTextArea textarea {
        width: 300px !important;
    }
    </style>
""", unsafe_allow_html=True)

text = st.text_input("Input Text:")
sentiment =''

if st.button('Analyze Sentiment'):
    if text:
        sentiment = detect_sentiment(text)
        custom_sentiment = detect_custom_sentiment(text)

        # Menentukan warna berdasarkan sentimen
        if custom_sentiment == "Negative":
            st.markdown(f"Sentiment Review: <span style='color:red; font-weight:bold;'>{custom_sentiment}</span>", unsafe_allow_html=True)
        elif custom_sentiment == "Positive":
            st.markdown(f"Sentiment Review: <span style='color:green; font-weight:bold;'>{custom_sentiment}</span>", unsafe_allow_html=True)
        else:
            st.write(f"Complete Review!")
    else:
        st.write("Please input text for analyze!")

# Tambahkan credit di pojok kiri bawah
st.markdown("""
    <style>
    .credit {
        position: fixed;
        bottom: 10px;
        left: 10px;
        font-size: 13px;
        color: gray;
    }
    </style>
    <div class="credit">SALSA FEBRILIANA SANDITA | 24050121130088 | STATISTIKA UNDIP 2025</div>
""", unsafe_allow_html=True)
