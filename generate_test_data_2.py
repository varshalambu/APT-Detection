"""
Generate 2nd test dataset - apt_test_data_400.csv
Different patterns for additional testing
"""

import pandas as pd
import numpy as np

# Set random seed for different patterns
np.random.seed(123)

n_records = 400

# Feature names (80 features)
features = [
    'tcp_flags', 'udp_flags', 'icmp_type', 'protocol_type', 'ip_version', 'ttl',
    'total_packets', 'packets_forward', 'packets_backward', 'packet_length_avg',
    'packet_length_std', 'packet_length_min', 'packet_length_max', 'packet_iat_avg',
    'packet_iat_std', 'packet_iat_min', 'total_bytes', 'bytes_forward', 'bytes_backward', 'byte_rate_forward',
    'byte_rate_backward', 'byte_length_avg', 'byte_length_std', 'byte_length_min',
    'byte_length_max', 'byte_iat_avg', 'flow_duration', 'flow_start_time', 'flow_end_time', 'active_time_avg',
    'active_time_std', 'active_time_min', 'active_time_max', 'idle_time_avg',
    'idle_time_std', 'idle_time_min', 'init_win_size_forward', 'init_win_size_backward', 'window_size_forward',
    'window_size_backward', 'syn_count', 'fin_count', 'rst_count', 'ack_count',
    'psh_count', 'urg_count', 'header_length_forward', 'header_length_backward', 'fwd_psh_flags',
    'bwd_psh_flags', 'fwd_urg_flags', 'bwd_urg_flags', 'fwd_header_length',
    'bwd_header_length', 'subflow_fwd_packets', 'subflow_fwd_bytes', 'subflow_bwd_packets', 'subflow_bwd_bytes', 'dns_queries', 'dns_responses',
    'http_requests', 'http_responses', 'https_handshakes', 'ssl_certificates',
    'tls_versions', 'certificate_length', 'entropy_payload', 'entropy_header', 'payload_variance', 'header_variance',
    'suspicious_ports_count', 'blacklist_lookups', 'geolocation_changes',
    'asn_changes', 'failed_login_attempts', 'successful_logins',
    'data_exfiltration_indicators', 'c2_communication_score', 'malware_signature_hits',
    'anomaly_score'
]

# Generate data
data = {}
for feature in features:
    if 'count' in feature or 'hits' in feature or 'attempts' in feature:
        data[feature] = np.random.randint(0, 100, n_records)
    elif 'score' in feature or 'entropy' in feature or 'indicators' in feature:
        data[feature] = np.random.uniform(0, 1, n_records)
    elif 'length' in feature or 'size' in feature:
        data[feature] = np.random.randint(0, 65535, n_records)
    elif 'time' in feature or 'duration' in feature or 'iat' in feature:
        data[feature] = np.random.exponential(scale=150, size=n_records)
    elif 'rate' in feature:
        data[feature] = np.random.uniform(0, 10000, n_records)
    elif 'changes' in feature or 'lookups' in feature:
        data[feature] = np.random.randint(0, 10, n_records)
    else:
        data[feature] = np.random.uniform(0, 1000, n_records)

df = pd.DataFrame(data)

# Create distinct patterns for testing

# Pattern 1: Heavy C2 & Exfiltration (samples 0-100)
df.loc[0:100, 'c2_communication_score'] = np.random.uniform(0.75, 0.99, 101)
df.loc[0:100, 'data_exfiltration_indicators'] = np.random.uniform(0.70, 0.95, 101)
df.loc[0:100, 'bytes_backward'] = np.random.randint(500000, 2000000, 101)
df.loc[0:100, 'entropy_payload'] = np.random.uniform(0.80, 0.98, 101)
df.loc[0:100, 'anomaly_score'] = np.random.uniform(0.65, 0.90, 101)

# Pattern 2: Port scanning & Reconnaissance (samples 101-200)
df.loc[101:200, 'dns_queries'] = np.random.randint(20, 80, 100)
df.loc[101:200, 'suspicious_ports_count'] = np.random.randint(10, 40, 100)
df.loc[101:200, 'syn_count'] = np.random.randint(5, 20, 100)
df.loc[101:200, 'ff_count'] = np.random.randint(0, 5, 100)
df.loc[101:200, 'anomaly_score'] = np.random.uniform(0.45, 0.75, 100)

# Pattern 3: Clean/Benign traffic (samples 201-300)
df.loc[201:300, 'flow_duration'] = np.random.uniform(50, 300, 100)
df.loc[201:300, 'c2_communication_score'] = np.random.uniform(0.0, 0.15, 100)
df.loc[201:300, 'data_exfiltration_indicators'] = np.random.uniform(0.0, 0.10, 100)
df.loc[201:300, 'entropy_payload'] = np.random.uniform(0.25, 0.50, 100)
df.loc[201:300, 'anomaly_score'] = np.random.uniform(0.0, 0.20, 100)

# Pattern 4: Initial compromise/Exploitation (samples 301-399)
df.loc[301:399, 'failed_login_attempts'] = np.random.randint(10, 60, 99)
df.loc[301:399, 'malware_signature_hits'] = np.random.randint(2, 15, 99)
df.loc[301:399, 'rst_count'] = np.random.randint(5, 25, 99)
df.loc[301:399, 'entropy_header'] = np.random.uniform(0.60, 0.85, 99)
df.loc[301:399, 'anomaly_score'] = np.random.uniform(0.50, 0.85, 99)

# Handle NaN values
df = df.fillna(0)

# Save to CSV
output_file = 'apt_test_data_400.csv'
df.to_csv(output_file, index=False)

print(f"✓ Generated {n_records} test records")
print(f"✓ {len(features)} network traffic features")
print(f"✓ File saved: {output_file}")
print(f"\nData Summary:")
print(f"  - Shape: {df.shape}")
print(f"  - Pattern 1 (0-100): C2 & Exfiltration")
print(f"  - Pattern 2 (101-200): Reconnaissance")
print(f"  - Pattern 3 (201-300): Benign Traffic")
print(f"  - Pattern 4 (301-399): Initial Access/Exploitation")
print(f"\n✓ Ready for testing!")
print(f"  Upload '{output_file}' to the APT Detection Dashboard")
