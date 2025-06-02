"""
Search Engine Configuration
Centralized configuration for easy tuning of scoring parameters
"""

# Refined scoring configuration
REFINED_SCORING_CONFIG = {
    # Phrase match scoring - reduced from excessive values
    'trigram_title_bonus': 5.0,      # Was 10.0 - reduced 50%
    'trigram_body_bonus': 1.5,       # Was 2.0 - reduced 25%
    'bigram_title_bonus': 2.5,       # Was 5.0 - reduced 50%
    'bigram_body_bonus': 0.8,        # Was 1.0 - reduced 20%
    
    # Individual term scoring
    'title_fraction_multiplier': 2.0,  # Was 3.0 - reduced 33%
    'body_term_base': 0.1,            # Unchanged
    'body_term_max': 1.5,             # Was 2.0 - reduced 25%
    
    # Structure-based scoring with caps to prevent dominance
    'summary_multiplier': 2.5,        # Was 4.0 - reduced 37.5%
    'summary_max_contribution': 3.0,   # New cap
    'header_base_weight': 2.0,        # Was 3.0 - reduced 33%
    'header_max_contribution': 2.5,   # New cap
    'key_points_multiplier': 2.0,     # Was 3.6 - reduced 44%
    'key_points_max_contribution': 2.0, # New cap
    
    # Entity/concept bonuses
    'entity_bonus': 1.5,              # Was 2.0 - reduced 25%
    'concept_bonus': 1.0,             # Was 1.5 - reduced 33%
    
    # Proximity scoring
    'proximity_max_contribution': 1.0, # New cap
}

# Query intent detection patterns
INTENT_PATTERNS = {
    'instruction_seeking': [
        r'\bhow to\b', r'\bsteps?\s+(?:for|to)\b', r'\bbest way to\b',
        r'\bguide\s+(?:for|to)\b', r'\btutorial\b', r'\binstructions?\b'
    ],
    'comparison_seeking': [
        r'\bvs?\b', r'\bversus\b', r'\bcompare\b', r'\bdifference\s+between\b',
        r'\bwhich\s+is\s+better\b', r'\bbetter\s+than\b'
    ],
    'troubleshooting': [
        r'\bwhy\s+(?:isn\'?t|not|won\'?t|can\'?t)\b', r'\bwhat\s+went\s+wrong\b',
        r'\bfix\b', r'\btroubleshoot\b', r'\berror\b', r'\bissue\b',
        r'\bproblem\b', r'\bdebug\b'
    ],
    'discovery': [
        r'\bfind\s+all\b', r'\bshow\s+me\b', r'\blist\b',
        r'\bwhat\s+are\s+(?:all\s+)?the\b', r'\bgive\s+me\s+(?:all\s+)?the\b'
    ],
    'version_specific': [
        r'\b20\d{2}\b', r'\bv\d+\.\d+\b', r'\bversion\s+\d+\b',
        r'\blatest\b', r'\brecent\b', r'\bnew\b', r'\bupdated?\b'
    ]
}

# Recency bias settings
RECENCY_CONFIG = {
    'decay_days': 180,          # Content loses 50% relevance after 180 days
    'bias_range': (0.8, 1.2),  # Recency factor range (min, max)
    'troubleshooting_bias': True,    # Apply recency for troubleshooting
    'discovery_bias': True,          # Apply recency for discovery
    'instruction_bias': False,       # Don't apply recency for how-to guides
    'comparison_bias': False,        # Don't apply recency for comparisons
    'information_bias': False       # Don't apply recency for general knowledge
}

# Content length preferences
LENGTH_CONFIG = {
    'very_short_penalty': 0.7,      # < 100 words
    'short_start': 100,             # Words where penalty starts improving
    'optimal_start': 300,           # Words where content becomes optimal
    'optimal_end': 1000,            # Words where content is still optimal
    'long_penalty_rate': 0.1,      # Penalty rate for very long content
    'max_penalty': 0.1,             # Maximum penalty for very long content
}

