import joblib
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import socket

# Load the trained model
model = joblib.load("phishing_url_classifier.joblib")

# Define feature columns for creating a DataFrame
feature_columns = [
    'length_url', 'length_hostname', 'ip', 'nb_dots', 'nb_hyphens',
    'nb_at', 'nb_qm', 'nb_and', 'nb_or', 'nb_eq',
    'nb_underscore', 'nb_tilde', 'nb_percent', 'nb_slash', 'nb_star',
    'nb_colon', 'nb_comma', 'nb_semicolumn', 'nb_dollar', 'nb_space',
    'nb_www', 'nb_com', 'nb_dslash', 'http_in_path', 'https_token',
    'ratio_digits_url', 'ratio_digits_host', 'punycode', 'port', 'tld_in_path',
    'tld_in_subdomain', 'abnormal_subdomain', 'nb_subdomains', 'prefix_suffix',
    'random_domain', 'shortening_service', 'path_extension', 'nb_redirection',
    'nb_external_redirection', 'length_words_raw', 'char_repeat', 
    'shortest_words_raw', 'shortest_word_host', 'shortest_word_path', 
    'longest_words_raw', 'longest_word_host', 'longest_word_path', 
    'avg_words_raw', 'avg_word_host', 'avg_word_path', 'phish_hints',
    'domain_in_brand', 'brand_in_subdomain', 'brand_in_path', 
    'suspecious_tld', 'statistical_report', 'nb_hyperlinks', 
    'ratio_intHyperlinks', 'ratio_extHyperlinks', 'ratio_nullHyperlinks', 
    'nb_extCSS', 'ratio_intRedirection', 'ratio_extRedirection', 
    'ratio_intErrors', 'ratio_extErrors', 'login_form', 'external_favicon', 
    'links_in_tags', 'submit_email', 'ratio_intMedia', 'ratio_extMedia',
    'sfh', 'iframe', 'popup_window', 'safe_anchor', 'onmouseover', 
    'right_clic', 'empty_title', 'domain_in_title', 
    'domain_with_copyright', 'whois_registered_domain', 
    'domain_registration_length', 'domain_age', 'web_traffic', 
    'dns_record', 'google_index', 'page_rank'
]

# Function to extract features from a URL (Placeholder)
def extract_features_from_url(url):
    features = [0] * 87  # Replace with actual feature extraction logic
    return pd.DataFrame([features], columns=feature_columns)

# Function to check if a domain exists using DNS
def domain_exists(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False

# Function to use Selenium to follow redirects and get the final URL
def get_final_url(initial_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    final_url = initial_url
    try:
        driver.get(initial_url)
        final_url = driver.current_url
    except Exception as e:
        print(f"Error navigating URL: {e}")
    finally:
        driver.quit()
    
    return final_url

# Function to predict URL legitimacy with redirection handling
def predict_url(url):
    # Step 1: Check if the initial domain exists
    initial_domain = url.split('/')[2]
    if not domain_exists(initial_domain):
        return "C"
    
    # Step 2: Use Selenium to follow redirects and get the final URL
    final_url = get_final_url(url)
    final_domain = final_url.split('/')[2]

    # Step 3: Check if the final domain exists
    if not domain_exists(final_domain):
        return "C"
    
    # Step 4: Extract features and classify the final URL
    url_features = extract_features_from_url(final_url)
    prediction = model.predict(url_features)
    
    # Step 5: Determine category based on prediction and domain existence
    if prediction[0] == 0:  # Legitimate
        return "A"
    else:  # Phishing
        return "B"
