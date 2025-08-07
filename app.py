import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = "https://xmtisomtotyjbgtzblzg.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhtdGlzb210b3R5amJndHpibHpnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE4NzE2ODQsImV4cCI6MjA2NzQ0NzY4NH0.Pql_5kbWjv0OfAOgw0cJcZQu23Fdfj_E_1f-qyDRcHg"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Konfigurasi halaman
st.set_page_config(page_title="Pensiun Mandiri", layout="centered")

# Inisialisasi session state
if "halaman" not in st.session_state: 
    st.session_state["halaman"] = "home"

# Styling CSS
st.markdown("""
    <style>
    @media (min-width: 768px) {
        .block-container {
            padding-top: 1rem;
        }
    }
    @media (max-width: 767px) {
        .block-container {
            padding-top: 2rem;
        }
    }
    /* Styling untuk background */
    .stApp {
        background-color: white;    /* warna background */
        padding: 1px 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk navigasi dan refresh
def go_to(page):
    st.session_state["halaman"] = page
    st.rerun()

# ===============================
# FUNGSI HALAMAN UTAMA
# ===============================
def halaman_home():
    # Styling Judul
    st.markdown("""
<h1 style='color: black; 
        font-family:Georgia; 
        font-size:50px;
        font-weight: 600;
        '>Informasi Dana Pensiun</h1>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.image("gambar.png", caption="Ilustrasi Dana Pensiun", use_container_width=True)

    # Styling artikel
    st.markdown("""
        <style>
        .artikel {
            text-align: justify !important;
            font-size: 17px; 
            line-height: 1.5;
            color: black;
            margin-top: 2px; 
            margin-bottom: 30px;
        }
        </style>
    """, unsafe_allow_html=True) 

    # Isi artikel
    informasi = """
    <div class='artikel' style='font-size:18px; line-height:1.7;'>
    Banyak orang belum menyadari pentingnya mempersiapkan dana pensiun sejak usia muda.<br>

    <h3>💼 Kenapa Dana Pensiun Itu Penting?</h3>
    Padahal, dengan memulainya lebih awal, kita dapat meringankan beban keuangan di masa tua dan memastikan kebutuhan hidup tetap terpenuhi. 
    Masa pensiun adalah fase di mana penghasilan tetap biasanya sudah tidak ada, namun pengeluaran seperti biaya makan, tempat tinggal, dan kesehatan justru tetap ada—bahkan bisa meningkat. 
    Oleh karena itu, tanpa persiapan yang matang, risiko keuangan di masa pensiun bisa menjadi sangat berat.<br><br>

    <h4>Bayangkan ini 💭</h4>
    Kamu ingin menikmati masa tua dengan tenang, tanpa harus bergantung pada anak atau keluarga. Kamu ingin tetap bisa jalan-jalan, beli makanan enak, dan menjaga kesehatan—semua itu butuh persiapan.<br><br>

    <h3>📊 Apa Itu Dana Pensiun?</h3>
    Dana pensiun adalah <strong>tabungan atau investasi jangka panjang</strong> yang disiapkan untuk kebutuhan hidup saat kita tidak lagi bekerja. <br><br>
    Kebutuhan tersebut mencakup:<br>
        🍽️ Biaya makan dan kebutuhan harian<br>
        🏡 Tempat tinggal<br>
        💊 Biaya kesehatan<br>
        🎉 Hiburan & gaya hidup<br><br>
        

    <h3>🎯 Kenapa Harus Mulai dari Sekarang?</h3>
        <ul>
        <li><strong>Efek Compounding (bunga berbunga):</strong> Semakin awal mulai, semakin besar hasilnya. Uangmu bekerja untukmu.</li>
        <li><strong>Jaga Kualitas Hidup:</strong> Tetap mandiri dan sejahtera saat tua nanti.</li>
        <li><strong>Lawan Inflasi:</strong> Biaya hidup naik terus tiap tahun—persiapanmu juga harus naik.</li>
        </ul>

    <h3>🧮 Simulasikan Dana Pensiunmu Sekarang!</h3>
    Melalui aplikasi ini, kamu bisa dengan mudah menghitung estimasi kebutuhan dana pensiun di masa depan, hanya dengan memasukkan beberapa informasi berikut:<br>
        <ul>
        <li>Usia saat ini</li>
        <li>Target usia pensiun</li>
        <li>Pengeluaran bulanan saat ini</li>
        <li>Nilai inflasi (kenaikan harga barang dan jasa secara umum dalam suatu periode waktu tertentu)</li>
        <li>Return investasi (persentase keuntungan dari uang yang diinvestasikan)</li>
        </ul>
    </div>
    """
    st.markdown(informasi, unsafe_allow_html=True)

    st.markdown("""
    ### 📝 Langkah-Langkah Melakukan Simulasi

   <div style="padding-left: 12px; font-size: 17px;">
    <p>1️⃣ <b>Masukkan Usia Saat Ini</b><br>
        Masukkan umur anda saat ini di slider yang tersedia.</p>

    <p>2️⃣ <b>Tentukan Usia Pensiun</b><br>
        Tentukan kapan anda ingin pensiun di slider yang tersedia.</p>

    <p>3️⃣ <b>Isi Kebutuhan Hidup Bulanan Saat Pensiun</b><br>
        Perkirakan kebutuhan hidup anda per bulan saat pensiun (dalam Rupiah).</p>

    <p>4️⃣ <b>Atur Inflasi dan Return Investasi</b><br>
        Sesuaikan nilai inflasi yang terjadi dan return investasi yang anda inginkan.</p>

    <p>5️⃣ <b>Klik Tombol "🔍 Hitung Kebutuhan Pensiun"</b><br>
        Sistem akan menghitung dan menampilkan berapa yang harus anda tabung setiap bulan.</p>

    <p>6️⃣ <b>Lihat Hasil Perhitungan</b><br>
        Hasil akan ditampilkan secara lengkap: kebutuhan bulanan, tahunan, dan total tabungan yang harus disiapkan.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("➡️ Mulai Simulasi"):
        st.session_state["hasil"] = None
        go_to("simulasi")

    # styling button "simulasi"
    st.markdown("""
    <style>
    div.stButton > button {
        padding: 8px 16px;
        background-color: white;
        border: 3px solid #74C365 !important;
        color: white;
        border-radius: 10px !important;
        border: none;
        width: auto;
        min-width: 250px;
        max-width: 100%;
        margin: 0 auto;
        display: block;
    }
    /* Styling huruf dalam button */
    div.stButton > button > div > p {
    font-size: 22px !important;
    font-weight: 550 !important;
    color: black !important
}       
                
    div.stButton > button:hover {
    background-color: #74C365!important;
        color: white ! important; 
        font-weight: bold !important;
        text-decoration: none !important;
        
}
    </style>
""", unsafe_allow_html=True)

# ===============================
# FUNGSI HALAMAN SIMULASI
# ===============================
def halaman_simulasi():
    # Styling judul
    st.markdown("""
<h1 style='color:black; 
        font-family:Georgia; 
        font-size:50px;
        font-weight: 600;
        '>🧮 Simulasi Dana Pensiun</h1>
""", unsafe_allow_html=True)

    # Jika tombol reset di klik maka semua data yang telah diinput hilang
    if st.session_state.get("reset_input", False):
        for key in ["usia_sekarang", "pensiun", "inflasi", "kebutuhan", "hasil"]:
            if key in st.session_state:
                del st.session_state[key]
    st.session_state["reset_input"] = False
    
    if "hasil" not in st.session_state:
        st.session_state["hasil"] = None

    # Masukkan Pengguna
    usia_sekarang = st.slider("Berapa usia Anda sekarang?", 18, 50, 25, key="usia_sekarang")
    pensiun = st.slider("Target usia pensiun?", 30, 70, 55, key="pensiun")
    inflasi = st.slider("Inflasi (%)", 0.02, 0.18, 0.03, step=0.01, key="inflasi")
    st.caption("📉 Berdasarkan data 5 tahun terakhir rata-rata inflasi yang terjadi di Indonesia adalah 2,5% per tahun")

    investasi = st.slider("Return investasi (%)", 0.02, 0.20, 0.15, step=0.01, key="investasi")
    st.caption("🗠 Return investasi yang ideal untuk dana pensiun adalah 15%")

    kebutuhan = st.number_input("Kebutuhan hidup per bulan saat pensiun (Rp)", min_value=0,
    value=None, placeholder="Masukkan nominal dalam rupiah", step=1000, format="%d", key="kebutuhan")

    if kebutuhan is not None:
        st.caption(f"🧮 Format dalam bentuk uang: **Rp {kebutuhan:,.0f}**")
    else:
        st.caption("🧮 Format dalam bentuk uang: Rp -")

    # Button hitung & reset
    col1, col2 = st.columns([1, 1])

    # Button hitung
    with col1:

     if st.button("🔍 Hitung Kebutuhan Pensiun"):

        # Perhitungan
        if kebutuhan is not None and kebutuhan > 0 and pensiun > usia_sekarang:
            usia_pensiun = pensiun - usia_sekarang
            durasi = usia_pensiun * 12
            i = investasi / 12

            nilai_bulanan = kebutuhan * (1 + inflasi) ** usia_pensiun
            nilai_tahunan = nilai_bulanan * 12
            total_tabungan = nilai_tahunan / 0.04
           
            tabungan_bulanan = total_tabungan / (((1 + i)**durasi - 1) / (i / (1 + i)))

             # Simpan ke Supabase
            
            data = {
                "usia_awal": usia_sekarang,
                "usia_pensiun": pensiun,
                "inflasi": inflasi,
                "return_investasi": investasi,
                "kebutuhan_bulanan": int(kebutuhan),
                "kebutuhan_bulanan_masa_depan": int(nilai_bulanan),
                "kebutuhan_tahunan_masa_depan": int(nilai_tahunan),
                "tabungan_bulanan": int(tabungan_bulanan),
                "total_tabungan": int(total_tabungan)
            }
            supabase.table("simulasi_pensiun").insert(data).execute()

            # Cetak hasil Perhitungan
            st.session_state["hasil"] = {
                "nilai_bulanan": nilai_bulanan,
                "nilai_tahunan": nilai_tahunan,
                "total_tabungan": total_tabungan,
                "tabungan_bulanan": tabungan_bulanan
            }
        else:
            st.warning("❗ Pastikan input valid:\n- Kebutuhan > 0\n- Usia pensiun > usia sekarang")

    with col2:
        if st.button("🔄 Ulangi Perhitungan"):
            st.session_state["reset_input"] = True
            st.rerun()
    
    # Tampilkan hasil
    if st.session_state["hasil"] is not None:
         st.markdown(f"""
    <style>
    .hasil-container {{
        background-color:#e6f4ea;
        padding:20px;
        border-left:5px solid #34a853;
        border-right:5px solid #34a853;
        border-radius:10px;
        font-size:18px;
        font-family:Arial, sans-serif;
        line-height:1.8;
    }}
    @media only screen and (max-width: 600px) {{
        .hasil-container {{
            font-size:16px;
            padding:15px;
            line-height:1.5;
        }}
    }}
    </style>
    <div class="hasil-container">
        🛒 <b>Kebutuhan bulanan di masa depan:</b><br> Rp {st.session_state['hasil']['nilai_bulanan']:,.0f}<br><br>
        📅 <b>Kebutuhan tahunan di masa depan:</b><br> Rp {st.session_state['hasil']['nilai_tahunan']:,.0f}<br><br>
        💰 <b>Total tabungan yang harus dimiliki:</b><br> Rp {st.session_state['hasil']['total_tabungan']:,.0f}<br><br>
        💸 <b>Uang yang harus ditabung setiap bulan:</b><br> Rp {st.session_state['hasil']['tabungan_bulanan']:,.0f}
    </div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("⬅️ Kembali ke Halaman Utama"):
        go_to("home")

    st.markdown("""
    <style>
    div.stButton > button {
        background-color: white;
        border: 2px solid #1f84d9 !important;
        color: white;
        border-radius: 10px !important;
        border: none;
        width: auto;
        ;
    }
    /* Styling huruf dalam button */
    div.stButton > button > div > p {
    font-size: 16px !important;
    font-weight: 550 !important;
    color: black !important
}       

    div.stButton > button:hover {
    background-color: #1f84d9!important;
        color: white ! important; 
        font-weight: bold !important;
        text-decoration: none !important;

}
    </style>
""", unsafe_allow_html=True)    
# ===========================
# LIHAT RIWAYAT SIMULASI
# ===========================
    st.markdown("---")
    st.markdown("""
    <style>     
    details {
        border: 2px solid #6c3c0c !important;
        border-radius: 16px !important;
        background-color: white !important;
    }            

    </style>
""", unsafe_allow_html=True)

    st.markdown("""
    <style>
    .streamlit-expanderHeader {
        color: #5D3A00 !important; /* coklat */
        font-weight: 500;
    }
    details summary span {
        color: #5D3A00 !important;
    }
    </style>
""", unsafe_allow_html=True)
    
    with st.expander("📜 Lihat Riwayat Simulasi"):
        try:
            response = supabase.table("simulasi_pensiun").select("*").order("created_at", desc=True).limit(20).execute()
            data = response.data

            if data:
                st.dataframe(data)
            else:
                st.info("Belum ada riwayat tersimpan.")
        except Exception as e:
            st.error(f"❌ Gagal mengambil data: {e}")

# ===============================
# RENDER HALAMAN SESUAI STATE
# ===============================
if st.session_state["halaman"] == "home":
    halaman_home()
elif st.session_state["halaman"] == "simulasi":
    halaman_simulasi()





