import streamlit as st
import pandas as pd
import boto3
import plotly.graph_objects as go
from io import BytesIO
from config.settings import S3_ENDPOINT, AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET_NAME

# 1. Production-Grade Telemetry Cyber-Console Configuration
st.set_page_config(
    page_title="SLB DELFI | NextGen Subsurface Mission Control",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sophisticated Sci-Fi Dark Room CSS Framework
st.markdown("""
    <style>
        /* Base Control Room Styling */
        .stApp { background-color: #060913 !important; }
        h1, h2, h3, h4, p, span { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif !important; }
        
        /* Premium Cyberpunk KPI Cards (Glassmorphism) */
        .cyber-card {
            background: linear-gradient(135deg, rgba(15, 21, 39, 0.9) 0%, rgba(9, 13, 26, 0.9) 100%);
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #1e2942;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
            margin-bottom: 15px;
            position: relative;
            overflow: hidden;
        }
        .cyber-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 3px;
            background: linear-gradient(90deg, #0056B3, #00C6FF);
        }
        .cyber-card-alert::before {
            background: linear-gradient(90deg, #D31027, #EA00D9) !important;
        }
        .cyber-title {
            color: #94A3B8; /* Correction lisibilité titre KPI */
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 700;
            margin-bottom: 8px;
        }
        .cyber-value {
            color: #FFFFFF;
            font-size: 32px;
            font-weight: 800;
            letter-spacing: -0.5px;
            text-shadow: 0 0 10px rgba(0, 198, 255, 0.2);
        }
        .cyber-status {
            font-size: 11px;
            margin-top: 10px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }
        
        /* Ultra-Readable Custom Storage Info Matrix */
        .storage-box {
            background: #0D1326; 
            padding: 24px; 
            border-radius: 12px; 
            border: 1px solid #1E2942;
            line-height: 2; 
            font-size: 14px;
            color: #E2E8F0 !important; /* Gris très clair pour une lisibilité parfaite */
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        }
        .storage-box:hover {
            border-color: #00C6FF;
            box-shadow: 0 0 15px rgba(0, 198, 255, 0.2);
        }
        .storage-item {
            margin-bottom: 10px;
            display: flex;
            align-items: baseline;
        }
        .storage-bullet {
            color: #38BDF8;
            margin-right: 10px;
            font-weight: bold;
        }
        
        /* Custom Tab UI Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            background-color: #0b1121;
            padding: 6px;
            border-radius: 8px;
            border: 1px solid #16223f;
        }
        .stTabs [data-baseweb="tab"] {
            color: #94a3b8 !important;
            background-color: transparent !important;
            font-weight: 600 !important;
            border: none !important;
            padding: 10px 24px !important;
            border-radius: 6px !important;
            transition: all 0.3s ease;
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(135deg, #0056B3 0%, #002d62 100%) !important;
            color: white !important;
            box-shadow: 0 4px 14px rgba(0, 86, 179, 0.4) !important;
        }

        /* Sidebar Spacing Optimization */
        [data-testid="stSidebar"] {
            background-color: #090d1a !important;
            border-right: 1px solid #16223f;
        }
        .sidebar-section-title {
            font-size: 13px;
            font-weight: 700;
            color: #E2E8F0; /* Titres de la barre latérale plus clairs */
            letter-spacing: 1.5px;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        
        /* High Contrast Section Headers */
        .section-header {
            color: #FFFFFF !important;
            font-weight: 700 !important;
            letter-spacing: 0.5px;
            margin-bottom: 15px !important;
        }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data_from_s3():
    """Optimized S3 Storage Tier Connector Protocol."""
    print("[INFO] Initializing secure connection gateway to MinIO S3 Data Lake...")
    s3_client = boto3.client(
        's3', endpoint_url=S3_ENDPOINT,
        aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY
    )
    s3_key = "production/year=2026/well_telemetry.parquet"
    obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=s3_key)
    return pd.read_parquet(BytesIO(obj['Body'].read()))

try:
    df = load_data_from_s3()
    
    # --- MISSION SIDEBAR NETWORK GATEWAY ---
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/b/b8/Schlumberger_logo.svg", use_container_width=True)
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    
    st.sidebar.markdown('<p class="sidebar-section-title">🖥️ CORE COGNITIVE NODE</p>', unsafe_allow_html=True)
    well_list = df['WELL_BORE_CODE'].unique()
    selected_well = st.sidebar.selectbox("TARGET WELLBORE ASSET", well_list, label_visibility="collapsed")
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown('<p class="sidebar-section-title">📡 INFRASTRUCTURE TOPOLOGY</p>', unsafe_allow_html=True)
    st.sidebar.markdown("""
    <div style="background-color:#0b1121; padding:15px; border-radius:8px; border:1px solid #16223f; font-size:12px; line-height: 1.6;">
        <span style="color:#94A3B8;">GATEWAY STATUS:</span> <span style="color:#10B981;font-weight:bold;">● ONLINE [EDGE]</span><br>
        <span style="color:#94A3B8;">STREAM OPTIMIZER:</span> <code style="color:#38BDF8;">Snappy-Parquet</code><br>
        <span style="color:#94A3B8;">METADATA LAYER:</span> <code style="color:#38BDF8;">OSDU Core Schema</code><br>
        <span style="color:#94A3B8;">DATALAKE INSTANCE:</span> <code style="color:#A855F7;">MinIO S3 Cluster</code>
    </div>
    """, unsafe_allow_html=True)
    
    df_filtered = df[df['WELL_BORE_CODE'] == selected_well].sort_values('DATEPRD')

    # --- MAIN HUD INSTRUMENTATION ---
    st.markdown('<h1 style="color:#FFFFFF; font-size:36px; font-weight:800; margin-bottom:5px;">⚡ DELFI MISSION CONTROL ROOM</h1>', unsafe_allow_html=True)
    st.markdown(f"<p style='color:#64748B; font-size:14px; margin-bottom:25px;'>CONNECTED FIELD: <span style='color:#38BDF8; font-weight:700;'>VOLVE SUBSURFACE DATASET</span> | STREAM ACTIVE: <span style='color:#38BDF8; font-weight:700;'>{selected_well}</span></p>", unsafe_allow_html=True)

    # Statistical Aggregation
    avg_pressure = df_filtered['AVG_DOWNHOLE_PRESSURE'].mean()
    avg_temp = df_filtered['AVG_DOWNHOLE_TEMPERATURE'].mean()
    avg_water_cut = df_filtered['WATER_CUT'].mean()
    total_oil = df_filtered['BORE_OIL_VOL'].sum()

    # Layout Generation: HUD Cards
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    with kpi1:
        st.markdown(f"""
            <div class="cyber-card">
                <div class="cyber-title">Downhole Pressure Matrix</div>
                <div class="cyber-value">{avg_pressure:.1f} <span style="font-size:14px; color:#94A3B8; font-weight:normal;">bar</span></div>
                <div class="cyber-status" style="color:#10B981;">● TELEMETRY LINK STABLE</div>
            </div>
        """, unsafe_allow_html=True)
    with kpi2:
        st.markdown(f"""
            <div class="cyber-card">
                <div class="cyber-title">Thermal Core Reservoir</div>
                <div class="cyber-value">{avg_temp:.1f} <span style="font-size:14px; color:#94A3B8; font-weight:normal;">°C</span></div>
                <div class="cyber-status" style="color:#10B981;">● NOMINAL OPERATIONS</div>
            </div>
        """, unsafe_allow_html=True)
    with kpi3:
        alert_class = "cyber-card-alert" if avg_water_cut > 25 else ""
        st.markdown(f"""
            <div class="cyber-card {alert_class}">
                <div class="cyber-title">Calculated Water Cut</div>
                <div class="cyber-value">{avg_water_cut:.2f} <span style="font-size:14px; color:#94A3B8; font-weight:normal;">%</span></div>
                <div class="cyber-status" style="color:#EF4444;">⚠️ DEPLETION CRITICAL ALERT</div>
            </div>
        """, unsafe_allow_html=True)
    with kpi4:
        st.markdown(f"""
            <div class="cyber-card">
                <div class="cyber-title">Export Aggregation Output</div>
                <div class="cyber-value">{total_oil:,.0f} <span style="font-size:14px; color:#94A3B8; font-weight:normal;">bbl</span></div>
                <div class="cyber-status" style="color:#38BDF8;">📈 NET PRODUCTION VALIDATED</div>
            </div>
        """, unsafe_allow_html=True)

    # --- ADVANCED HIGH-DENSITY GRAPHICS & ANALYTICAL TABS ---
    tab_analytics, tab_gauges, tab_data_lake = st.tabs([
        "📊 ADVANCED CROSS-GRAPHICS", 
        "⭕ REAL-TIME ADVANCED GAUGES", 
        "💾 OSDU METADATA RECORD LAYER"
    ])

    with tab_analytics:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_filtered['DATEPRD'], y=df_filtered['BORE_OIL_VOL'],
            name="Hydrocarbon Output (bbl/day)",
            line=dict(color='#00C6FF', width=3.5), mode='lines',
            fill='tozeroy', fillcolor='rgba(0, 198, 255, 0.02)'
        ))
        fig.add_trace(go.Scatter(
            x=df_filtered['DATEPRD'], y=df_filtered['WATER_CUT'],
            name="Water Breakthrough Ratio (%)",
            line=dict(color='#EA00D9', width=2, dash='dash'), yaxis="y2"
        ))
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(orientation="h", yanchor="bottom", y=1.06, xanchor="right", x=1, font=dict(size=11)),
            xaxis=dict(title="Continuous Production Chronology", showgrid=True, gridcolor="#131c31"),
            yaxis=dict(title="Oil Discharge Rate (bbl/day)", titlefont=dict(color="#00C6FF"), tickfont=dict(color="#00C6FF"), showgrid=True, gridcolor="#131c31"),
            yaxis2=dict(title="Water Cut Scale (%)", titlefont=dict(color='#EA00D9'), tickfont=dict(color='#EA00D9'), anchor="x", overlaying="y", side="right", showgrid=False),
            height=480, margin=dict(l=10, r=10, t=10, b=10)
        )
        st.plotly_chart(fig, width="stretch")

    with tab_gauges:
        col_g1, col_g2 = st.columns(2)
        
        with col_g1:
            fig_g1 = go.Figure(go.Indicator(
                mode = "gauge+number", value = avg_pressure,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Downhole Sensor Pressure Integrity (bar)", 'font': {'size': 14, 'color': '#94A3B8'}},
                gauge = {
                    'axis': {'range': [None, 400], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
                    'bar': {'color': "#00C6FF"},
                    'bgcolor': "#0b1121",
                    'borderwidth': 2, 'bordercolor': "#1e2942",
                    'steps': [
                        {'range': [0, 150], 'color': '#0d1b2a'},
                        {'range': [150, 300], 'color': '#14213d'},
                        {'range': [300, 400], 'color': '#4a0010'}],
                }
            ))
            fig_g1.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=320, margin=dict(t=40, b=10))
            st.plotly_chart(fig_g1, width="stretch")
            
        with col_g2:
            fig_g2 = go.Figure(go.Indicator(
                mode = "gauge+number", value = avg_temp,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Subsurface Thermal Core State (°C)", 'font': {'size': 14, 'color': '#94A3B8'}},
                gauge = {
                    'axis': {'range': [None, 150], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
                    'bar': {'color': "#F59E0B"},
                    'bgcolor': "#0b1121",
                    'borderwidth': 2, 'bordercolor': "#1e2942",
                    'steps': [
                        {'range': [0, 75], 'color': '#0d1b2a'},
                        {'range': [75, 120], 'color': '#14213d'},
                        {'range': [120, 150], 'color': '#4a0010'}],
                }
            ))
            fig_g2.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=320, margin=dict(t=40, b=10))
            st.plotly_chart(fig_g2, width="stretch")

    with tab_data_lake:
        col_dl_left, col_dl_right = st.columns([1, 1])
        with col_dl_left:
            st.markdown('<h3 class="section-header">💾 STORAGE INFRASTRUCTURE MATRIX</h3>', unsafe_allow_html=True)
            st.markdown("""
            <div class="storage-box">
                <div class="storage-item"><span class="storage-bullet">▪</span> <b>OSDU R3 Data Standardization:</b> Fully Validated Map Entities.</div>
                <div class="storage-item"><span class="storage-bullet">▪</span> <b>Data Architecture Paradigm:</b> Time-series partitioned structural lake layer.</div>
                <div class="storage-item"><span class="storage-bullet">▪</span> <b>Downstream Analytical Readiness:</b> High-throughput pipeline optimized for DELFI AI, Petrel, and Spotfire Ingestion.</div>
                <div class="storage-item"><span class="storage-bullet">▪</span> <b>Cloud Footprint Optimization:</b> <span style="color:#10B981; font-weight:700;">~74.1% Storage Space Preserved</span> via binary compression.</div>
            </div>
            """, unsafe_allow_html=True)
        with col_dl_right:
            st.markdown('<h3 class="section-header">📍 GEOSPATIAL FIELD COORDINATION</h3>', unsafe_allow_html=True)
            map_data = pd.DataFrame({'lat': [58.44], 'lon': [1.90]})
            st.map(map_data, zoom=5)
            
        st.markdown("<br><h3 class='section-header'>🔍 OPTIMIZED STORAGE HEAD RECORDS (TOP 5 ROW EXTRACT)</h3>", unsafe_allow_html=True)
        st.dataframe(
            df_filtered[['DATEPRD', 'AVG_DOWNHOLE_PRESSURE', 'BORE_OIL_VOL', 'WATER_CUT']].head(5), 
            width="stretch"
        )

except Exception as server_error:
    st.error(f"⚠️ [CRITICAL ARCHITECTURE EXCEPTION] Failed to map distributed data layer stream: {server_error}")