# Clustering settings
CLUSTERING_CONFIG = {
    'similarity_threshold': 0.5,    # Threshold for clustering similar results
    'cluster_score_factor': 0.5,    # Factor for additional cluster members
    'diversity_penalty_rate': 0.15, # Rate for category diversity penalty
    'cluster_member_factor': 0.8,   # Score factor for non-primary cluster members
}

# LLM intent analysis settings
LLM_INTENT_CONFIG = {
    'use_llm_analysis': True,       # Whether to try LLM analysis first
    'fallback_confidence': 0.8,    # Max confidence for pattern-based fallback
    'default_confidence': 0.3,     # Confidence when defaulting to information_seeking
    'required_fields': ['intent_type', 'confidence'],  # Required fields in LLM response
}

def get_scoring_config():
    """Get the current scoring configuration"""
    return REFINED_SCORING_CONFIG.copy()

def get_intent_patterns():
    """Get the current intent detection patterns"""
    return INTENT_PATTERNS.copy()

def get_recency_config():
    """Get the current recency bias configuration"""
    return RECENCY_CONFIG.copy()

def get_length_config():
    """Get the current content length configuration"""
    return LENGTH_CONFIG.copy()

def get_clustering_config():
    """Get the current clustering configuration"""
    return CLUSTERING_CONFIG.copy()

def get_llm_intent_config():
    """Get the current LLM intent analysis configuration"""
    return LLM_INTENT_CONFIG.copy()

def update_scoring_config(**kwargs):
    """Update scoring configuration parameters"""
    global REFINED_SCORING_CONFIG
    for key, value in kwargs.items():
        if key in REFINED_SCORING_CONFIG:
            REFINED_SCORING_CONFIG[key] = value
        else:
            print(f"Warning: Unknown scoring config key: {key}")

def update_recency_config(**kwargs):
    """Update recency bias configuration parameters"""
    global RECENCY_CONFIG
    for key, value in kwargs.items():
        if key in RECENCY_CONFIG:
            RECENCY_CONFIG[key] = value
        else:
            print(f"Warning: Unknown recency config key: {key}")

# Pre-defined configuration profiles for different use cases
CONFIG_PROFILES = {
    'balanced': {
        # Current refined settings - good balance
        'scoring': REFINED_SCORING_CONFIG,
        'recency': RECENCY_CONFIG
    },
    'precision_focused': {
        # Higher precision, lower recall
        'scoring': {
            **REFINED_SCORING_CONFIG,
            'trigram_title_bonus': 6.0,
            'bigram_title_bonus': 3.0,
            'title_fraction_multiplier': 2.5,
            'summary_max_contribution': 2.0,
            'header_max_contribution': 2.0
        },
        'recency': {
            **RECENCY_CONFIG,
            'decay_days': 120,  # Shorter decay for more recency bias
        }
    },
    'recall_focused': {
        # Higher recall, broader matching
        'scoring': {
            **REFINED_SCORING_CONFIG,
            'trigram_title_bonus': 4.0,
            'bigram_title_bonus': 2.0,
            'body_term_max': 2.0,
            'summary_max_contribution': 4.0,
            'header_max_contribution': 3.0
        },
        'recency': {
            **RECENCY_CONFIG,
            'decay_days': 240,  # Longer decay for less recency bias
        }
    }
}

def apply_config_profile(profile_name: str):
    """Apply a pre-defined configuration profile"""
    if profile_name not in CONFIG_PROFILES:
        print(f"Unknown profile: {profile_name}. Available: {list(CONFIG_PROFILES.keys())}")
        return False
    
    profile = CONFIG_PROFILES[profile_name]
    
    global REFINED_SCORING_CONFIG, RECENCY_CONFIG
    REFINED_SCORING_CONFIG.update(profile['scoring'])
    RECENCY_CONFIG.update(profile['recency'])
    
    print(f"Applied configuration profile: {profile_name}")
    return True