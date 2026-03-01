"""
Generate 1000 test records for APT Detection Dashboard
Network traffic feature simulation with diverse patterns
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate 1000 records
n_records = 1000

# Create feature names (80 features representing network traffic characteristics)
features = [
    # Protocol features (0-5)
    'tcp_flags', 'udp_flags', 'icmp_type', 'protocol_type', 'ip_version', 'ttl',
    
    # Packet statistics (6-15)
    'total_packets', 'packets_forward', 'packets_backward', 'packet_length_avg',
    'packet_length_std', 'packet_length_min', 'packet_length_max', 'packet_iat_avg',
    'packet_iat_std', 'packet_iat_min',
    
    # Byte statistics (16-25)
    'total_bytes', 'bytes_forward', 'bytes_backward', 'byte_rate_forward',
    'byte_rate_backward', 'byte_length_avg', 'byte_length_std', 'byte_length_min',
    'byte_length_max', 'byte_iat_avg',
    
    # Duration features (26-35)
    'flow_duration', 'flow_start_time', 'flow_end_time', 'active_time_avg',
    'active_time_std', 'active_time_min', 'active_time_max', 'idle_time_avg',
    'idle_time_std', 'idle_time_min',
    
    # Window and flag features (36-45)
    'init_win_size_forward', 'init_win_size_backward', 'window_size_forward',
    'window_size_backward', 'syn_count', 'fin_count', 'rst_count', 'ack_count',
    'psh_count', 'urg_count',
    
    # Statistical features (46-55)
    'header_length_forward', 'header_length_backward', 'fwd_psh_flags',
    'bwd_psh_flags', 'fwd_urg_flags', 'bwd_urg_flags', 'fwd_header_length',
    'bwd_header_length', 'subflow_fwd_packets', 'subflow_fwd_bytes',
    
    # Additional traffic characteristics (56-65)
    'subflow_bwd_packets', 'subflow_bwd_bytes', 'dns_queries', 'dns_responses',
    'http_requests', 'http_responses', 'https_handshakes', 'ssl_certificates',
    'tls_versions', 'certificate_length',
    
    # Anomaly indicators (66-75)
    'entropy_payload', 'entropy_header', 'payload_variance', 'header_variance',
    'suspicious_ports_count', 'blacklist_lookups', 'geolocation_changes',
    'asn_changes', 'failed_login_attempts', 'successful_logins',
    
    # Traffic pattern features (76-79)
    'data_exfiltration_indicators', 'c2_communication_score', 'malware_signature_hits',
    'anomaly_score'
]

# Verify we have 80 features
assert len(features) == 80, f"Expected 80 features, got {len(features)}"

# Generate synthetic data with patterns for different scenarios
data = {}

for feature in features:
    if 'count' in feature or 'hits' in feature or 'attempts' in feature:
        # Integer counts
        data[feature] = np.random.randint(0, 100, n_records)
    elif 'score' in feature or 'entropy' in feature or 'indicators' in feature:
        # Normalized scores (0-1)
        data[feature] = np.random.uniform(0, 1, n_records)
    elif 'length' in feature or 'size' in feature:
        # Packet/header sizes in bytes
        data[feature] = np.random.randint(0, 65535, n_records)
    elif 'time' in feature or 'duration' in feature or 'iat' in feature:
        # Time-related features
        data[feature] = np.random.exponential(scale=100, size=n_records)
    elif 'rate' in feature:
        # Rate features
        data[feature] = np.random.uniform(0, 10000, n_records)
    elif 'changes' in feature or 'lookups' in feature or 'distance' in feature:
        # Binary or small integer features
        data[feature] = np.random.randint(0, 10, n_records)
    else:
        # General numeric features
        data[feature] = np.random.uniform(0, 1000, n_records)

# Create DataFrame
df = pd.DataFrame(data)

# Introduce some realistic patterns for different types of traffic
# Pattern 1: Normal traffic (samples 0-300)
df.loc[0:300, 'flow_duration'] = np.random.uniform(100, 500, 301)
df.loc[0:300, 'entropy_payload'] = np.random.uniform(0.3, 0.6, 301)
df.loc[0:300, 'c2_communication_score'] = np.random.uniform(0.0, 0.2, 301)
df.loc[0:300, 'data_exfiltration_indicators'] = np.random.uniform(0.0, 0.15, 301)

# Pattern 2: Reconnaissance activity (samples 301-500)
df.loc[301:500, 'dns_queries'] = np.random.randint(10, 50, 200)
df.loc[301:500, 'suspicious_ports_count'] = np.random.randint(5, 20, 200)
df.loc[301:500, 'anomaly_score'] = np.random.uniform(0.4, 0.7, 200)
df.loc[301:500, 'geolocation_changes'] = np.random.randint(1, 5, 200)

# Pattern 3: C2 Communication (samples 501-700)
df.loc[501:700, 'c2_communication_score'] = np.random.uniform(0.6, 0.95, 200)
df.loc[501:700, 'flow_duration'] = np.random.uniform(1000, 5000, 200)
df.loc[501:700, 'packet_iat_std'] = np.random.uniform(50, 500, 200)
df.loc[501:700, 'https_handshakes'] = np.random.randint(2, 10, 200)

# Pattern 4: Data Exfiltration (samples 701-900)
df.loc[701:900, 'data_exfiltration_indicators'] = np.random.uniform(0.6, 0.95, 200)
df.loc[701:900, 'bytes_backward'] = np.random.randint(100000, 1000000, 200)
df.loc[701:900, 'entropy_payload'] = np.random.uniform(0.7, 0.95, 200)
df.loc[701:900, 'byte_rate_backward'] = np.random.uniform(5000, 50000, 200)

# Pattern 5: Initial Access/Exploitation (samples 901-1000)
df.loc[901:999, 'failed_login_attempts'] = np.random.randint(5, 50, 99)
df.loc[901:999, 'malware_signature_hits'] = np.random.randint(1, 10, 99)
df.loc[901:999, 'rst_count'] = np.random.randint(2, 20, 99)
df.loc[901:999, 'anomaly_score'] = np.random.uniform(0.5, 0.8, 99)

# Handle any NaN values
df = df.fillna(0)

# Save to CSV
output_file = 'apt_test_data_1000.csv'
df.to_csv(output_file, index=False)

print(f"✓ Generated {n_records} test records")
print(f"✓ {len(features)} network traffic features")
print(f"✓ File saved: {output_file}")
print(f"\nData Summary:")
print(f"  - Shape: {df.shape}")
print(f"  - Features: {', '.join(features[:5])}... and {len(features)-5} more")
print(f"\nData Statistics:")
print(df.describe())

print("\n✓ Ready for dashboard testing!")
print(f"  Upload '{output_file}' to the APT Detection Dashboard at http://127.0.0.1:7861")
